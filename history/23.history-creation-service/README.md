# history-creation-service

Este microservicio registra eventos históricos relacionados con la matrícula de estudiantes.

## Tecnologías
- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker

## Endpoint principal

### `POST /history`
Crea una entrada en el historial académico. Valida que `student_id` y `section_id` existan.

## CI/CD
Preparado para integrar con GitHub Actions, DockerHub y desplegarse en AWS.
