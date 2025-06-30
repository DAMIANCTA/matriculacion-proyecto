
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy psycopg2-binary
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3023"]
