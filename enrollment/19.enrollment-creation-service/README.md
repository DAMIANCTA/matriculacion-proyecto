# Enrollment Creation Service

This microservice handles the creation of enrollment records in a PostgreSQL database. It validates student and section existence via cross-service calls.

## Tech Stack

- Python 3.11
- FastAPI
- PostgreSQL
- Docker
- SQLAlchemy

## Endpoints

### `POST /enrollments`

Creates a new enrollment if the student and section exist.

## Environment Variables

- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_NAME

## Run with Docker

```bash
docker build -t enrollment-creation-service .
docker run -p 3016:3016 --env-file .env enrollment-creation-service
```