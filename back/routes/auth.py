"""Módulo para autenticação de usuários com Google OAuth2."""
import os
from flask import Blueprint, session, redirect, request, current_app as app, url_for
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
import google.auth.transport.requests
from services.user_service import UserService
from services.session_service import SessionService

auth_bp = Blueprint("auth", __name__)

# Define ambiente de transporte inseguro para testes
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


def create_flow():
    """Cria um fluxo OAuth com as configurações necessárias."""
    return Flow.from_client_secrets_file(
        client_secrets_file=app.config["CLIENT_SECRETS_FILE"],
        scopes=[
            "https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email",
            "openid",
        ],
    )


@auth_bp.route("/login")
def login():
    """Rota para iniciar o processo de autenticação."""
    flow = create_flow()
    flow.redirect_uri = url_for("auth.callback", _external=True)
    authorization_url, state = flow.authorization_url(
        access_type="offline",  # necessário para obter um refresh token
        include_granted_scopes="true",
    )
    session["state"] = state
    return redirect(authorization_url)


@auth_bp.route("/callback")
def callback():
    """Rota para o callback de autenticação."""
    # Verifica o estado para prevenir CSRF
    if not session.get("state") == request.args.get("state"):
        return "Invalid state parameter", 400

    flow = create_flow()
    flow.redirect_uri = url_for("auth.callback", _external=True)
    flow.fetch_token(authorization_response=request.url)
    credentials = flow.credentials
    session["credentials"] = {
        "token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
        "granted_scopes": credentials.scopes,
    }
    token_request = google.auth.transport.requests.Request()
    id_info = id_token.verify_oauth2_token(
        credentials.id_token, token_request, audience=app.config["GOOGLE_CLIENT_ID"]
    )
    session["google_id"] = id_info.get("sub")
    user = UserService.login(username=id_info.get("name"), email=id_info.get("email"))
    SessionService.set_user(user)
    return redirect("/user/dashboard")


@auth_bp.route("/logout")
def logout():
    """Rota para encerrar a sessão do usuário."""
    SessionService.clear()
    return redirect("/")
