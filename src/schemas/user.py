from pydantic import BaseModel, Field

from src.utils.roles import RoleEnum


class UserUpdateSchema(BaseModel):
    username: str = Field(max_length=128)
    text_password: str = Field(min_length=8, max_length=64)

    
class UserCreateSchema(UserUpdateSchema):
    role: RoleEnum


class UserResponseSchema(BaseModel):
    id: int
    username: str
    role: RoleEnum
