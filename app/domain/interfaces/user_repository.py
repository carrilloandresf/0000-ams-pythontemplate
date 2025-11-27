from abc import ABC, abstractmethod
from typing import Iterable

from app.domain.models.user import User


class UserRepository(ABC):
    @abstractmethod
    async def list(self) -> Iterable[User]:
        raise NotImplementedError

    @abstractmethod
    async def create(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    async def get(self, user_id: int) -> User | None:
        raise NotImplementedError

    @abstractmethod
    async def update(self, user_id: int, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, user_id: int) -> None:
        raise NotImplementedError
