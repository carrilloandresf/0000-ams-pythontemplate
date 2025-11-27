from pydantic import BaseModel, Field


class CalculationResponse(BaseModel):
    expression: str = Field(..., example="5+3")
    result: float
