# subject-reading-service

Este microservicio permite consultar asignaturas usando WebSocket.

## 🧪 Uso

1. Asegúrate de tener la tabla `subjects` en la base de datos `subjects_db` en PostgreSQL.
2. Construye la imagen:

```bash
docker build -t subject-reading-service .
```

3. Ejecuta el contenedor:

```bash
docker run -p 3007:3007 --network=host subject-reading-service
```

4. Abre `ws-client/leer-asignaturas.html` en el navegador para usar el cliente WebSocket.

## 📦 Variables de entorno

- `DB_USER=damian`
- `DB_PASSWORD=0710`
- `DB_HOST=postgres`
- `DB_NAME=subjects_db`
