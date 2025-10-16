import pkg from "pg";
const { Pool } = pkg;

export function createPostgresConnection() {
  const pool = new Pool({
    host: process.env.DB_HOST || "db",
    user: process.env.DB_USER || "postgres",
    password: process.env.DB_PASS || "postgres",
    database: process.env.DB_NAME || "testdb",
  });

  return pool;
}

export async function insertPost(pool, { user_id, title, content }) {
  const result = await pool.query(
    "INSERT INTO posts (user_id, title, content) VALUES ($1, $2, $3) RETURNING id",
    [user_id, title, content]
  );

  return result.rows[0];
}

export async function getPostById(pool, id) {
  const result = await pool.query("SELECT * FROM posts WHERE id=$1", [id]);

  return result.rows[0];
}
