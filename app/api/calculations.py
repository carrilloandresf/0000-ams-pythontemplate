from fastapi import APIRouter, HTTPException, Query

from app.domain.services.calculation_service import CalculationService
from app.schemas.calculation import CalculationResponse

router = APIRouter(prefix="/api", tags=["calculate"])


@router.get("/calculate", response_model=CalculationResponse)
def calculate(expression: str = Query(..., example="5+3")) -> CalculationResponse:
    service = CalculationService()
    try:
        result = service.evaluate(expression)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return CalculationResponse(expression=expression, result=result)
