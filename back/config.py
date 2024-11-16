"""Configurações do projeto."""

import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()


class Config:
    """Configurações do projeto."""

    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "minhasenhaultrasecreta")
    JWT_SECRET_KEY = SECRET_KEY
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    GOOGLE_DISCOVERY_URL = (
        "https://accounts.google.com/.well-known/openid-configuration"
    )
