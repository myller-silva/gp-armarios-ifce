"""Módulo com rotas de tratamento de erros"""

from flask import Blueprint, render_template
from werkzeug.exceptions import HTTPException

errors_bp = Blueprint("errors", __name__)

@errors_bp.app_errorhandler(HTTPException)
def handle_http_exception(e):
    """Trata erros HTTP e exibe uma página personalizada"""

    return render_template("error.html", code=e.code, message=e.description), e.code


@errors_bp.app_errorhandler(Exception)
def handle_generic_exception(e):
    """Trata erros genéricos"""
    error_info = {
        "type": type(e).__name__,
        "args": e.args,
        "message": str(e),
        "doc": e.__doc__,
    }
    return render_template("error.html", code=500, message=error_info), 500
