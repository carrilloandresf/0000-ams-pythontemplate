from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    app_name: str = Field("FastAPI SOLID Sample", env="APP_NAME")
    environment: str = Field("development", env="ENVIRONMENT")

    db_user: str = Field("app_user", env="DB_USER")
    db_password: str = Field("app_password", env="DB_PASSWORD")
    db_host: str = Field("db", env="DB_HOST")
    db_port: int = Field(3306, env="DB_PORT")
    db_name: str = Field("app_db", env="DB_NAME")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
