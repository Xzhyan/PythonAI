from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


# Caminho absoluto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Diretorio de arquvos JSON
JSON_DIR = BASE_DIR / 'json'


class Settings(BaseSettings):
    """Configurações do projeto"""

    APP_NAME: str = "PythonIA"

    # model_config = SettingsConfigDict(
    #     env_file=".env"
    # )


settings = Settings()
