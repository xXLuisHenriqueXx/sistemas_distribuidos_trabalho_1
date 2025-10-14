import express from "express";
import pkg from "pg";
import { seedDatabase } from "./seed.js";

const { Pool } = pkg;
const app = express();
app.use(express.json());

const pool = new Pool({
  host: process.env.DB_HOST || "db",
  user: process.env.DB_USER || "postgres",
  password: process.env.DB_PASS || "postgres",
  database: process.env.DB_NAME || "testdb",
});

// 🔹 Reseed automático no startup
(async () => {
  console.log("⚙️ Reseeding database on startup...");
  try {
    await seedDatabase(pool);
    console.log("✅ Database reseeded successfully!");
  } catch (err) {
    console.error("❌ Error reseeding database:", err);
    process.exit(1);
  }
})();

app.get("/posts/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const result = await pool.query("SELECT * FROM posts WHERE id=$1", [id]);
    if (result.rows.length === 0) return res.status(404).send("Not found");
    res.json(result.rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).send("Error fetching post");
  }
});

app.post("/posts", async (req, res) => {
  try {
    const { user_id, title, content } = req.body;
    const result = await pool.query(
      "INSERT INTO posts (user_id, title, content) VALUES ($1, $2, $3) RETURNING id",
      [user_id, title, content]
    );
    res.status(201).json({ id: result.rows[0].id });
  } catch (err) {
    console.error(err);
    res.status(500).send("Error inserting post");
  }
});

const port = 3000;
app.listen(port, () => console.log(`🚀 App running on port ${port}`));
