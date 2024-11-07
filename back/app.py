from flask import Flask
import os
from routes.user import user_bp
from routes.auth import auth_bp
# import ssl


app = Flask(__name__)
app.secret_key = "YOUR_SECRET_KEY"  # Defina uma chave secreta para segurança

app.config["GOOGLE_OAUTH_SECRETS"] = os.getenv("GOOGLE_OAUTH_SECRETS")

# Registrando os blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(user_bp, url_prefix="/user")



if __name__ == "__main__":
    # app.run(debug=True)
    # app.run(ssl_context=('cert.pem', 'key.pem'))  # Adiciona o SSL
    app.run(ssl_context=('server.crt', 'server.key'))


