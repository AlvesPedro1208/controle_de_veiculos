from app.config import conecta_db
from datetime import datetime

def cadastrar_veiculo(data):
    try:
        query = """
            INSERT INTO veiculos (
                placa, modelo, marca, ano_fabricacao, cor, chassi, tipo, capacidade_carga,
                combustivel, hodometro, data_aquisicao, observacoes, status, criado_em
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        params = (
            data.get("placa"),
            data.get("modelo"),
            data.get("marca"),
            data.get("ano_fabricacao"),
            data.get("cor"),
            data.get("chassi"),
            data.get("tipo"),
            data.get("capacidade_carga"),
            data.get("combustivel"),
            data.get("hodometro"),
            data.get("data_aquisicao"),
            data.get("observacoes"),
            True,  # status ativo por padrão
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

        conecta_db(query, params)
        return {"mensagem": f"Veículo {data.get('modelo')} ({data.get('placa')}) cadastrado com sucesso!"}
    except Exception as e:
        return {"erro": str(e)}

def listar_veiculos():
    query = """
        SELECT id_veiculo, placa, modelo, marca, ano_fabricacao, status
        FROM veiculos
        ORDER BY id_veiculo;
    """
    veiculos = conecta_db(query)
    lista = []

    if veiculos:
        for v in veiculos:
            lista.append({
                "id": v[0],
                "placa": v[1],
                "modelo": v[2],
                "marca": v[3],
                "ano": v[4],
                "status": "Ativo" if v[5] else "Inativo"
            })
    return lista

def alterar_status_veiculo(placa):
    query_verifica = "SELECT status FROM veiculos WHERE placa = %s;"
    status_atual = conecta_db(query_verifica, (placa,))

    if not status_atual:
        return {"erro": f"Veículo com placa {placa} não encontrado."}

    novo_status = not status_atual[0][0]

    query_update = "UPDATE veiculos SET status = %s WHERE placa = %s;"
    conecta_db(query_update, (novo_status, placa))

    return {"mensagem": f"Status do veículo {placa} alterado para: {'Ativo' if novo_status else 'Inativo'}"}
