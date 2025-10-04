from pydantic import BaseModel, EmailStr

# Defines data contracts (how data is sent over the network)
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class ClassBase(BaseModel):
    name: str
    subject: str


class Class(ClassBase):
    id: int

    class Config:
        orm_mode = True
