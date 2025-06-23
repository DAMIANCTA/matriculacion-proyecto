# Section Update Service

✅ **Lenguaje**: Go  
✅ **Estilo**: WebHook  
✅ **Base de datos**: PostgreSQL (tabla `sections`)  
✅ **Diseño**: SOLID, KISS, DRY  

## Uso

### Endpoint
- `POST /webhook/update-section`  
  Payload:
  ```json
  {
    "id": "uuid",
    "subject_id": "uuid",
    "name": "Math B",
    "total_capacity": 50,
    "current_capacity": 45,
    "schedule": "Mon-Wed 10:00-12:00"
  }
  ```

### Docker

```bash
docker build -t section-update-service .
docker run -p 3011:3011 --env-file .env section-update-service
```
