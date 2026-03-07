# -------------------------------------------------------------
# Matheus MArins
# LOCADORA API
# ------------------------------------------------------------
FROM python:3.10.20-alpine3.22

# Labels OCI Padrão (boas práticas de uso de container)
LABEL org.opencontainers.image.title="Locadora API"
LABEL org.opencontainers.image.description="App back end - Interativa com banco de dados"
LABEL org.opencontainers.image.authors="Matheus Marins <matheus.bernardello@live.com>"
LABEL org.opencontainers.image.source="https://github.com/Marins14/Locadora"

# Cria usuario não root - segurança
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

COPY requirements.txt .

#Stage 2: Instala as dependencias da aplicação
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

# Mudar ownership para o usuário não-root
RUN chown -R appuser:appgroup /app

# Trocar para usuário não-root
USER appuser

EXPOSE 8000

CMD ["sh", "-c", "python app/wait_for_db.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]