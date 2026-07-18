from pathlib import Path
from dotenv import load_dotenv
import os

# ==========================================
# Localiza a raiz do projeto
# ==========================================
BASE_DIR = Path(__file__).resolve().parents[2]

# Carrega o arquivo .env localizado na raiz
load_dotenv(BASE_DIR / ".env")


class Settings:
    # ==========================================
    # Aplicação
    # ==========================================
    APP_NAME = os.getenv("APP_NAME", "MercadoLivre-AI")
    APP_ENV = os.getenv("APP_ENV", "development")
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

    # ==========================================
    # Banco de Dados
    # ==========================================
    DATABASE_URL = os.getenv("DATABASE_URL", "")

    # ==========================================
    # Mercado Livre OAuth
    # ==========================================
    MELI_CLIENT_ID = os.getenv("MELI_CLIENT_ID", "")
    MELI_CLIENT_SECRET = os.getenv("MELI_CLIENT_SECRET", "")
    MELI_REDIRECT_URI = os.getenv("MELI_REDIRECT_URI", "")

    # ==========================================
    # OpenAI
    # ==========================================
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")


# Instância única das configurações
settings = Settings()