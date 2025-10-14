import pkg from "pg";
import { faker } from "@faker-js/faker";
import dotenv from "dotenv";

dotenv.config();
const { Pool } = pkg;

const USE_INDEX = process.env.USE_INDEX === "true";
const DATASET_SIZE = parseInt(process.env.DATASET_SIZE || "50000", 10);

export async function seedDatabase(pool) {
  console.log("🗑 Dropping and recreating table...");
  await pool.query(`
    DROP TABLE IF EXISTS posts;
    CREATE TABLE posts (
      id SERIAL PRIMARY KEY,
      user_id INT,
      title TEXT,
      content TEXT,
      created_at TIMESTAMP DEFAULT NOW()
    );
  `);

  console.log(`🌱 Inserting ${DATASET_SIZE.toLocaleString()} posts...`);
  const client = await pool.connect();
  try {
    await client.query("BEGIN");

    for (let i = 0; i < DATASET_SIZE; i++) {
      await client.query(
        "INSERT INTO posts (user_id, title, content) VALUES ($1, $2, $3)",
        [
          Math.floor(Math.random() * 1000) + 1,
          faker.lorem.sentence(),
          faker.lorem.paragraphs(2),
        ]
      );
      if (i % 5000 === 0 && i > 0) console.log(`${i} inserted...`);
    }

    if (USE_INDEX) {
      console.log("🧱 USE_INDEX=true → creating indices...");
      await client.query("CREATE INDEX IF NOT EXISTS idx_posts_user_id ON posts(user_id);");
      await client.query("CREATE INDEX IF NOT EXISTS idx_posts_created_at ON posts(created_at);");
      console.log("✅ Indices created.");
    } else {
      console.log("🧩 USE_INDEX=false → skipping index creation.");
    }

    await client.query("COMMIT");
  } catch (err) {
    await client.query("ROLLBACK");
    console.error("❌ Error while seeding:", err);
    throw err;
  } finally {
    client.release();
  }

  console.log("✅ Seeding complete!");
}
