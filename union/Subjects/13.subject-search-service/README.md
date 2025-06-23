# subject-search-service

Microservicio WebHook en Go (Fiber) para realizar búsquedas avanzadas de asignaturas.

## Endpoint

`POST /webhook/subject-search`

### JSON Body

```json
{
  "name": "matemática",
  "credits": 4,
  "duration": "semestre"
}
```

## Docker

```bash
docker build -t subject-search-service .
docker run -p 3009:3009 --env DB_USER=damian --env DB_PASSWORD=0710 --env DB_NAME=subjects_db --env DB_HOST=subjects_db subject-search-service
```