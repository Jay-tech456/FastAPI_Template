from typing import Optional
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
import os
from dotenv import load_dotenv

load_dotenv() 
DATABASE_URL = os.getenv("DATABASE_URL") or ""


class NotFoundError(Exception):
    pass


class Base(DeclarativeBase):
    pass


class DBItem(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]


class DBAutomation(Base):
    __tablename__ = "automations"

    id: Mapped[int] = mapped_column(primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"))
    code: Mapped[str]




engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Gives you a database session per request (like a handle into postgres)

Base = declarative_base()  # Special SLQAlchemy class that helps to create models

# Dependency to get the data base session and close it successfully
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
