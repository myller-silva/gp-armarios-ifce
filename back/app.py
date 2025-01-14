"""
app.py
Este arquivo é o ponto de entrada da aplicação. Aqui são definidas as rotas e os blueprints.
"""

import os
from flask import Flask, redirect, session
from routes.auth import auth_bp
from routes.main import main_bp
from routes.user import user_bp
from routes.admin import admin_bp
from routes.student import student_bp
from flask_migrate import Migrate
# from data_initializer import initialize_data


from models import db


migrate = Migrate()

def create_app():
    app = Flask("SIGMAR")
    
    # Configurações da aplicação
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sigmar.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = os.environ.get("SECRET_KEY")
    app.config["GOOGLE_CLIENT_ID"] = os.environ.get("GOOGLE_CLIENT_ID")
    app.config["CLIENT_SECRETS_FILE"] = "client_secret.json"
    
    # Inicialização dos plugins
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Registro dos Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(student_bp, url_prefix="/student")
    
    return app

app = create_app()


@app.route("/")
def index():
    """
    Rota inicial da aplicação. 
    Aqui é feito um redirecionamento para a rota de dashboard do usuário, caso ele esteja logado.
    """
    return redirect("/user/dashboard") if "google_id" in session else redirect("/login")


@app.route("/home")
def home():
    """
    Rota inicial da aplicação. 
    Aqui é feito um redirecionamento para a rota de dashboard do usuário, caso ele esteja logado.
    """
    return redirect("/user/dashboard") if "google_id" in session else redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
