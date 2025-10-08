

# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from database import engine 
# import models 
# import schemas
# from database import get_db

from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
from router.users import router as items_router
# from routers.automations import router as automations_router
# from routers.limiter import limiter
# from slowapi import _rate_limit_exceeded_handler
# from slowapi.errors import RateLimitExceeded


# Helps to create the database tables --> Make sure the correspongding tables exist in the DB
# models.Base.metadata.create_all(bind=engine)

test_router = APIRouter()

app = FastAPI(title="Interview Prep API")



# Bastic Routes 
@app.get("/")
def get(): 
    return { 
        "message": "Hello world", 
    }

