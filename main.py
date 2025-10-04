

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine 
import models 
import schemas
from database import get_db


# Helps to create the database tables --> Make sure the correspongding tables exist in the DB
models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Interview Prep API")
get_db()



# Bastic Routes 
@app.get("/")
def get(): 
    return { 
        "message": "Hello world", 
    }
@app.post("/")
def post(): 
    return { 
        "message": "Hello, this is the post command"
    }
@app.put("/")
def put(): 
    return { 
        "message": "Hello this is the put command"
    }

@app.delete("/")
def delete(): 
    return { 
        "message": "Hello this is the delete command"
    }


# Using internal routes to create and read users 
# Second parameter of the functions is how the model responds using the response_model
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_users(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=204, detail="User not found")
    db.delete(db_user)
    db.commit()
    return db_user


# Get All the users 
@app.get("/users/", response_model=list[schemas.User])
def get_all_users(db: Session = Depends(get_db)): 
    user = db.query(models.User).all()
    return user



# More Routes to handle all the other classes
@app.post("/classes/", response_model=schemas.Class)
def create_class(cls: schemas.ClassBase, db: Session = Depends(get_db)):
    db_class = models.Class(name=cls.name, subject=cls.subject)
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class