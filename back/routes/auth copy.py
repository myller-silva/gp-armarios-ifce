import os
from flask import Blueprint, redirect, render_template, session, url_for, request, current_app
import google_auth_oauthlib.flow
import json
import requests

auth_bp = Blueprint('auth', __name__, template_folder='templates')

# Esta função inicializa o fluxo OAuth com base nas credenciais armazenadas
def create_oauth_flow():
    # oauth_config = json.loads(current_app.config['GOOGLE_OAUTH_SECRETS'])
    # oauth_config = os.getenv("GOOGLE_OAUTH_SECRETS")
    google_oauth_secrets = os.getenv("GOOGLE_OAUTH_SECRETS")
    if google_oauth_secrets:
        google_oauth_secrets = json.loads(google_oauth_secrets)  # Converte a string JSON em um dicionário
        # app.config['GOOGLE_OAUTH_SECRETS'] = google_oauth_secrets
    oauth_config = google_oauth_secrets
    oauth_flow = google_auth_oauthlib.flow.Flow.from_client_config(
        oauth_config,
        scopes=[
            "https://www.googleapis.com/auth/userinfo.email",
            "openid",
            "https://www.googleapis.com/auth/userinfo.profile",
        ]
    )
    # Desabilitar SSL (apenas para desenvolvimento)
    # session = requests.Session()
    # session.verify = False  # NÃO recomendado para produção!
    
    # # Usar a sessão customizada no fluxo OAuth
    # oauth_flow.session = session  # Atribuir a sessão personalizada ao fluxo OAuth
    return oauth_flow

@auth_bp.route('/signin')
def signin():
    oauth_flow = create_oauth_flow()
    oauth_flow.redirect_uri = url_for('auth.authorize', _external=True)
    authorization_url, state = oauth_flow.authorization_url()
    session['state'] = state
    return redirect(authorization_url)


@auth_bp.route('/authorize')
def authorize():
    if not session['state'] == request.args['state']:
        return 'Invalid state parameter', 400
    
    oauth_flow = create_oauth_flow()
    oauth_flow.fetch_token(authorization_response=request.url)
    session['access_token'] = oauth_flow.credentials.token
    return redirect('/')


@auth_bp.route('/')
def home():
    if "access_token" in session:
        user_info = get_user_info(session["access_token"])
        if user_info:
            return render_template('home.html', user_info=user_info)
    return render_template('home.html')


def get_user_info(access_token):
    response = requests.get("https://www.googleapis.com/oauth2/v3/userinfo", headers={
        "Authorization": f"Bearer {access_token}"
    })
    if response.status_code == 200:
        user_info = response.json()
        return user_info
    else:
        print(f"Failed to fetch user info: {response.status_code} {response.text}")
        return None


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')
