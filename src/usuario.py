from datetime import datetime
from src.config import conecta_db

class Usuario:
    def __init__(self):
        pass
    
    def cadastrar_usuario(self, username, senha, email):
        query_verifica = "SELECT id FROM usuario WHERE username = %s;"
        usuario_existente = conecta_db(query_verifica, (username,))

        if usuario_existente:
            print("Usuário já cadastrado!")
            return

        data_criacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        status = True

        query = """
            INSERT INTO usuario (username, senha, email, data_criacao, status) 
            VALUES (%s, %s, %s, %s, %s);
        """
        params = (username, senha, email, data_criacao, status)

        conecta_db(query, params)
        print("Usuário cadastrado com sucesso!")

    @staticmethod
    def listar_usuarios():
        query = "SELECT id, username, email, status FROM usuario ORDER BY id;"
        usuarios = conecta_db(query)

        if usuarios:
            for u in usuarios:
                status_text = "Ativo" if u[3] else "Inativo"
                print(f"ID: {u[0]} | Username: {u[1]} | Email: {u[2]} | Status: {status_text}")
        else:
            print("Nenhum usuário cadastrado.")

    @staticmethod
    def desativar_usuario(username):
        # Verifica se o usuário existe
        query_verifica = "SELECT id FROM usuario WHERE username = %s;"
        usuario_existente = conecta_db(query_verifica, (username,))

        if not usuario_existente:
            print(f"Usuário '{username}' não encontrado.")
            return

        # Atualiza status no banco
        query = "UPDATE usuario SET status = False WHERE username = %s;"
        conecta_db(query, (username,))
        print(f"Usuário '{username}' foi desativado com sucesso!")
