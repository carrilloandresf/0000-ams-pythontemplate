from fastapi import FastAPI

from app.api import calculations, health, stats, text, users
from app.infrastructure.db.session import init_db

app = FastAPI(title="FastAPI SOLID Template")

app.include_router(health.router)
app.include_router(calculations.router)
app.include_router(text.router)
app.include_router(users.router)
app.include_router(stats.router)


@app.on_event("startup")
async def on_startup():
    await init_db()
