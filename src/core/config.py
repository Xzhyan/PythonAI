from pydantic_settings import BaseSettings, SettingsConfigDict

# constants
from .constants import ENV_FILE


class Settings(BaseSettings):
    APP_NAME: str
    AUTHOR: str
    VERSION: str

    model_config = SettingsConfigDict(
        env_file=ENV_FILE
    )


settings = Settings()
