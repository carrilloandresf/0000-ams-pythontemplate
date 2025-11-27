from fastapi import APIRouter

from app.domain.services.text_service import TextService
from app.schemas.text import TextRequest, TextResponse

router = APIRouter(prefix="/api", tags=["text"])


@router.post("/process-text", response_model=TextResponse)
async def process_text(payload: TextRequest) -> TextResponse:
    service = TextService()
    result = service.process(payload.text)
    return TextResponse(**result)
