import time
import psycopg2
import os

while True:
    try:
        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT"),
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
        )
        conn.close()
        print("Banco de dados funcional!")
        break
    except psycopg2.OperationalError:
        print("Aguardando pelo banco de dados...")
        time.sleep(2)
