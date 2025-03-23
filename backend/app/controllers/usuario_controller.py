from datetime import datetime
from app.config import conecta_db

def cadastrar_usuario(data):
    username = data.get("username")
    senha = data.get("senha")
    email = data.get("email")

    query_verifica = "SELECT id FROM usuarios WHERE username = %s;"
    existente = conecta_db(query_verifica, (username,))
    if existente:
        return {"mensagem": "Usuário já cadastrado"}

    query = """
        INSERT INTO usuarios (username, senha, email, data_criacao, status)
        VALUES (%s, %s, %s, %s, %s);
    """
    params = (
        username,
        senha,
        email,
        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        True
    )
    conecta_db(query, params)
    return {"mensagem": "Usuário cadastrado com sucesso"}

def listar_usuarios():
    query = "SELECT id_usuario, username, email, status FROM usuarios ORDER BY id_usuario;"
    usuarios = conecta_db(query)

    lista = []
    if usuarios:
        for u in usuarios:
            lista.append({
                "id": u[0],
                "username": u[1],
                "email": u[2],
                "status": "Ativo" if u[3] else "Inativo"
            })
    return lista
