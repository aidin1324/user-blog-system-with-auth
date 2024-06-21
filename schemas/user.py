from pydantic import BaseModel, EmailStr
from typing import Union


class UserBase(BaseModel):
    login: str
    is_active: bool = True
    is_superuser: bool = False
    email: Union[EmailStr, None] = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    id: int
