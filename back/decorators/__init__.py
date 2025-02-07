"""Módulo com decorators"""

from functools import wraps
from flask import redirect, url_for, session
from flask import request, render_template
from werkzeug.exceptions import HTTPException

def role_required(role):
    """Decorator para verificar se o usuário possui a role necessária para acessar a rota"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = session.get('user')
            user_role = user.get('role') if user else None
            if user_role != role:
                return redirect(url_for('main.unauthorized'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def login_is_required(function):
    """Decorator para verificar se o usuário está logado antes de acessar a rota"""
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect("/login")
        return function(*args, **kwargs)
    return decorated_function

def error_handler(f):
    """Decorator para capturar exceções e exibir uma página de erro"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except HTTPException as http_exc:  # Captura exceções HTTP
            status_code = http_exc.code
            error_message = http_exc.description
            print(f"Erro HTTP na rota {request.path}: {error_message} (Código: {status_code})")
            return render_template("error.html", code=status_code, message=error_message), status_code
        except Exception as e:  # Captura outros erros genéricos
            status_code = 500  # Erro interno do servidor
            error_message = str(e)
            print(f"Erro genérico na rota {request.path}: {error_message}")
            return render_template("error.html", code=status_code, message=error_message), status_code
    return decorated_function
