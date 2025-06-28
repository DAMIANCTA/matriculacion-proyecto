# Enrollment Reading Service

## Endpoints

- `GET /enrollments`: Obtener todas las matrículas
- `GET /enrollments/by-student/{id}`: Obtener matrículas por estudiante
- `GET /enrollments/by-state?state=ACTIVA`: Obtener matrículas por estado

## Variables de Entorno

- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_NAME`

## Uso

```bash
docker build -t enrollment-reading-service .
docker run -p 3020:3020 --env-file .env enrollment-reading-service
```
