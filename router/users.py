from fastapi import APIRouter, HTTPException
from fastapi.params import Depends 
from sqlalchemy.orm import Session
from db.core import get_db, NotFoundError



router = APIRouter( 
    prefix= "/users",
)



@router.post("")
def create_users(): 
    return { "message": "This is the create user function"}


@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return { 
        "Message": "This is the get user"
    }


@router.put("/{user_id}")
def update_users(user_id: int, db: Session = Depends(get_db)): 
    """ This takes in a Path parameter of a user id"""
    return { 
        "message": "This is the update router for the user"
    }


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)): 
    """ This is the delete method using the user id"""
    return { 
        "message": "This is the delete router for the user"
    }