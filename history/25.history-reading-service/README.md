# History Reading Service

Microservicio para consulta avanzada de historial académico por estudiante o sección.

## Endpoints

- `GET /history/by-student/{student_id}`
- `GET /history/by-section/{section_id}`

## Stack

- Python 3.11
- FastAPI
- PostgreSQL
- Docker

## Pruebas

```bash
pytest tests/test_history.py
```
