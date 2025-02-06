"""Módulo para manipulação de usuários."""

from repositories.user_repository import UserRepository


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
