"""Módulo com o Padrão GoF Façade para configurar o aplicativo Flask e inicializar os plugins"""

import os
from flask import Flask
from flask_migrate import Migrate
from models import db
from routes.auth import auth_bp
from routes.main import main_bp
from routes.user import user_bp
from routes.admin import admin_bp
from routes.student import student_bp
from routes.errors import errors_bp
from routes.files import files_bp


class AppFacade:
    """Classe Façade para configurar o aplicativo Flask e inicializar os plugins"""

    def __init__(self):
        self.app = Flask("SIGMAR")
        self.migrate = Migrate()

    def configure_app(self):
        """Configura as variáveis de ambiente da aplicação"""
        self.app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "DATABASE_URL", "sqlite:///sigmar.db"
        )
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.app.secret_key = os.environ.get("SECRET_KEY")
        self.app.config["GOOGLE_CLIENT_ID"] = os.environ.get("GOOGLE_CLIENT_ID")
        self.app.config["CLIENT_SECRETS_FILE"] = "client_secret.json"

    def initialize_plugins(self):
        """Inicializa os plugins do Flask"""
        db.init_app(self.app)
        self.migrate.init_app(self.app, db)

    def register_blueprints(self):
        """Registra todos os Blueprints"""
        self.app.register_blueprint(auth_bp)
        self.app.register_blueprint(main_bp)
        self.app.register_blueprint(errors_bp)
        self.app.register_blueprint(user_bp, url_prefix="/user")
        self.app.register_blueprint(admin_bp, url_prefix="/admin")
        self.app.register_blueprint(student_bp, url_prefix="/student")
        self.app.register_blueprint(files_bp, url_prefix="/files")

    def create_app(self):
        """Cria e retorna o aplicativo Flask"""
        self.configure_app()
        self.initialize_plugins()
        self.register_blueprints()

        # Garantir que as tabelas do banco sejam criadas
        with self.app.app_context():
            db.create_all()

        return self.app
