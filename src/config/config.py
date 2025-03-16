import psycopg2
import os
import sys
from dotenv import load_dotenv

# Garante que a saída do terminal use UTF-8
os.environ["PYTHONIOENCODING"] = "utf-8"
sys.stdout.reconfigure(encoding='utf-8')

# Credenciais do DB
load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')

def connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        print('Conectado ao banco de dados!')
        return conn
    except Exception as e:
        print(f'Erro ao conectar ao banco: {e}')
        return None

# Função para executar queries
def conecta_db(query, params=None):
    conn = connection()
    if conn is None:
        print('Erro ao conectar ao DB!')
        return

    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = None
        if query.strip().lower().startswith("select"):
            result = cursor.fetchall()  
        conn.commit()
        cursor.close()
        return result
    except Exception as e:
        print(f'Erro ao executar a query: {e}')
    finally:
        conn.close()
