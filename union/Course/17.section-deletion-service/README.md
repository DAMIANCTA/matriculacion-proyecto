# 🧩 section-deletion-service (Microservicio 17)

**Lenguaje**: Node.js  
**Estilo**: GraphQL  
**Base de datos**: PostgreSQL (`sections`)  
**Puerto**: `3014`  
**Dominio**: Course Sections  

## 🎯 Función
Elimina una sección según su `id` usando una mutación GraphQL.

## 📦 Instalación

```bash
npm install
npm start
```

## 🚀 Ejemplo GraphQL

```
mutation {
  deleteSection(id: "SECCION_ID_UUID")
}
```

## 🐳 Docker

```bash
docker build -t section-deletion-service .
docker run -p 3014:3014 --env-file .env section-deletion-service
```

## ✅ Cumple con:
- GraphQL como estilo
- PostgreSQL como backend
- Principios SOLID / KISS / DRY
- Listo para CI/CD y despliegue