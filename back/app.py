import os
from flask import Flask, redirect, session
from routes.auth import auth_bp
from routes.main import main_bp
from routes.user import user_bp

app = Flask("SIGMAR")


app.secret_key = os.environ.get("SECRET_KEY")
app.config["GOOGLE_CLIENT_ID"] = os.environ.get("GOOGLE_CLIENT_ID")
app.config["CLIENT_SECRETS_FILE"] = "client_secret.json"

# Registro dos Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(user_bp, url_prefix="/user")


@app.route("/")
def index():
    return redirect("/user/dashboard") if "google_id" in session else redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
