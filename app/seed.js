import { faker } from "@faker-js/faker";
import dotenv from "dotenv";

dotenv.config();

const USE_INDEX = process.env.USE_INDEX === "true";
const DATASET_SIZE = parseInt(process.env.DATASET_SIZE || "50000", 10);

export async function seedDatabase(client, dbType) {
  console.log(`⚙️ Seeding database (${dbType})...`);
  console.log(`📦 Dataset size: ${DATASET_SIZE.toLocaleString()} registros`);
  console.log(`🏗 Índices: ${USE_INDEX ? "ativados" : "desativados"}`);

  if (dbType === "postgres") {
    await client.query(`
      DROP TABLE IF EXISTS posts;
      CREATE TABLE posts (
        id SERIAL PRIMARY KEY,
        user_id INT,
        title TEXT,
        content TEXT,
        created_at TIMESTAMP DEFAULT NOW()
      );
    `);

    const BATCH_SIZE = 1000;
    console.log("🌱 Inserindo registros...");
    const totalBatches = Math.ceil(DATASET_SIZE / BATCH_SIZE);

    for (let b = 0; b < totalBatches; b++) {
      const values = [];
      const params = [];

      for (let i = 0; i < BATCH_SIZE; i++) {
        const idx = b * BATCH_SIZE + i;
        if (idx >= DATASET_SIZE) break;

        const userId = Math.floor(Math.random() * 1000) + 1;
        const title = faker.lorem.sentence();
        const content = faker.lorem.paragraphs(2);

        params.push(userId, title, content);
        values.push(
          `($${params.length - 2}, $${params.length - 1}, $${params.length})`
        );
      }

      await client.query(
        `INSERT INTO posts (user_id, title, content) VALUES ${values.join(
          ","
        )}`,
        params
      );

      if ((b + 1) % 10 === 0)
        console.log(
          `... ${Math.min((b + 1) * BATCH_SIZE, DATASET_SIZE)} inseridos`
        );
    }

    if (USE_INDEX) {
      console.log("🧱 Criando índices...");
      await client.query(
        "CREATE INDEX IF NOT EXISTS idx_posts_user_id ON posts(user_id)"
      );
      await client.query(
        "CREATE INDEX IF NOT EXISTS idx_posts_created_at ON posts(created_at)"
      );
    }

    console.log("✅ Seeding Postgres concluído!");
  } else if (dbType === "mongo") {
    const Post = client;

    console.log("🧹 Limpando coleção...");
    await Post.deleteMany({});

    console.log("🌱 Inserindo documentos...");
    const docs = [];
    for (let i = 0; i < DATASET_SIZE; i++) {
      docs.push({
        user_id: Math.floor(Math.random() * 1000) + 1,
        title: faker.lorem.sentence(),
        content: faker.lorem.paragraphs(2),
        created_at: new Date(),
      });

      if (docs.length >= 1000) {
        await Post.insertMany(docs);
        docs.length = 0;
        if (i % 5000 === 0 && i > 0) console.log(`${i} inseridos...`);
      }
    }

    if (docs.length > 0) await Post.insertMany(docs);

    if (USE_INDEX) {
      console.log("🧱 Criando índices no Mongo...");
      await Post.collection.createIndex({ user_id: 1 });
      await Post.collection.createIndex({ created_at: 1 });
    }

    console.log("✅ Seeding Mongo concluído!");
  } else {
    throw new Error(`❌ Tipo de banco desconhecido: ${dbType}`);
  }

  console.log("🏁 Seeding completo!\n");
}
