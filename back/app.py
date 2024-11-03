from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from models import db, User
from flask_cors import CORS
from config import Config
# from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
jwt = JWTManager(app)


# Configurando CORS
CORS(app)  # Permite que qualquer origem acesse seu aplicativo

with app.app_context():
    db.create_all()


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password=data['password'])  # Adicione hash para senha aqui
    
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        return jsonify({"msg": f"Error to register user: {new_user.username}", "error": str(e)}), 500
    
    access_token = create_access_token(identity=new_user.id, additional_claims={"username": new_user.username, "email": new_user.email})
    
    return jsonify({"token": access_token}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    # if user and check_password_hash(user.password, data['password']):  # Verifica a senha com hash
    if user and user.password == data['password']:
        access_token = create_access_token(identity=user.id, additional_claims={"username": user.username, "email": user.email})
        
        refresh_token = create_refresh_token(identity=user.id)  # Cria um refresh token
        return jsonify({"token": access_token, "refresh_token": refresh_token}), 200
    
    return jsonify({"msg": "Bad username or password"}), 401


@app.route('/user', methods=['GET'])
@jwt_required()
def get_user_info():
    current_user_id = get_jwt_identity()  # Pega o ID do usuário do token
    print("current_user_id: ", current_user_id)
    user = User.query.get(current_user_id)  # Busca o usuário pelo ID
    if user:
        return jsonify(username=user.username, email=user.email), 200
    return jsonify({"msg": "User not found"}), 404


@app.route('/token/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user_id = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user_id)
    return jsonify(access_token=new_access_token), 200
