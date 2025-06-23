# Role Assignment Service

Microservicio SOAP para asignación de roles a usuarios.

## 🔧 Tecnologías
- Node.js (Express)
- PostgreSQL
- SOAP

## 📁 Estructura
- `index.js`: inicia el servidor SOAP
- `roleService.js`: lógica de negocio (consulta y asignación de rol)
- `wsdl/role-assignment.wsdl`: definición WSDL del servicio

## ▶️ Uso
### Requisitos
- Docker y Docker Compose
- Base de datos PostgreSQL corriendo con tabla `student_users`

### Comando
```bash
docker build -t usuario-role-assignment-service .
docker run -p 3003:3003 --env DB_USER=damian --env DB_PASSWORD=0710 --env DB_HOST=postgres --env DB_NAME=userdb usuario-role-assignment-service
```

### Endpoint SOAP
```
POST http://localhost:3003/assign-role
SOAPAction: ""
```

### Ejemplo de request:
```xml
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tns="http://www.globalenrollment.com/role">
  <soap:Body>
    <tns:assignRole>
      <id>UUID-del-usuario</id>
      <role>admin</role>
    </tns:assignRole>
  </soap:Body>
</soap:Envelope>
```
