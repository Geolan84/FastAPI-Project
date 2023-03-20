from typing import Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    name: str

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    email: str
    name: str
    surname: str
    patronymic: str
    is_hr: bool


# class UserUpdate(schemas.BaseUserUpdate):
#     pass