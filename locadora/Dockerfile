FROM python:3.10.20-alpine3.22

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 8000

CMD  ["python wait_for_db.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]