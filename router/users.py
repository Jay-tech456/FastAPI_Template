from fastapi import APIRouter, HTTPException, Request
from fastapi.params import Depends
from sqlalchemy.orm import Session
from db.core import get_db, NotFoundError
from .limiter import limiter

from db.user import (
    UserOut,
    UserCreate,
    UserUpdate,
    read_user_item,
    get_all_users,
    create_user,
    update_user,
    delete_user
)

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# -----------------------------
# CREATE USER
# -----------------------------
@router.post("", response_model=UserOut)
# @limiter.limit("1/second")
def create_users(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = create_user(user, db)
        return db_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# -----------------------------
# READ USER BY ID
# -----------------------------
@router.get("/{user_id}", response_model=UserOut)
# @limiter.limit("1/second")
def read_user(user_id: int, db: Session = Depends(get_db)):
    try:
        db_user = read_user_item(user_id, db)
        return db_user
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


# -----------------------------
# GET ALL USERS
# -----------------------------
@router.get("", response_model=list[UserOut])
# @limiter.limit("1/second")
def read_users(db: Session = Depends(get_db)):
    users = get_all_users(db)
    return users


# -----------------------------
# UPDATE USER
# -----------------------------
@router.put("/{user_id}", response_model=UserOut)
# @limiter.limit("1/second")
def update_users(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    try:
        updated_user = update_user(user_id, user_update, db)
        return updated_user
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


# -----------------------------
# DELETE USER
# -----------------------------
@router.delete("/{user_id}")
# @limiter.limit("1/second")
def delete_users(user_id: int, db: Session = Depends(get_db)):
    try:
        delete_user(user_id, db)
        return {"message": f"User with id {user_id} has been deleted"}
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
