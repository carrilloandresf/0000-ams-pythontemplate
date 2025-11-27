from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(..., example="Ada Lovelace")
    email: EmailStr = Field(..., example="ada@example.com")


class UserUpdate(BaseModel):
    name: str = Field(..., example="Ada Lovelace")
    email: EmailStr = Field(..., example="ada@example.com")


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
