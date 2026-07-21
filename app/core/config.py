from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

# ==========================================================
# Diretório base do projeto
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / ".env")


class Settings(BaseSettings):
    """
    Configurações globais da aplicação.

    Todas as configurações são carregadas automaticamente
    a partir do arquivo .env.
    """

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore",
    )

    # ======================================================
    # Aplicação
    # ======================================================

    APP_NAME: str = "MercadoLivre AI"

    APP_ENV: str = "development"

    DEBUG: bool = True

    # ======================================================
    # Banco de Dados
    # ======================================================

    DATABASE_URL: str

    # ======================================================
    # JWT
    # ======================================================

    SECRET_KEY: str

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    # ======================================================
    # Mercado Livre
    # ======================================================

    MELI_CLIENT_ID: str

    MELI_CLIENT_SECRET: str

    MELI_REDIRECT_URI: str

    MELI_API_URL: str = "https://api.mercadolibre.com"

    MELI_AUTH_URL: str = "https://auth.mercadolivre.com.br"

    MELI_REQUEST_TIMEOUT: int = 30

    # ======================================================
    # OpenAI
    # ======================================================

    OPENAI_API_KEY: str = ""


settings = Settings()