from pydantic import BaseModel, Field


class TextRequest(BaseModel):
    text: str = Field(..., example="hello world")


class TextResponse(BaseModel):
    original: str
    uppercase: str
    word_count: int
    frequency: dict[str, int]
