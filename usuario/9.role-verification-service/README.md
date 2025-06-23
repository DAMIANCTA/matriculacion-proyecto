# role-verification-service

Microservicio para verificar el rol de un usuario vía WebSocket.

## 🧠 Tecnología
- Lenguaje: Python
- Framework: FastAPI
- Comunicación: WebSocket
- Base de datos: PostgreSQL (tabla `student_users`)

## 📦 Variables de entorno esperadas
- `DB_USER`: Usuario de la base de datos
- `DB_PASSWORD`: Contraseña
- `DB_NAME`: Nombre de la base de datos
- `DB_HOST`: Host (ej. postgres dentro de Docker)

## 🚀 Cómo ejecutar
```bash
docker build -t role-verification-service .
docker run -p 3005:3005 --env DB_USER=damian --env DB_PASSWORD=0710 --env DB_NAME=userdb --env DB_HOST=postgres role-verification-service
```

## 🧪 Prueba con websocat
```bash
websocat ws://localhost:3005/ws/verify-role
```
Y envía:
```json
{"username": "laura.ec", "role": "estudiante"}
```

## ✅ Respuestas posibles
```json
{ "status": "ok", "message": "Rol verificado" }
{ "status": "error", "message": "Rol no coincide o usuario no encontrado" }
```