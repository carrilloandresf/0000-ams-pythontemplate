from app.domain.interfaces.user_repository import UserRepository
from app.domain.models.user import User


class UserService:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    async def list_users(self):
        return await self._repository.list()

    async def create_user(self, name: str, email: str) -> User:
        new_user = User(id=None, name=name, email=email)
        return await self._repository.create(new_user)

    async def get_user(self, user_id: int) -> User | None:
        return await self._repository.get(user_id)

    async def update_user(self, user_id: int, name: str, email: str) -> User:
        updated_user = User(id=user_id, name=name, email=email)
        return await self._repository.update(user_id, updated_user)

    async def delete_user(self, user_id: int) -> None:
        await self._repository.delete(user_id)
