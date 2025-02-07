"""Módulo de serviço de sessão."""
from flask import session
from models import User

class SessionService:
    """Classe de serviço de sessão"""

    @staticmethod
    def get_user():
        """Obtem o usuário da sessão"""
        return session.get("user")

    @staticmethod
    def set_user(user: User):
        """Define o usuário da sessão."""
        session["user"] = user.to_dict()

    @staticmethod
    def clear():
        """Limpa a sessão."""
        session.clear()
        