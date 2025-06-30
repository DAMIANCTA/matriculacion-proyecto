
# Academic History Service

Microservicio REST desarrollado con FastAPI para consultar historial académico.  
Valida identificadores por estudiante, sección y matrícula.

## Endpoints
- `GET /history`  
- `GET /history/{history_id}`  
- `GET /history/student/{student_id}`

## Arquitectura
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker

## Diseño aplicado
- **KISS**: Código limpio y directo.
- **SOLID**: Responsabilidad única y dependencias bien definidas.
- **DRY**: Reutilización de lógica.

## CI/CD & Despliegue
Preparado para GitHub, DockerHub y AWS Academy.
