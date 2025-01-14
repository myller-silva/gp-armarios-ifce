from flask import Blueprint, session, render_template, redirect, url_for
from decorators import login_is_required

# Criação do blueprint para o usuário
user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/dashboard")
@login_is_required
def dashboard():
    """Função para renderizar o dashboard do usuário"""
    user = session.get("user")
    return render_template("dashboard.html", user = user)

@user_bp.route("/perfil")
@login_is_required
def perfil():
    """Função para renderizar o perfil do usuário"""
    user = session.get("user")
    return render_template("perfil.html", user = user)