import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT")

def conecta_db(query, params=None):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        cur = conn.cursor()
        cur.execute(query, params)
        result = None
        if query.strip().lower().startswith("select"):
            result = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        print(f"Erro ao executar query: {e}")
        return None
