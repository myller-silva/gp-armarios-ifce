"""Módulo para manipulação de usuários no banco de dados."""

from models import db, User


class UserRepository:
    """Classe para manipulação de usuários no banco de dados."""

    @staticmethod
    def get_all():
        """Retorna todos os usuários."""
        return User.query.all()

    @staticmethod
    def get_by_email(email):
        """Retorna um usuário pelo e-mail."""
        return User.query.filter(User.email == email).first()

    @staticmethod
    def get_by_id(user_id):
        """Retorna um usuário pelo ID."""
        return User.query.get(user_id)

    @staticmethod
    def create_user(name, email):
        """Cria um novo usuário."""
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        """Deleta um usuário."""
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            
    @staticmethod
    def update_user(user_id, name, email):
        """Atualiza um usuário."""
        user = User.query.get(user_id)
        if user:
            user.name = name
            user.email = email
            db.session.commit()
            return user
        return None
    
    @staticmethod
    def get_users_filtered(data):
        """Retorna usuários filtrados."""
        query = User.query
        if data.get("email"):
            query = query.filter(User.email.ilike(f"%{data['email']}%"))
        if data.get("role"):
            query = query.filter(User.role == data['role'])
        return query.all()
