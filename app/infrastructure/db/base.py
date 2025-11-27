from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import models to register metadata
from app.infrastructure.db.models.user_model import UserModel  # noqa: E402,F401
