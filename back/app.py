"""
app.py
Este arquivo é o ponto de entrada da aplicação. Aqui são definidas as rotas e os blueprints.
"""

import os
from flask import Flask, redirect, session
from routes.auth import auth_bp
from routes.main import main_bp
from routes.user import user_bp
# from flask_migrate import Migrate
from models import db

app = Flask("SIGMAR")

# Configurações da aplicação
app.secret_key = os.environ.get("SECRET_KEY")
app.config["GOOGLE_CLIENT_ID"] = os.environ.get("GOOGLE_CLIENT_ID")
app.config["CLIENT_SECRETS_FILE"] = "client_secret.json"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/site.db"  # Caminho para o banco SQLite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Registro dos Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(user_bp, url_prefix="/user")


# Inicialização do banco de dados
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    """
    Rota inicial da aplicação.
    Aqui é feito um redirecionamento para a rota de dashboard do usuário, caso ele esteja logado.
    """
    return redirect("/user/dashboard") if "google_id" in session else redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
