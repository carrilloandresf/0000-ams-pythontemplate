from typing import Iterable

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.interfaces.user_repository import UserRepository
from app.domain.models.user import User
from app.infrastructure.db.models.user_model import UserModel


class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def list(self) -> Iterable[User]:
        result = await self._session.execute(select(UserModel))
        return [self._map_to_domain(row[0]) for row in result.all()]

    async def create(self, user: User) -> User:
        instance = UserModel(name=user.name, email=user.email)
        self._session.add(instance)
        try:
            await self._session.commit()
        except IntegrityError as exc:
            await self._session.rollback()
            raise ValueError("Email already exists") from exc
        await self._session.refresh(instance)
        return self._map_to_domain(instance)

    async def get(self, user_id: int) -> User | None:
        result = await self._session.execute(select(UserModel).where(UserModel.id == user_id))
        user_model = result.scalar_one_or_none()
        return self._map_to_domain(user_model) if user_model else None

    async def update(self, user_id: int, user: User) -> User:
        result = await self._session.execute(select(UserModel).where(UserModel.id == user_id))
        user_model = result.scalar_one_or_none()
        if not user_model:
            raise ValueError("User not found")
        user_model.name = user.name
        user_model.email = user.email
        try:
            await self._session.commit()
        except IntegrityError as exc:
            await self._session.rollback()
            raise ValueError("Email already exists") from exc
        await self._session.refresh(user_model)
        return self._map_to_domain(user_model)

    async def delete(self, user_id: int) -> None:
        result = await self._session.execute(select(UserModel).where(UserModel.id == user_id))
        user_model = result.scalar_one_or_none()
        if not user_model:
            raise ValueError("User not found")
        await self._session.delete(user_model)
        await self._session.commit()

    @staticmethod
    def _map_to_domain(model: UserModel) -> User:
        return User(id=model.id, name=model.name, email=model.email)
