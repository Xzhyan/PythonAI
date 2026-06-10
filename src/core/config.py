from pydantic_settings import BaseSettings, SettingsConfigDict
from .constants import BASE_DIR


class Settings(BaseSettings):
    APP_NAME: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / '.env'
    )
