import express from "express";
import dotenv from "dotenv";
import { seedDatabase } from "./seed.js";
import {
  createPostgresConnection,
  insertPost as insertPg,
  getPostById as getPgById,
  getPostsByUserId as getPgByUserId,
  getAllPostIds as getAllPgIds,
} from "./db/postgres.js";
import {
  createMongoConnection,
  insertPost as insertMg,
  getPostById as getMgById,
  getPostsByUserId as getMgByUserId,
  getAllPostIds as getAllMgIds,
} from "./db/mongo.js";

dotenv.config();

const app = express();
app.use(express.json());

let dbClient = null;
let isServerReady = false; // <-- 1. Flag de prontidão

const dbType = process.env.DB_TYPE || "postgres";
const ENABLE_SECONDARY_READS = process.env.ENABLE_SECONDARY_READS === 'true';

(async () => {
  console.log("⚙️ Starting up...");

  try {
    if (dbType === "postgres") {
      dbClient = await createPostgresConnection();
    } else {
      dbClient = await createMongoConnection();
    }

    // O seeding agora acontece ANTES de marcar como pronto
    await seedDatabase(dbClient, dbType);

    console.log("✅ Database seeded.");

    const port = 3000;
    app.listen(port, () => {
      console.log(`🚀 App running on port ${port}`);
      // 2. Marca como pronto SÓ DEPOIS do listen
      isServerReady = true;
      console.log("✅ Server marked as ready.");
    });
  } catch (err) {
    console.error("❌ Startup error:", err);
    process.exit(1);
  }
})();

// --- 3. NOVA ROTA DE HEALTHCHECK ---
app.get("/health", (req, res) => {
  if (isServerReady) {
    res.status(200).send("OK");
  } else {
    // Responde 503 Service Unavailable se o seeding ainda não terminou
    res.status(503).send("Server Not Ready");
  }
});

app.get("/posts/all/ids", async (req, res) => {
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


// Rota de leitura primária (ID) (sem alterações)
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

// Rota condicional (sem alterações)
if (ENABLE_SECONDARY_READS) {
  console.log("... Rota de leitura secundária (/users/:uid) ATIVADA.");
  app.get("/users/:uid/posts", async (req, res) => {
    try {
      const { uid } = req.params;
      const result =
        dbType === "postgres"
          ? await getPgByUserId(dbClient, uid) 
          : await getMgByUserId(dbClient, uid); 

      res.json(result);
    } catch (err) {
      console.error(err);
      res.status(500).send("Error fetching posts by user");
    }
  });
} else {
  console.log("... Rota de leitura secundária (/users/:uid) DESATIVADA.");
}


// Rota de escrita (sem alterações)
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

