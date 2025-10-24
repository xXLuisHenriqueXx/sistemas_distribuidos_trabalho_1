import express from "express";
import dotenv from "dotenv";
import { seedDatabase } from "./seed.js";
import {
  createPostgresConnection,
  insertPost as insertPg,
  getPostById as getPgById,
  getAllPostIds as getAllPgIds,
} from "./db/postgres.js";
import {
  createMongoConnection,
  insertPost as insertMg,
  getPostById as getMgById,
  getAllPostIds as getAllMgIds,
} from "./db/mongo.js";

dotenv.config();

const app = express();
app.use(express.json());

let dbClient = null;
let isServerReady = false;

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

    console.log("✅ Database seeded.");

    const port = 3000;
    app.listen(port, () => {
      console.log(`🚀 App running on port ${port}`);
      isServerReady = true;
      console.log("✅ Server marked as ready.");
    });
  } catch (err) {
    console.error("❌ Startup error:", err);
    process.exit(1);
  }
})();

app.get("/health", (_, res) => {
  if (isServerReady) {
    res.status(200).send("OK");
  } else {
    res.status(503).send("Server Not Ready");
  }
});

app.get("/posts/all/ids", async (_, res) => {
  try {
    const ids =
      dbType === "postgres"
        ? await getAllPgIds(dbClient)
        : await getAllMgIds(dbClient);
    res.json(ids);
  } catch (err) {
    console.error(err);
    res.status(500).send("Error fetching all IDs");
  }
});

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
    let data, result;

    if (dbType === "postgres") {
      const { user_id, title, content } = req.body;
      data = { user_id, title, content };
      result = await insertPg(dbClient, data);
    } else {
      const { author, title, content } = req.body;
      data = { author, title, content, created_at: new Date() };
      result = await insertMg(dbClient, data);
    }

    res.status(201).json({ id: result.id || result._id });
  } catch (err) {
    console.error(err);
    res.status(500).send("Error inserting post");
  }
});
