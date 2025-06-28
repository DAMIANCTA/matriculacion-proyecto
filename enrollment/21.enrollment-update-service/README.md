# enrollment-update-service

Este microservicio permite actualizar el estado de una matrícula dentro del sistema distribuido de matriculación.

## Endpoints

### PUT `/enrollments/{id}`
Actualiza completamente la matrícula con el ID proporcionado.

### PATCH `/enrollments/{id}/status`
Actualiza únicamente el estado de la matrícula (por ejemplo, cancelar o finalizar).  
Si se cambia a "cancelado", se registra en la tabla `enrollment_logs`.

## Base de Datos

Este microservicio se conecta a **dos tablas** dentro de una base de datos PostgreSQL:
- `enrollments`: tabla relacional con información de las matrículas activas.
- `enrollment_logs`: tabla tipo logs/time-series que guarda el historial de cambios.

## Tecnologías

- Lenguaje: Python
- Framework: FastAPI
- Base de datos: PostgreSQL (relacional + logs)
- Arquitectura: REST
- Docker: Sí
- CI/CD: Compatible con GitHub Actions y DockerHub
- Patrones: KISS, SOLID, DRY
