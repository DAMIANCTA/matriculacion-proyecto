const { Pool } = require('pg');

const pool = new Pool({
  user: process.env.DB_USER || 'damian',
  host: process.env.DB_HOST || 'postgres',
  database: process.env.DB_NAME || 'userdb',
  password: process.env.DB_PASSWORD || '0710',
  port: 5432
});



const service = {
  PasswordChangeService: {
    PasswordChangePort: {
      async changePassword({ username, oldPassword, newPassword }) {
        try {
          const res = await pool.query(
            'SELECT * FROM student_users WHERE username = $1 AND password = $2',
            [username, oldPassword]
          );

          if (res.rows.length === 0) {
            return { message: "Credenciales incorrectas" };
          }

          await pool.query(
            'UPDATE student_users SET password = $1 WHERE username = $2',
            [newPassword, username]
          );

          return { message: "Contraseña actualizada correctamente" };
        } catch (err) {
          console.error("Error en el servicio de cambio de contraseña:", err);
          return { message: "Error interno del servidor" };
        }
      }
    }
  }
};

module.exports = service;