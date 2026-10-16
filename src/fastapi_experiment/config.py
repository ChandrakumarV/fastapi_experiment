from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_url: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # class Config:
    #     env_file = ".env"
    #     env_file = ".env.development"


settings = Settings()

print(settings.model_dump())
