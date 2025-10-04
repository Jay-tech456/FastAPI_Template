from sqlalchemy import Column, Integer, String
from database import Base


# Defines the actual tables structure in the databases
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)



class Class(Base): 
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index = True)
    subject = Column(String, index= True)
