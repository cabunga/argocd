import os
from fastapi import FastAPI
import psycopg2

app = FastAPI()

# Las credenciales vendrán de los Secrets de Kubernetes
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASS = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "mydb")

@app.get("/")
def read_root():
    try:
        # Intenta conectarse a la base de datos
        conn = psycopg2.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASS, dbname=DB_NAME
        )
        conn.close()
        return {"status": "success", "message": "¡Conexión a la base de datos exitosa!"}
    except Exception as e:
        return {"status": "error", "message": f"Fallo al conectar: {str(e)}"}
