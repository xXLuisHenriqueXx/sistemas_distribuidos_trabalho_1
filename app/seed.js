import { faker } from "@faker-js/faker";
import dotenv from "dotenv";

dotenv.config();

const USE_INDEX = process.env.USE_INDEX === "true";
const DATASET_SIZE = parseInt(process.env.DATASET_SIZE || "50000", 10);
const USER_COUNT = parseInt(process.env.USER_COUNT || "5000", 10); // option 2

const BATCH_SIZE = 1000;
const STATUSES = ["PENDING", "PAID", "SHIPPED", "CANCELLED"];

function randomCreatedAt() {
  return faker.date.between({ from: "2020-01-01", to: "2025-01-01" });
}

function randomTotal(min = 5, max = 1000) {
  const v = Math.random() * (max - min) + min;
  return Math.round(v * 100) / 100;
}

function pickUserId() {
  const hotThreshold = Math.floor(USER_COUNT * 0.05);
  if (Math.random() < 0.5) {
    return Math.floor(Math.random() * hotThreshold) + 1;
  } else {
    return (
      Math.floor(Math.random() * (USER_COUNT - hotThreshold)) + hotThreshold + 1
    );
  }
}

export async function seedDatabase(client, dbType) {
  console.log(`⚙️ Seeding database (${dbType})...`);
  console.log(`📦 Dataset size: ${DATASET_SIZE.toLocaleString()} registros`);
  console.log(`👥 Usuários (USER_COUNT): ${USER_COUNT}`);
  console.log(`🏗 Índices: ${USE_INDEX ? "ativados" : "desativados"}`);

  if (dbType === "postgres") {
    await client.query(`
      DROP TABLE IF EXISTS orders;
      CREATE TABLE orders (
        id SERIAL PRIMARY KEY,
        user_id INT NOT NULL,
        status TEXT NOT NULL,
        total_value NUMERIC(10,2) NOT NULL,
        created_at TIMESTAMP NOT NULL
      );
    `);

    console.log("🌱 Inserindo registros (Postgres orders)...");
    const totalBatches = Math.ceil(DATASET_SIZE / BATCH_SIZE);

    for (let b = 0; b < totalBatches; b++) {
      const values = [];
      const params = [];

      for (let i = 0; i < BATCH_SIZE; i++) {
        const idx = b * BATCH_SIZE + i;
        if (idx >= DATASET_SIZE) break;

        const userId = pickUserId();
        const r = Math.random();
        let status = "PAID";
        if (r < 0.1) status = "PENDING";
        else if (r < 0.65) status = "PAID";
        else if (r < 0.9) status = "SHIPPED";
        else status = "CANCELLED";

        const totalValue = randomTotal(5, 2000);
        const createdAt = randomCreatedAt();

        params.push(userId, status, totalValue, createdAt);
        values.push(
          `($${params.length - 3}, $${params.length - 2}, $${
            params.length - 1
          }, $${params.length})`
        );
      }

      await client.query(
        `INSERT INTO orders (user_id, status, total_value, created_at) VALUES ${values.join(
          ","
        )}`,
        params
      );

      if ((b + 1) % 10 === 0) {
        console.log(
          `... ${Math.min((b + 1) * BATCH_SIZE, DATASET_SIZE)} inseridos`
        );
      }
    }

    if (USE_INDEX) {
      console.log("🧱 Criando índices (Postgres)...");
      await client.query(
        `CREATE INDEX IF NOT EXISTS idx_orders_user_id ON orders(user_id);`
      );
      await client.query(
        `CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(status);`
      );
      await client.query(
        `CREATE INDEX IF NOT EXISTS idx_orders_user_created ON orders(user_id, created_at DESC);`
      );
      await client.query(
        `CREATE INDEX IF NOT EXISTS idx_orders_created_at ON orders(created_at);`
      );
    }

    console.log("✅ Seeding Postgres (orders) concluído!");
  } else if (dbType === "mongo") {
    const Order = client;

    console.log("🧹 Limpando coleção (Mongo orders)...");
    await Order.deleteMany({});

    console.log("🌱 Inserindo documentos (Mongo orders)...");
    const docs = [];
    for (let i = 0; i < DATASET_SIZE; i++) {
      const userId = pickUserId();
      const r = Math.random();
      let status = "PAID";
      if (r < 0.1) status = "PENDING";
      else if (r < 0.65) status = "PAID";
      else if (r < 0.9) status = "SHIPPED";
      else status = "CANCELLED";

      docs.push({
        user_id: userId,
        status,
        total_value: randomTotal(5, 2000),
        created_at: randomCreatedAt(),
      });

      if (docs.length >= 1000) {
        await Order.insertMany(docs);
        docs.length = 0;
        if ((i + 1) % 10000 === 0) console.log(`${i + 1} inseridos...`);
      }
    }

    if (docs.length > 0) await Order.insertMany(docs);

    if (USE_INDEX) {
      console.log("🧱 Criando índices (Mongo)...");
      await Order.collection.createIndex({ user_id: 1 });
      await Order.collection.createIndex({ status: 1 });
      await Order.collection.createIndex({ user_id: 1, created_at: -1 });
      await Order.collection.createIndex({ created_at: 1 });
    }

    console.log("✅ Seeding Mongo (orders) concluído!");
  } else {
    throw new Error(`❌ Tipo de banco desconhecido: ${dbType}`);
  }

  console.log("🏁 Seeding completo!\n");
}
