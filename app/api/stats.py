from fastapi import APIRouter, Depends

from app.api.deps import get_stats_service
from app.domain.services.stats_service import StatsService

router = APIRouter(prefix="/api/stats", tags=["stats"])


@router.get("/user-count")
async def user_count(service: StatsService = Depends(get_stats_service)):
    return await service.get_user_count()


@router.get("/user-stats/{user_id}")
async def user_stats(user_id: int, service: StatsService = Depends(get_stats_service)):
    return await service.get_user_stats(user_id)
