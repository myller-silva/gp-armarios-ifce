import os
import pathlib
import requests
from flask import Blueprint, session, redirect, request, abort, current_app as app
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

auth_bp = Blueprint("auth", __name__)

# Define ambiente de transporte inseguro para testes
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# Função para criar o fluxo OAuth2 do Google
def create_flow():
    return Flow.from_client_secrets_file(
        client_secrets_file=app.config["CLIENT_SECRETS_FILE"],
        scopes=["https://www.googleapis.com/auth/userinfo.profile",
                "https://www.googleapis.com/auth/userinfo.email", "openid"],
        redirect_uri="http://127.0.0.1:5000/callback"
    )

# Decorador para verificar login
def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        return function(*args, **kwargs)
    return wrapper

# Rota para login
@auth_bp.route("/login")
def login():
    flow = create_flow()
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

# Rota para o callback de autenticação
@auth_bp.route("/callback")
def callback():
    flow = create_flow()
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=app.config["GOOGLE_CLIENT_ID"]
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/user/dashboard")

# Rota para logout
@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")
