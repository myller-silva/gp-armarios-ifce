"""Módulo com rotas para autenticação com o Google."""

import os
import requests
from flask import Blueprint, session, redirect, request, abort, current_app as app
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
from services.user_service import UserService
from services.session_service import SessionService

auth_bp = Blueprint("auth", __name__)

# Define ambiente de transporte inseguro para testes
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


def create_flow():
    """Cria um fluxo OAuth2 para autenticação com o Google."""
    return Flow.from_client_secrets_file(
        client_secrets_file=app.config["CLIENT_SECRETS_FILE"],
        scopes=[
            "https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email",
            "openid",
        ],
        redirect_uri="http://127.0.0.1:5000/callback",
    )


@auth_bp.route("/login")
def login():
    """Rota para iniciar o processo de autenticação."""
    flow = create_flow()
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@auth_bp.route("/callback")
def callback():
    """Rota para o callback de autenticação."""
    flow = create_flow()
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=app.config["GOOGLE_CLIENT_ID"],
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
