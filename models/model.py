from typing import List

from pydantic import BaseModel


class UserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str


class UpdateUserResponse(BaseModel):
    name: str
    job: str
    updatedAt: str


class RegisterResponse(BaseModel):
    id: int
    token: str


class ErrorResponse(BaseModel):
    error: str


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class Support(BaseModel):
    url: str
    text: str


class UsersResponse(BaseModel):
    data: List[User]
    support: Support
