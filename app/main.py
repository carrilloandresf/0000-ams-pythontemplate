from dotenv import load_dotenv
from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.routers import users, utility

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API REST Plantilla",
    version="1.0.0",
    description="API REST sencilla con FastAPI, MySQL y Docker.",
)

app.include_router(utility.router)
app.include_router(users.router)
