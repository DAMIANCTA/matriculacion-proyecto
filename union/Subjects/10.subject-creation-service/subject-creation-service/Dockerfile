FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install fastapi "uvicorn[standard]" asyncpg
EXPOSE 3006
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3006"]