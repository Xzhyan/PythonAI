from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configurações do projeto"""

    APP_NAME: str = "PythonIA"

    # model_config = SettingsConfigDict(
    #     env_file=".env"
    # )


settings = Settings()
