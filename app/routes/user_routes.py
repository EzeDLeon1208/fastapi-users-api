from fastapi import APIRouter
from typing import List
from app.models.user_model import User
from app.services.user_service import (
    get_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user,
)
router = APIRouter()

@router.get("/users",response_model=List[User])
def list_users():
    users = get_users()
    return users

@router.get("/users/{user_id}",response_model=User)
def get_user(user_id: int):
    return get_user_by_id(user_id)

@router.post("/users",response_model=User)
def add_user(user: User):
    return create_user(user)

@router.put("/users/{user_id}",response_model=User)
def edit_user(user_id: int, user: User):
    return update_user(user_id, user)

@router.delete("/users/{user_id}")
def remove_user(user_id: int):
    return delete_user(user_id)