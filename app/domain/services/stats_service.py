from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


class StatsService:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_user_count(self) -> dict:
        result = await self._session.execute(text("CALL get_user_count()"))
        row = result.fetchone()
        count = row[0] if row else 0
        return {"user_count": count}

    async def get_user_stats(self, user_id: int) -> dict:
        result = await self._session.execute(text("CALL get_user_stats(:user_id)"), {"user_id": user_id})
        row = result.fetchone()
        if not row:
            return {"user_id": user_id, "has_user": False}
        # assuming stored procedure returns id, name, email
        return {"user_id": row[0], "name": row[1], "email": row[2], "has_user": True}
