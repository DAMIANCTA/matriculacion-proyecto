const { Pool } = require('pg');

const pool = new Pool({
  user: process.env.DB_USER,
  host: process.env.DB_HOST,
  database: process.env.DB_NAME,
  password: process.env.DB_PASSWORD,
  port: 5432
});

module.exports = {
  Mutation: {
    deleteSection: async (_, { id }) => {
      try {
        const res = await pool.query('DELETE FROM sections WHERE id = $1', [id]);
        return res.rowCount > 0
          ? "Section deleted successfully"
          : "Section not found";
      } catch (error) {
        console.error("Deletion error:", error);
        return "Internal server error";
      }
    }
  }
};