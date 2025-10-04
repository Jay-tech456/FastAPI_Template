from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Creates a SQLAlchemy engine and session --> Connections to Postgres
load_dotenv()  # load environment variables

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Gives you a database session per request (like a handle into postgres)

Base = declarative_base()  # Special SLQAlchemy class that helps to create models

# Safely opens/ closes session per each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
