const { Pool } = require('pg');

const pool = new Pool({
  user: process.env.DB_USER || 'damian',
  host: process.env.DB_HOST || 'postgres',
  database: process.env.DB_NAME || 'userdb',
  password: process.env.DB_PASSWORD || '0710',
  port: 5432
});

const service = {
  DeleteUserService: {
    DeleteUserPort: {
      async deleteUser({ id }) {
        try {
          const result = await pool.query('DELETE FROM student_users WHERE id = $1', [id]);

          if (result.rowCount === 0) {
            return { message: "Usuario no encontrado" };
          }

          return { message: "Usuario eliminado correctamente" };
        } catch (err) {
          console.error("Error al eliminar usuario:", err);
          return { message: "Error interno del servidor" };
        }
      }
    }
  }
};

module.exports = service;
