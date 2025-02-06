"""Módulo para manipulação de usuários."""

from repositories.user_repository import UserRepository
from services.request_service import RequestService
from services.session_service import SessionService


class UserService:
    """Classe para manipulação de usuários."""

    @staticmethod
    def get_all_users():
        """Retorna todos os usuários."""
        # Possibilidade de adicionar lógica adicional (exemplo: filtragens)
        return UserRepository.get_all()

    @staticmethod
    def get_user_by_id(user_id):
        """Retorna um usuário pelo ID."""
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    @staticmethod
    def create_user(name, email):
        """Cria um novo usuário."""
        # Exemplo de regra de negócio adicional
        if "@" not in email:
            raise ValueError("Invalid email format")
        return UserRepository.create_user(name, email)

    # filtro de usuários
    @staticmethod
    def get_users_filtered(data):
        """Retorna usuários filtrados."""
        return UserRepository.get_users_filtered(data)

    @staticmethod
    def delete_user(user_id):
        """Deleta um usuário."""
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return UserRepository.delete_user(user_id)

    @staticmethod
    def update_user(user_id, name, email):
        """Atualiza um usuário."""
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return UserRepository.update_user(user_id, name, email)

    # @staticmethod
    # def get_user_requests(user_id):
    #     """Retorna as solicitações de um usuário."""
    #     return RequestService.get_requests_filtered({"user_id": user_id})
    
    @staticmethod
    def get_user_requests():
        """Retorna as solicitações de um usuário."""
        user = SessionService.get_user()
        user_id = user["id"]
        return RequestService.get_requests_filtered({"user_id": user_id})
    
