from __future__ import annotations

import os
from threading import Lock
from uuid import uuid4

import httpx
import uvicorn
from fastapi import FastAPI, Header, HTTPException, status
from pydantic import BaseModel, Field


PROVIDER_URL = os.getenv("PAYMENT_PROVIDER_URL", "http://127.0.0.1:9000")
PAYMENT_API_KEY = os.getenv("PAYMENT_API_KEY", "demo-secret-key")
PROVIDER_API_KEY = os.getenv("PROVIDER_API_KEY", "demo-secret-key")
PROVIDER_TIMEOUT_SECONDS = float(os.getenv("PAYMENT_PROVIDER_TIMEOUT", "5.0"))


class PaymentRequest(BaseModel):
    order_id: str = Field(..., min_length=1)
    customer_name: str = Field(..., min_length=1)
    amount: float = Field(..., gt=0)


class ProviderPaymentRequest(BaseModel):
    order_reference: str = Field(..., min_length=1)
    customer: str = Field(..., min_length=1)
    amount: float = Field(..., gt=0)


class PaymentStatusUpdate(BaseModel):
    transaction_id: str = Field(..., min_length=1)
    status: str = Field(..., min_length=1)


provider_app = FastAPI(title="Mock Payment Provider")
app = FastAPI(title="Payment Service")

_processed_payments: dict[str, dict[str, str]] = {}
_processed_payments_lock = Lock()
payment_statuses: dict[str, str] = {}


@provider_app.post("/api/payments")
def process_payment(
    payment: ProviderPaymentRequest,
    x_api_key: str = Header(..., alias="X-API-Key"),
    idempotency_key: str | None = Header(None, alias="Idempotency-Key"),
) -> dict[str, str]:
    if x_api_key != PROVIDER_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
    if not idempotency_key:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Idempotency-Key header is required",
        )

    with _processed_payments_lock:
        existing_result = _processed_payments.get(idempotency_key)
        if existing_result is not None:
            return existing_result

        result = {
            "transaction_id": str(uuid4()),
            "status": "completed",
        }
        _processed_payments[idempotency_key] = result
        return result


def build_provider_payload(payment: PaymentRequest) -> dict[str, str | float]:
    return {
        "order_reference": payment.order_id,
        "customer": payment.customer_name,
        "amount": payment.amount,
    }


@app.post("/payments")
def create_payment(
    payment: PaymentRequest,
    idempotency_key: str | None = Header(None, alias="Idempotency-Key"),
) -> dict[str, str]:
    request_key = idempotency_key or str(uuid4())
    headers = {
        "X-API-Key": PAYMENT_API_KEY,
        "Idempotency-Key": request_key,
    }

    try:
        response = httpx.post(
            f"{PROVIDER_URL}/api/payments",
            json=build_provider_payload(payment),
            headers=headers,
            timeout=PROVIDER_TIMEOUT_SECONDS,
        )
    except httpx.TimeoutException as exc:
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="Payment provider request timed out",
        ) from exc
    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Payment provider is unavailable",
        ) from exc

    if response.status_code == status.HTTP_401_UNAUTHORIZED:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Payment provider authentication failed",
        )
    if response.status_code == status.HTTP_429_TOO_MANY_REQUESTS:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Payment provider rate limit exceeded",
        )
    if response.status_code >= 500:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Payment provider error",
        )
    if response.status_code != status.HTTP_200_OK:
        detail = "Payment request rejected"
        try:
            provider_detail = response.json().get("detail")
            if provider_detail:
                detail = str(provider_detail)
        except ValueError:
            pass
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
        )

    try:
        result = response.json()
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Payment provider returned invalid JSON",
        ) from exc

    if not isinstance(result, dict) or not result.get("transaction_id"):
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Payment provider returned an invalid payment response",
        )
    return {
        "transaction_id": str(result["transaction_id"]),
        "status": str(result.get("status", "unknown")),
    }


@app.post("/webhooks/payment-status")
def receive_payment_status(update: PaymentStatusUpdate) -> dict[str, bool | str]:
    payment_statuses[update.transaction_id] = update.status
    return {
        "received": True,
        "transaction_id": update.transaction_id,
        "status": update.status,
    }


if __name__ == "__main__":
    service_role = os.getenv("SERVICE_ROLE", "payment").lower()
    selected_app = provider_app if service_role == "provider" else app
    selected_port = 9000 if service_role == "provider" else 8000
    uvicorn.run(selected_app, host="127.0.0.1", port=selected_port)