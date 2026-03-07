import time
import psycopg2
import os

while True:
    try:
        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=os.getenv("POSTGRES_PORT", "5432"),
            database=os.getenv("POSTGRES_DB", "locadora"),
            user=os.getenv("POSTGRES_USER", "applocadora"),
            password=os.getenv("POSTGRES_PASSWORD", "applocadora"),
        )
        conn.close()
        print("Banco de dados funcional!")
        break
    except psycopg2.OperationalError:
        print("Aguardando pelo banco de dados...")
        time.sleep(2)
