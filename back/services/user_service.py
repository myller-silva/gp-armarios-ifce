"""Módulo para manipulação de usuários."""

from repositories.user_repository import UserRepository
from services.request_service import RequestService
from services.session_service import SessionService


class UserService:
    """Classe para manipulação de usuários."""

    @staticmethod
    def get_all_users():
        """Retorna todos os usuários."""
        return UserRepository.get_all()

    @staticmethod
    def get_user_by_id(user_id):
        """Retorna um usuário pelo ID."""
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    @staticmethod
    def get_user_by_email(email):
        """Retorna um usuário pelo e-mail."""
        return UserRepository.get_by_email(email)

    @staticmethod
    def create_user(name: str, email: str, role: str):
        """Cria um novo usuário."""
        if "@" not in email:
            raise ValueError("Invalid email format")
        user = UserRepository.create_user(name=name, email=email, role=role)
        return user

    @staticmethod
    def create_admin(name: str, email: str):
        """Cria um novo usuário administrador."""
        return UserService.create_user(name=name, email=email, role="admin")

    @staticmethod
    def create_student(name: str, email: str):
        """Cria um novo usuário aluno."""
        return UserService.create_user(name=name, email=email, role="aluno")

    @staticmethod
    def create_student_if_not_exists(name: str, email: str):
        """Cria um novo usuário aluno se não existir."""
        user = UserRepository.get_by_email(email)
        if not user:
            user = UserService.create_student(name, email)
        return user

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

    @staticmethod
    def get_user_requests():
        """Retorna as solicitações de um usuário."""
        user = SessionService.get_user()
        user_id = user["id"]
        return RequestService.get_requests_filtered({"user_id": user_id})

    @staticmethod
    def has_any_user():
        """Verifica se existe algum usuário no banco de dados."""
        return UserRepository.has_any_user()

    @staticmethod
    def login(username: str, email: str):
        """Realiza o login de um usuário.
        Se for o primeiro usuário, ele é criado como administrador.
        Se o usuário não existir, ele é criado como aluno.
        """
        if not UserService.has_any_user():
            return UserService.create_admin(name=username, email=email)
        user = UserService.get_user_by_email(email)
        if not user:
            return UserService.create_student(name=username, email=email)
        return user
