# Subject Creation Service

Este microservicio crea nuevas asignaturas usando WebSocket y FastAPI.

## WebSocket Endpoint

- URL: `ws://localhost:3006/ws/create-subject`

### Payload

```json
{
  "name": "Matemáticas",
  "description": "Cálculo diferencial",
  "credits": 6,
  "duration": "60 horas"
}
```

### Respuesta

```json
{
  "status": "ok",
  "message": "Asignatura creada exitosamente"
}
```

## Docker

```bash
docker build -t subject-creation-service .
docker run -p 3006:3006 --env DB_USER=damian --env DB_PASSWORD=0710 --env DB_NAME=subjects_db --env DB_HOST=postgres subject-creation-service
```
