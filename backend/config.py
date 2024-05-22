from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
    schema_config = SettingsConfigDict(
        env_prefix="POSTGRES_",
        case_sensitive=False,
    )

    host: str
    port: int
    user: str
    password: str
    db: str

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


database_config = DatabaseConfig()
