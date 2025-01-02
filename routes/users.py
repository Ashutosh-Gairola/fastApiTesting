from fastapi import APIRouter, HTTPException
from models import User

router = APIRouter()

# Sample data for users
users = [{"id": 1, "username": "john_doe", "email": "john@example.com"}]

@router.get("/users", tags=["Users"])
def get_users():
    """Retrieve all users."""
    return users

@router.post("/users", tags=["Users"])
def create_user(user: User):
    """Create a new user."""
    if any(existing_user["id"] == user.id for existing_user in users):
        raise HTTPException(status_code=400, detail="User with this ID already exists")
    users.append(user.dict())
    return {"message": "User created successfully", "user": user}

@router.put("/users/{user_id}", tags=["Users"])
def update_user(user_id: int, user: User):
    """Update an existing user."""
    for existing_user in users:
        if existing_user["id"] == user_id:
            existing_user.update(user.dict())
            return {"message": "User updated successfully", "user": existing_user}
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{user_id}", tags=["Users"])
def delete_user(user_id: int):
    """Delete a user."""
    for existing_user in users:
        if existing_user["id"] == user_id:
            users.remove(existing_user)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
