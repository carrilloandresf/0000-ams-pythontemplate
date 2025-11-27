from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=100)
    email: EmailStr | None = None


class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True


class UserCount(BaseModel):
    total_users: int


class ExpressionResult(BaseModel):
    expression: str
    result: float


class TextProcessRequest(BaseModel):
    text: str = Field(..., min_length=1)


class TextProcessResponse(BaseModel):
    original: str
    uppercase: str
    word_count: int


class HealthStatus(BaseModel):
    status: str
