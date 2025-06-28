FROM python:3.11-slim

WORKDIR /app

RUN apt update && apt install -y curl

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3016"]
