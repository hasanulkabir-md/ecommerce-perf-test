from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Phone", "price": 800},
]
cart = []

class CartItem(BaseModel):
    product_id: int
    quantity: int

@app.get("/products")
def get_products():
    return products

@app.post("/cart")
def add_to_cart(item: CartItem):
    cart.append(item.dict())
    return {"msg": "Item added", "cart": cart}

@app.post("/checkout")
def checkout():
    total = sum([p["quantity"] * 100 for p in cart])
    cart.clear()
    return {"msg": "Order placed", "total": total}
