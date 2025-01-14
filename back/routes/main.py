from flask import Blueprint,  render_template

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    """Rota para a página inicial"""
    return render_template("index.html")

@main_bp.route("/unauthorized")
def unauthorized():
    """Rota para a página de acesso não autorizado"""
    return render_template("unauthorized.html")