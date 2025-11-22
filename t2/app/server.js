import express from "express";
import dotenv from "dotenv";
import { seedDatabase } from "./seed/seed.js";
import { startChaosMonkey } from "./caos.js";
import {
  createMongoConnection,
  insertOrder,
  getOrderById,
  getOrdersByUserId,
  getOrdersByStatus,
  getOrdersInRange,
  getAllOrderIds,
} from "./mongo/mongo.js";

dotenv.config();

const app = express();
app.use(express.json());

let isServerReady = false;

(async () => {
  console.log("Starting  App (NoSQL Distributed)...");

  try {
    await createMongoConnection();

    console.log("Iniciando Seed...");
    await seedDatabase("mongo-replicaset");

    const port = 3000;
    app.listen(port, () => {
      console.log(`App running on port ${port}`);
      isServerReady = true;
      console.log("Server marked as ready. Accepting connections.");

      console.log("Ativando Chaos Monkey...");
      startChaosMonkey();
    });
  } catch (err) {
    console.error("Startup error:", err);
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

app.post("/orders", async (req, res) => {
  try {
    const { user_id, status, total_value, created_at, ...extras } = req.body;
    const data = {
      user_id,
      status,
      total_value,
      created_at: created_at || new Date(),
      metadata: extras,
    };

    const result = await insertOrder(data);
    res.status(201).json({ id: result._id });
  } catch (err) {
    if (Math.random() < 0.01) console.error("Erro (amostra):", err.message);
    res.status(500).send("Error inserting order");
  }
});

app.get("/orders/all/ids", async (_, res) => {
  try {
    const ids = await getAllOrderIds();
    res.json(ids);
  } catch (err) {
    res.status(500).send("Error fetching IDs");
  }
});

app.get("/orders/by-user/:userId", async (req, res) => {
  try {
    const { userId } = req.params;
    const limit = parseInt(req.query.limit || "50", 10);
    const result = await getOrdersByUserId(userId, limit);
    res.json(result);
  } catch (err) {
    res.status(500).send("Error fetching by user");
  }
});

app.get("/orders/by-status/:status", async (req, res) => {
  try {
    const { status } = req.params;
    const limit = parseInt(req.query.limit || "50", 10);
    const result = await getOrdersByStatus(status, limit);
    res.json(result);
  } catch (err) {
    res.status(500).send("Error fetching by status");
  }
});

app.get("/orders/range", async (req, res) => {
  try {
    const { from, to } = req.query;
    if (!from || !to) return res.status(400).send("Missing dates");
    const limit = parseInt(req.query.limit || "100", 10);
    const result = await getOrdersInRange(from, to, limit);
    res.json(result);
  } catch (err) {
    res.status(500).send("Error fetching range");
  }
});

app.get("/orders/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const result = await getOrderById(id);
    if (!result) return res.status(404).send("Not found");
    res.json(result);
  } catch (err) {
    res.status(500).send("Error fetching order");
  }
});
