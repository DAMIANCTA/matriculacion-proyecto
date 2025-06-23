FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3006
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3007"]
