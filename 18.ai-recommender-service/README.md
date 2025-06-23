
# ai-recommender-service

Microservicio 18 del sistema de matriculación distribuido.
- **Dominio:** AI-Based Recommender
- **Lenguaje:** C# (.NET)
- **Estilo de arquitectura:** GraphQL
- **Base de datos:** MongoDB (NoSQL documental)
- **Funcionalidad:** Generar recomendaciones personalizadas con base en secciones disponibles.

## Uso

1. Iniciar MongoDB.
2. Ejecutar el contenedor con Docker.
3. Enviar la siguiente consulta GraphQL a `http://localhost:3015/graphql`:

```
query {
  generateRecommendations(userId: "123")
}
```

## Docker

Este microservicio se construye con:

```
docker build -t ai-recommender-service .
docker run -p 3015:80 --env-file .env ai-recommender-service
```
