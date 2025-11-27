from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.services.stats_service import StatsService
from app.domain.services.user_service import UserService
from app.infrastructure.db.session import get_session
from app.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository


def get_db_session(session: AsyncSession = Depends(get_session)) -> AsyncSession:
    return session


def get_user_service(session: AsyncSession = Depends(get_db_session)) -> UserService:
    repository = SqlAlchemyUserRepository(session)
    return UserService(repository)


def get_stats_service(session: AsyncSession = Depends(get_db_session)) -> StatsService:
    return StatsService(session)
