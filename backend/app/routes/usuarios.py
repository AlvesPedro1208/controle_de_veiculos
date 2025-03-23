from flask import Blueprint, request, jsonify
from app.controllers.usuario_controller import cadastrar_usuario, listar_usuarios

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/", methods=["POST"])
def rota_cadastrar_usuario():
    data = request.get_json()
    response = cadastrar_usuario(data)
    return jsonify(response)

@usuarios_bp.route("/", methods=["GET"])
def rota_listar_usuarios():
    response = listar_usuarios()
    return jsonify(response)
