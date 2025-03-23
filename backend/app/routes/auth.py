from flask import Blueprint, request, jsonify
from app.controllers.auth_controller import autenticar_usuario

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    senha = data.get("senha")

    if not username or not senha:
        return jsonify({"erro": "Username e senha são obrigatórios"}), 400

    resultado = autenticar_usuario(username, senha)

    if resultado:
        return jsonify({"mensagem": "Login bem-sucedido", "usuario": resultado}), 200
    else:
        return jsonify({"erro": "Credenciais inválidas"}), 401
