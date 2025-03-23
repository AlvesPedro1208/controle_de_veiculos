from flask import Blueprint, request, jsonify
from app.controllers.veiculo_controller import cadastrar_veiculo, listar_veiculos, alterar_status_veiculo

veiculos_bp = Blueprint("veiculos", __name__)

@veiculos_bp.route("/", methods=["POST"])
def rota_cadastrar_veiculo():
    data = request.get_json()
    response = cadastrar_veiculo(data)
    return jsonify(response)

@veiculos_bp.route("/", methods=["GET"])
def rota_listar_veiculos():
    response = listar_veiculos()
    return jsonify(response)

@veiculos_bp.route("/<placa>", methods=["PUT"])
def rota_alterar_status(placa):
    response = alterar_status_veiculo(placa)
    return jsonify(response)
