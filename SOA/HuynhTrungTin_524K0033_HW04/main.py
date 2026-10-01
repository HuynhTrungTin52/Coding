from typing import Annotated

from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field

app = FastAPI()


class OrderUpdate(BaseModel):
    status: str
    note: str = None


class OrderItem(BaseModel):
    product_id: int = Field(gt=0)
    product_name: str
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class OrderCreate(BaseModel):
    customer_name: str
    shipping_address: Address
    items: list[OrderItem] = Field(min_length=1)


orders = [
    {
        "order_id": 1,
        "customer_name": "Nguyen Van An",
        "shipping_address": {
            "street": "19 Nguyen Huu Tho",
            "city": "Ho Chi Minh City",
            "postal_code": "700000"
        },
        "items": [
            {
                "product_id": 1,
                "product_name": "Laptop",
                "quantity": 1,
                "unit_price": 1200.0
            },
            {
                "product_id": 2,
                "product_name": "Wireless Mouse",
                "quantity": 2,
                "unit_price": 25.5
            }
        ],
        "total_amount": 1251.0,
        "status": "pending",
        "note": None
    },
    {
        "order_id": 2,
        "customer_name": "Nguyen Van B",
        "shipping_address": {
            "street": "123 Le Loi",
            "city": "Ho Chi Minh City",
            "postal_code": "700000"
        },
        "items": [
            {
                "product_id": 3,
                "product_name": "Keyboard",
                "quantity": 1,
                "unit_price": 100.0
            }
        ],
        "total_amount": 100.0,
        "status": "processing",
        "note": None
    }
]



@app.get("/orders")
async def get_orders():
    return orders


@app.get("/orders/{order_id}")
async def get_order(
    order_id: Annotated[int, Path(title="The ID of the order to get", gt=0)]
):
    for order in orders:
        if order["order_id"] == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")


@app.post("/orders")
async def create_order(order: OrderCreate):
    new_order_id = len(orders) + 1

    total_amount = sum(item.quantity * item.unit_price for item in order.items)

    new_order = {
        "order_id": new_order_id,
        "customer_name": order.customer_name,
        "shipping_address": order.shipping_address,
        "items": order.items,
        "total_amount": total_amount,
        "status": "pending",
        "note": None
    }

    orders.append(new_order)
    return new_order


@app.put("/orders/{order_id}")
async def update_order(
    order_id: Annotated[int, Path(title="The ID of the order to update", gt=0)],
    order_update: OrderUpdate,
    notify_customer: bool | None = None,
    priority: str | None = None,
):
    for order in orders:
        if order["order_id"] == order_id:
            order["status"] = order_update.status
            if order_update.note:
                order["note"] = order_update.note

            results = {"order_id": order_id, "order": order}
            if notify_customer is not None:
                results.update({"notify_customer": notify_customer})
            if priority:
                results.update({"priority": priority})
            return results

    raise HTTPException(status_code=404, detail="Order not found")