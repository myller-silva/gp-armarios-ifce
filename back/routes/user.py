from flask import Blueprint, session, render_template, redirect, url_for
from routes.auth import login_is_required

# Criação do blueprint para o usuário
user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/dashboard")
@login_is_required
def dashboard():
    user_name = session.get("name", "Usuário")
    user_email = session.get("email")
    user_role = session.get("role")
    user = {
        "name": user_name,
        "email": user_email,
        "role": user_role
    }
    # user = session.get("user")
    return render_template("dashboard.html", user = user)

