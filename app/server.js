import express from "express";
import dotenv from "dotenv";
import { seedDatabase } from "./seed.js";

import {
  createPostgresConnection,
  insertOrder as insertPgOrder,
  getOrderById as getPgOrderById,
  getOrdersByUserId as getPgOrdersByUserId,
  getOrdersByStatus as getPgOrdersByStatus,
  getOrdersInRange as getPgOrdersInRange,
  getAllOrderIds as getPgAllOrderIds,
} from "./db/postgres.js";

import {
  createMongoConnection,
  insertOrder as insertMgOrder,
  getOrderById as getMgOrderById,
  getOrdersByUserId as getMgOrdersByUserId,
  getOrdersByStatus as getMgOrdersByStatus,
  getOrdersInRange as getMgOrdersInRange,
  getAllOrderIds as getMgAllOrderIds,
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

app.post("/orders", async (req, res) => {
  try {
    const { user_id, status, total_value, created_at } = req.body;
    const data = {
      user_id,
      status,
      total_value,
      created_at: created_at || new Date(),
    };

    const result =
      dbType === "postgres"
        ? await insertPgOrder(dbClient, data)
        : await insertMgOrder(dbClient, data);

    res.status(201).json({ id: result.id || result._id });
  } catch (err) {
    console.error(err);
    res.status(500).send("Error inserting order");
  }
});

app.get("/orders/all/ids", async (_, res) => {
  try {
    const ids =
      dbType === "postgres"
        ? await getPgAllOrderIds(dbClient)
        : await getMgAllOrderIds(dbClient);
    res.json(ids);
  } catch (err) {
    console.error(err);
    res.status(500).send("Error fetching all order IDs");
  }
});

app.get("/orders/by-user/:userId", async (req, res) => {
  try {
    const { userId } = req.params;
    const limit = parseInt(req.query.limit || "50", 10);

    const result =
      dbType === "postgres"
        ? await getPgOrdersByUserId(dbClient, userId, limit)
        : await getMgOrdersByUserId(dbClient, userId, limit);

    res.json(result);
  } catch (err) {
    console.error(err);
    res.status(500).send("Error fetching orders by user ID");
  }
});

app.get("/orders/by-status/:status", async (req, res) => {
  try {
    const { status } = req.params;
    const limit = parseInt(req.query.limit || "50", 10);

    const result =
      dbType === "postgres"
        ? await getPgOrdersByStatus(dbClient, status, limit)
        : await getMgOrdersByStatus(dbClient, status, limit);

    res.json(result);
  } catch (err) {
    console.error(err);
    res.status(500).send("Error fetching orders by status");
  }
});

app.get("/orders/range", async (req, res) => {
  try {
    const { from, to } = req.query;
    if (!from || !to) {
      return res
        .status(400)
        .send("Query parameters 'from' and 'to' are required.");
    }
    const limit = parseInt(req.query.limit || "100", 10);

    const result =
      dbType === "postgres"
        ? await getPgOrdersInRange(dbClient, from, to, limit)
        : await getMgOrdersInRange(dbClient, from, to, limit);

    res.json(result);
  } catch (err) {
    console.error(err);
    res.status(500).send("Error fetching orders in range");
  }
});

app.get("/orders/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const result =
      dbType === "postgres"
        ? await getPgOrderById(dbClient, id)
        : await getMgOrderById(dbClient, id);

    if (!result) return res.status(404).send("Order not found");
    res.json(result);
  } catch (err) {
    console.error(err);
    res.status(500).send("Error fetching order");
  }
});
