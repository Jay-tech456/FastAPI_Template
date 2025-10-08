from typing import Optional
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from .core import User, DBAutomation, NotFoundError

# -----------------------------
# Pydantic Schemas
# -----------------------------
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True

# -----------------------------
# CRUD Helpers
# -----------------------------
def get_all_users(session: Session) -> list[User]:
    """Fetch all users from the database."""
    return session.query(User).all()


def read_user_item(item_id: int, session: Session) -> User:
    """Fetch a single user by ID."""
    db_item = session.query(User).filter(User.id == item_id).first()
    if not db_item:
        raise NotFoundError(f"Item with id {item_id} is not found within the table")
    return db_item


def create_user(user: UserCreate, session: Session) -> User:
    """Create a new user in the database."""
    db_item = User(name=user.name, email=user.email)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


def update_user(item_id: int, user_update: UserUpdate, session: Session) -> User:
    """Update an existing user."""
    db_item = read_user_item(item_id, session)
    
    if user_update.name is not None:
        db_item.name = user_update.name
    if user_update.email is not None:
        db_item.email = user_update.email

    session.commit()
    session.refresh(db_item)
    return db_item


def delete_user(item_id: int, session: Session) -> None:
    """Delete a user from the database."""
    db_item = read_user_item(item_id, session)
    session.delete(db_item)
    session.commit()
