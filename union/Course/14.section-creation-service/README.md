# section-creation-service

Microservicio para la creación de secciones de cursos.

### Lenguaje
Go (Gin)

### Arquitectura
WebHook

### Base de Datos
PostgreSQL - Tabla `sections`

### Endpoint
`POST /sections`

### JSON Esperado
```json
{
  "id": "uuid",
  "subject_id": "uuid",
  "name": "Sección 1",
  "total_capacity": 40,
  "current_capacity": 0,
  "schedule": "Lun-Mie-Vie 08:00-10:00",
  "creation_date": "2025-06-22T00:00:00Z"
}
```

### Ejecución local
```bash
docker build -t section-service .
docker run -p 3010:3010 --env-file .env section-service
```
