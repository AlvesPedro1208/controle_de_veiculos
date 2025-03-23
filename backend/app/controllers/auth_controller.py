from app.config import conecta_db

def autenticar_usuario(username, senha):
    query = """
        SELECT id_usuario, username, email, status
        FROM usuarios
        WHERE username = %s AND senha = %s;
    """
    resultado = conecta_db(query, (username, senha))

    if resultado:
        usuario = resultado[0]
        return {
            "id": usuario[0],
            "username": usuario[1],
            "email": usuario[2],
            "status": "Ativo" if usuario[3] else "Inativo"
        }

    return None
