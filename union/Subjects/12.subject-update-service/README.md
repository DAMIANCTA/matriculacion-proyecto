# Subject Update Service

Microservicio que permite actualizar los datos de una asignatura usando WebSocket (FastAPI).

## Endpoint WebSocket
```
ws://localhost:3008/ws/update-subject
```

## Formato de entrada esperado (JSON)
```json
{
  "id": "uuid-del-subject",
  "name": "Nuevo nombre",
  "description": "Nueva descripción",
  "credits": 5,
  "duration": "8 semanas"
}
```

## Cómo levantar con Docker
```bash
docker build -t subject-update-service .
docker run --env-file .env -p 3008:3008 subject-update-service
```