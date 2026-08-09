from pydantic_settings import BaseSettings, SettingsConfigDict

# constants
from .constants import ENV_FILE

class Settings(BaseSettings):
    PROJECT_NAME: str
    AUTHOR: str
    TEAM: str
    VERSION: str

    model_config = SettingsConfigDict(
        env_file=ENV_FILE
    )

settings = Settings
