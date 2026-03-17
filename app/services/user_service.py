from app.models.user_model import User
from fastapi import HTTPException

fake_db = []

# GET ALL
def get_users():
    return fake_db

# GET BY ID
def get_user_by_id(user_id: int):
    for user in fake_db:
        if user.id == user_id:
            return user
        raise HTTPException(status_code=404, detail="User not found")

# CREATE
def create_user(user: User):
    # Validacion para evitar duplicados
    for existing_user in fake_db:
        if existing_user.id == user.id:
            raise HTTPException(status_code=404, detail="User not found")

    fake_db.append(user)
    return user

# UPDATE
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(fake_db):
        if user.id == user_id:
            fake_db[index] = updated_user
            return updated_user

    raise HTTPException(status_code=404, detail="User not found")

# DELETE
def delete_user(user_id: int):
    for index, user in enumerate(fake_db):
        if user.id == user_id:
            deleted_user = fake_db.pop(index)
            return deleted_user

    raise HTTPException(status_code=404, detail="User not found")