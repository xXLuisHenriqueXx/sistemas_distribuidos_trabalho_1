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

export async function insertOrder(
  pool,
  { user_id, status, total_value, created_at }
) {
  const result = await pool.query(
    "INSERT INTO orders (user_id, status, total_value, created_at) VALUES ($1, $2, $3, $4) RETURNING id",
    [user_id, status, total_value, created_at]
  );

  return result.rows[0];
}

export async function getOrderById(pool, id) {
  const result = await pool.query("SELECT * FROM orders WHERE id=$1", [id]);
  return result.rows[0];
}

export async function getOrdersByUserId(pool, uid, limit = 50) {
  const result = await pool.query(
    "SELECT * FROM orders WHERE user_id = $1 ORDER BY created_at DESC LIMIT $2",
    [uid, limit]
  );
  return result.rows;
}

export async function getOrdersByStatus(pool, status, limit = 50) {
  const result = await pool.query(
    "SELECT * FROM orders WHERE status = $1 ORDER BY created_at DESC LIMIT $2",
    [status, limit]
  );
  return result.rows;
}

export async function getOrdersInRange(pool, fromTs, toTs, limit = 100) {
  const result = await pool.query(
    "SELECT * FROM orders WHERE created_at BETWEEN $1 AND $2 ORDER BY created_at DESC LIMIT $3",
    [fromTs, toTs, limit]
  );
  return result.rows;
}

export async function getAllOrderIds(pool) {
  const result = await pool.query("SELECT id FROM orders");
  return result.rows;
}
