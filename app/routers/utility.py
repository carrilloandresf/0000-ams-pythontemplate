from fastapi import APIRouter, HTTPException

from app.schemas import ExpressionResult, HealthStatus, TextProcessRequest, TextProcessResponse
from app.utils import evaluate_expression, process_text_payload

router = APIRouter(prefix="/api", tags=["Utilidades"])


@router.get("/calculate", response_model=ExpressionResult)
def calculate(expression: str):
    try:
        result = evaluate_expression(expression)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {"expression": expression, "result": result}


@router.post("/process-text", response_model=TextProcessResponse)
def process_text(payload: TextProcessRequest):
    processed = process_text_payload(payload.text)
    return processed


@router.get("/health", response_model=HealthStatus)
def health_check():
    return {"status": "ok"}
