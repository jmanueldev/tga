from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = (
        "postgresql+psycopg://tga:tga@localhost:5432/tga"
    )

    redis_url: str = "redis://localhost:6379"

    class Config:
        env_file = ".env"


settings = Settings()