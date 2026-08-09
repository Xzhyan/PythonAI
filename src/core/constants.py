from pathlib import Path

# caminho absoluto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# pasta de logs
LOG_DIR = BASE_DIR / 'logs'

# pasta de banco de dados
DB_DIR = BASE_DIR / ''

# arquivo .env de configuração
ENV_FILE = BASE_DIR / '.env'



