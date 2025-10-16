import express from "express";
import dotenv from "dotenv";
import { seedDatabase } from "./seed.js";
import {
  createPostgresConnection,
  insertPost as insertPg,
  getPostById as getPgById,
} from "./db/postgres.js";
import {
  createMongoConnection,
  insertPost as insertMg,
  getPostById as getMgById,
} from "./db/mongo.js";

dotenv.config();

const app = express();
app.use(express.json());

let dbClient = null;

const dbType = process.env.DB_TYPE || "postgres";

(async () => {
  console.log("⚙️ Starting up...");

  try {
    if (dbType === "postgres") {
      dbClient = await createPostgresConnection();
    } else {
      dbClient = await createMongoConnection();
    }

    await seedDatabase(dbClient, dbType);

    console.log("✅ Database ready, starting server...");

    const port = 3000;
    app.listen(port, () => console.log(`🚀 App running on port ${port}`));
  } catch (err) {
    console.error("❌ Startup error:", err);
    process.exit(1);
  }
})();

app.get("/posts/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const result =
      dbType === "postgres"
        ? await getPgById(dbClient, id)
        : await getMgById(dbClient, id);

    if (!result) return res.status(404).send("Not found");
    res.json(result);
  } catch (err) {
    console.error(err);
    res.status(500).send("Error fetching post");
  }
});

app.post("/posts", async (req, res) => {
  try {
    const { user_id, title, content } = req.body;
    const result =
      dbType === "postgres"
        ? await insertPg(dbClient, { user_id, title, content })
        : await insertMg(dbClient, { user_id, title, content });
    res.status(201).json({ id: result.id || result._id });
  } catch (err) {
    console.error(err);
    res.status(500).send("Error inserting post");
  }
});
