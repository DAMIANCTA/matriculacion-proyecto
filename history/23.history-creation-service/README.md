# history-creation-service

Microservicio para registrar el historial académico de un estudiante en el sistema distribuido de matriculación.

## Tecnologías
- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker

## Endpoints
- `POST /history`: Crear un nuevo registro de historial académico.

## Ejemplo JSON
```json
{
  "student_id": "uuid",
  "section_id": "uuid",
  "description": "Matrícula en sección"
}
```

## Pruebas
Las pruebas funcionales pueden realizarse con Postman o pytest.
