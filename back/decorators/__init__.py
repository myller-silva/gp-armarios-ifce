"""Módulo com decorators"""

from functools import wraps
from flask import redirect, url_for, session


def role_required(role):
    """Decorator para verificar se o usuário possui a role necessária para acessar a rota"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = session.get('user')
            user_role = user.get('role') if user else None
            if user_role != role:
                return redirect(url_for('main.unauthorized'))  # Redireciona para uma página de acesso não autorizado
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def login_is_required(function):
    """Decorator para verificar se o usuário está logado"""
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect("/login")
        return function(*args, **kwargs)
    return decorated_function

