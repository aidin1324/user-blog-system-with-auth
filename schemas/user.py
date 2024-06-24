
from pydantic import BaseModel, EmailStr
from typing import Union
from schemas import BlogPost


class UserBase(BaseModel):
    login: str
    email: Union[EmailStr, None] = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool = True
    is_superuser: bool = False
    blogs: list[BlogPost] = []

    class Config:
        orm_mode = True
