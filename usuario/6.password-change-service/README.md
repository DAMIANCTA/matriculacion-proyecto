# password-change-service

Microservicio SOAP para el cambio de contraseña de usuarios.

## Uso

- Puerto: 3002
- Endpoint SOAP: `/password`

## Configuración de conexión PostgreSQL

Se conecta a la base de datos `userdb` con:
- Usuario: `damian`
- Contraseña: `0710`
- Host: `postgres`

## Comandos Docker

```bash
docker build -t password-change-service .
docker run -p 3002:3002 password-change-service
```