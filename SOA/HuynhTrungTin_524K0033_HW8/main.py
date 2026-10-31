import os
from threading import Lock
from uuid import uuid4

import httpx
import uvicorn
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field


PROVIDER_URL = os.getenv(
    "PAYMENT_PROVIDER_URL",
    "http://127.0.0.1:9000"
)
PAYMENT_API_KEY = os.getenv(
    "PAYMENT_API_KEY",
    "demo-secret-key"
)
PROVIDER_API_KEY = os.getenv(
    "PROVIDER_API_KEY",
    "demo-secret-key"
)
PROVIDER_TIMEOUT = float(
    os.getenv("PAYMENT_PROVIDER_TIMEOUT", "5.0")
)


class PaymentCreate(BaseModel):
    order_id: str = Field(..., min_length=1)
    customer_name: str = Field(..., min_length=1)
    amount: float = Field(..., gt=0)


class ProviderPayment(BaseModel):
    order_reference: str = Field(..., min_length=1)
    customer: str = Field(..., min_length=1)
    amount: float = Field(..., gt=0)


class PaymentStatus(BaseModel):
    transaction_id: str = Field(..., min_length=1)
    status: str = Field(..., min_length=1)


provider_app = FastAPI(title="Mock Payment Provider")
app = FastAPI(title="Payment Service")

processed_payments: dict[str, dict[str, str]] = {}
processed_payments_lock = Lock()
payment_statuses: dict[str, str] = {}


@provider_app.post("/api/payments")
def process_payment(
    payment: ProviderPayment,
    x_api_key: str = Header(..., alias="X-API-Key"),
    idempotency_key: str = Header(..., alias="Idempotency-Key")
):
    if x_api_key != PROVIDER_API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    with processed_payments_lock:
        if idempotency_key in processed_payments:
            return processed_payments[idempotency_key]

        result = {
            "transaction_id": str(uuid4()),
            "status": "completed"
        }
        processed_payments[idempotency_key] = result
        return result


def build_provider_payload(payment: PaymentCreate):
    return {
        "order_reference": payment.order_id,
        "customer": payment.customer_name,
        "amount": payment.amount
    }


@app.post("/payments")
def create_payment(
    payment: PaymentCreate,
    idempotency_key: str = Header(..., alias="Idempotency-Key")
):
    request_key = idempotency_key
    headers = {
        "X-API-Key": PAYMENT_API_KEY,
        "Idempotency-Key": request_key
    }

    try:
        response = httpx.post(
            f"{PROVIDER_URL}/api/payments",
            json=build_provider_payload(payment),
            headers=headers,
            timeout=PROVIDER_TIMEOUT
        )
    except httpx.TimeoutException as exc:
        raise HTTPException(
            status_code=504,
            detail="Payment provider request timed out"
        ) from exc
    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=503,
            detail="Payment provider is unavailable"
        ) from exc

    if response.status_code == 401:
        raise HTTPException(
            status_code=502,
            detail="Payment provider authentication failed"
        )

    if response.status_code == 429:
        raise HTTPException(
            status_code=503,
            detail="Payment provider rate limit exceeded"
        )

    if response.status_code >= 500:
        raise HTTPException(
            status_code=502,
            detail="Payment provider error"
        )

    if response.status_code != 200:
        detail = "Payment request rejected"
        try:
            provider_detail = response.json().get("detail")
            if provider_detail:
                detail = str(provider_detail)
        except ValueError:
            pass

        raise HTTPException(
            status_code=400,
            detail=detail
        )

    try:
        result = response.json()
    except ValueError as exc:
        raise HTTPException(
            status_code=502,
            detail="Payment provider returned invalid JSON"
        ) from exc

    if not isinstance(result, dict) or not result.get("transaction_id"):
        raise HTTPException(
            status_code=502,
            detail="Payment provider returned an invalid payment response"
        )

    return {
        "transaction_id": str(result["transaction_id"]),
        "status": str(result.get("status", "unknown"))
    }


@app.post("/webhooks/payment-status")
def receive_payment_status(update: PaymentStatus):
    payment_statuses[update.transaction_id] = update.status
    return {
        "received": True,
        "transaction_id": update.transaction_id,
        "status": update.status
    }

