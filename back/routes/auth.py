import os
from flask import Blueprint, session, request, jsonify, redirect, url_for, render_template
import google_auth_oauthlib.flow
import json
import requests

auth_bp = Blueprint('auth', __name__, template_folder='templates')

def create_oauth_flow():
    google_oauth_secrets = os.getenv("GOOGLE_OAUTH_SECRETS")
    if google_oauth_secrets:
        google_oauth_secrets = json.loads(google_oauth_secrets)
    oauth_flow = google_auth_oauthlib.flow.Flow.from_client_config(
        google_oauth_secrets,
        scopes=[
            "https://www.googleapis.com/auth/userinfo.email",
            "openid",
            "https://www.googleapis.com/auth/userinfo.profile",
        ]
    )
    return oauth_flow


@auth_bp.route('/signin')
def signin():
    oauth_flow = create_oauth_flow()
    authorization_url, state = oauth_flow.authorization_url(prompt='consent')
    session['state'] = state
    return jsonify({
        "authorization_url": authorization_url
    })

@auth_bp.route('/token', methods=['POST'])
def get_token():
    code = request.json.get('code')  # O código de autorização enviado pelo cliente
    if not code:
        return jsonify({'error': 'Authorization code missing'}), 400

    oauth_flow = create_oauth_flow()
    oauth_flow.fetch_token(
        token_url="https://oauth2.googleapis.com/token",
        authorization_response=f'https://localhost:5000?code={code}',
        client_secret=os.getenv("GOOGLE_OAUTH_SECRETS_SECRET")
    )
    
    session['access_token'] = oauth_flow.credentials.token
    user_info = get_user_info(session['access_token'])
    return jsonify(user_info)

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
        return response.json()
    else:
        print(f"Failed to fetch user info: {response.status_code} {response.text}")
        return None


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')
