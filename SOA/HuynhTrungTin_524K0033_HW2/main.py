from enum import Enum

from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

products = [
    {
        "product_id": 1,
        "name": "Laptop",
        "category": "electronics",
        "price": 1200.0,
        "in_stock": True,
    },
    {
        "product_id": 2,
        "name": "Wireless Mouse",
        "category": "electronics",
        "price": 25.5,
        "in_stock": True,
    },
    {
        "product_id": 3,
        "name": "Office Chair",
        "category": "furniture",
        "price": 180.0,
        "in_stock": False,
    },
    {
        "product_id": 4,
        "name": "Desk Lamp",
        "category": "furniture",
        "price": 35.0,
        "in_stock": True,
    },
    {
        "product_id": 5,
        "name": "Python Programming",
        "category": "books",
        "price": 45.0,
        "in_stock": True,
    },
]


class Category(str, Enum):
    Furniture = "furniture"
    Electronics = "electronics"


@app.get("/products/{product_id}")
async def return_product_id(product_id: int):
    is_product = next(
        (product for product in products if product["product_id"] == product_id), None
    )
    if is_product == None:
        # print(type(products[1]["product_id"])==type(product_id))
        raise HTTPException(status_code=404, detail="Product not found")

    return is_product


@app.get("/products")
def return_products(
    category: Category | None = Query(default=None, description="Pick a category"),
    min_price: float | None = None,
    max_price: float | None = None,
    in_stock: bool | None = None,
    keyword: str | None = None,
):
    if category:
        return [product for product in products if product["category"] == category]
    if min_price:
        return [product for product in products if product["price"] >= min_price]
    if max_price:
        return [product for product in products if product["price"] <= max_price]
    if in_stock is not None:
        print(type(in_stock))
        return [product for product in products if product["in_stock"] == in_stock]
    if keyword:
        keyword.lower()
        return [product for product in products if keyword in product["name"].lower()]
    return products


@app.get("/")
async def info():
    return {"service": "Student Service", "course": "504070"}


@app.get("/health")
async def status():
    return {"status": "healthy"}


# for product in products:
#     print(product["product_id"])
