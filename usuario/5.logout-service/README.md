# Logout Service (SOAP)

Este microservicio implementa un servicio SOAP para cerrar sesión de un usuario.

## Uso

- Puerto: `3001`
- Ruta SOAP: `/logout`
- Método: `logoutUser`
- Requiere: campo `username`
- Respuesta: mensaje confirmando logout

## Cómo probar

```bash
docker build -t logout-service .
docker run -p 3001:3001 logout-service
```

O usar con `docker-compose`.

Puedes probar con SOAP UI o Postman (modo SOAP).
