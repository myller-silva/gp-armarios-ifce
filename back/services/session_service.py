from flask import session


class SessionService:
    """Classe de serviço de sessão"""

    @staticmethod
    def get_user():
        """Obtem o usuário da sessão"""
        return session.get("user")

    @staticmethod
    def set_user(user):
        """Define o usuário da sessão"""
        session["user"] = user
