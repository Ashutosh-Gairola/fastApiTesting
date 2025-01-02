from pydantic import BaseModel
from typing import Optional

# Item model
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# User model
class User(BaseModel):
    id: int
    username: str
    email: str

# Order model
class Order(BaseModel):
    id: int
    item_id: int
    user_id: int
    quantity: int
    total_price: float
