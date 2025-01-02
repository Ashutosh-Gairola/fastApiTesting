from fastapi import APIRouter, HTTPException
from models import Item

router = APIRouter()

# Sample data for items
items = [{"id": 1, "name": "Item 1", "description": "This is item 1"}]

@router.get("/items", tags=["Items"])
def get_items():
    """Retrieve all items."""
    return items

@router.post("/items", tags=["Items"])
def create_item(item: Item):
    """Create a new item."""
    if any(existing_item["id"] == item.id for existing_item in items):
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items.append(item.dict())
    return {"message": "Item created successfully", "item": item}

@router.put("/items/{item_id}", tags=["Items"])
def update_item(item_id: int, item: Item):
    """Update an existing item."""
    for existing_item in items:
        if existing_item["id"] == item_id:
            existing_item.update(item.dict())
            return {"message": "Item updated successfully", "item": existing_item}
    raise HTTPException(status_code=404, detail="Item not found")

@router.delete("/items/{item_id}", tags=["Items"])
def delete_item(item_id: int):
    """Delete an item."""
    for existing_item in items:
        if existing_item["id"] == item_id:
            items.remove(existing_item)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
