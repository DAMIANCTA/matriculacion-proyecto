const { Pool } = require('pg');

const pool = new Pool({
  user: process.env.DB_USER || 'damian',
  host: process.env.DB_HOST || 'postgres',
  database: process.env.DB_NAME || 'userdb',
  password: process.env.DB_PASSWORD || '0710',
  port: 5432
});


const service = {
  RoleAssignmentService: {
    RoleAssignmentPort: {
      async assignRole(args) {
        try {
          // args puede ser { id, role } o { parameters: { id, role } }
          const { id, role } = args.parameters || args;
          const user = await pool.query('SELECT * FROM student_users WHERE id = $1', [id]);
          if (user.rows.length === 0) {
            return { assignRoleResponse: { message: "Usuario no encontrado" } };
          }
          await pool.query('UPDATE student_users SET role = $1 WHERE id = $2', [role, id]);
          return { assignRoleResponse: { message: "Rol asignado correctamente" } };
        } catch (err) {
          console.error("Error al asignar rol:", err);
          return { assignRoleResponse: { message: "Error interno del servidor" } };
        }
      }
    }
  }
};

module.exports = service;