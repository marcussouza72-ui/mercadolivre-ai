from dotenv import load_dotenv
import os

# Carrega automaticamente o arquivo .env
load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "MercadoLivre-AI")
    APP_ENV = os.getenv("APP_ENV", "development")
    DEBUG = os.getenv("DEBUG", "True") == "True"

    DATABASE_URL = os.getenv("DATABASE_URL", "")

    MELI_CLIENT_ID = os.getenv("MELI_CLIENT_ID", "")
    MELI_CLIENT_SECRET = os.getenv("MELI_CLIENT_SECRET", "")
    MELI_REDIRECT_URI = os.getenv("MELI_REDIRECT_URI", "")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")


settings = Settings()