from fastapi import APIRouter, HTTPException
from models import Order

router = APIRouter()

# Sample data for orders
orders = [{"id": 1, "item_id": 1, "user_id": 1, "quantity": 2, "total_price": 40.0}]

@router.get("/orders", tags=["Orders"])
def get_orders():
    """Retrieve all orders."""
    return orders

@router.post("/orders", tags=["Orders"])
def create_order(order: Order):
    """Create a new order."""
    orders.append(order.dict())
    return {"message": "Order created successfully", "order": order}

@router.put("/orders/{order_id}", tags=["Orders"])
def update_order(order_id: int, order: Order):
    """Update an existing order."""
    for existing_order in orders:
        if existing_order["id"] == order_id:
            existing_order.update(order.dict())
            return {"message": "Order updated successfully", "order": existing_order}
    raise HTTPException(status_code=404, detail="Order not found")

@router.delete("/orders/{order_id}", tags=["Orders"])
def delete_order(order_id: int):
    """Delete an order."""
    for existing_order in orders:
        if existing_order["id"] == order_id:
            orders.remove(existing_order)
            return {"message": "Order deleted successfully"}
    raise HTTPException(status_code=404, detail="Order not found")
