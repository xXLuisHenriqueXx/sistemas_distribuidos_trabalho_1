import { faker } from "@faker-js/faker";
import dotenv from "dotenv";
import { insertManyOrders } from "../mongo/mongo.js";

dotenv.config();

const DATASET_SIZE = parseInt(process.env.DATASET_SIZE || "50000", 10);
const USER_COUNT = parseInt(process.env.USER_COUNT || "5000", 10);
const COMPLEX_DOC_RATIO = parseFloat(process.env.COMPLEX_DOC_RATIO || "0.6");

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

function generateDynamicMetadata(status) {
  const isComplex = Math.random() < COMPLEX_DOC_RATIO;

  if (isComplex) {
    const itemsCount = Math.floor(Math.random() * 5) + 3;
    const items = [];
    for (let k = 0; k < itemsCount; k++) {
      items.push({
        name: faker.commerce.productName(),
        price: parseFloat(faker.commerce.price()),
        sku: faker.string.alphanumeric(12),
        description: faker.commerce.productDescription(),
      });
    }
    return {
      type: "physical_goods_heavy",
      priority_shipping: Math.random() > 0.5,
      items,
      shipping_address: {
        street: faker.location.streetAddress(),
        city: faker.location.city(),
        zip: faker.location.zipCode(),
        country: faker.location.country(),
      },
    };
  }

  const subtype = Math.random();

  if (subtype < 0.5) {
    return {
      type: "digital_service",
      license_key: faker.string.uuid(),
    };
  } else {
    return {
      type: "simple_order",
      note: "No metadata",
    };
  }
}

export async function seedDatabase(dbType) {
  console.log(`Iniciando Seed (${dbType})...`);
  console.log(`Dataset: ${DATASET_SIZE.toLocaleString()} docs`);
  console.log(
    `Complexidade: ${(COMPLEX_DOC_RATIO * 100).toFixed(0)}% dos docs serão pesados`,
  );

  const docs = [];
  const batchSize = 2000;

  for (let i = 0; i < DATASET_SIZE; i++) {
    const userId = pickUserId();
    const r = Math.random();
    let status = "PAID";
    if (r < 0.1) status = "PENDING";
    else if (r < 0.65) status = "PAID";
    else if (r < 0.9) status = "SHIPPED";
    else status = "CANCELLED";

    const baseDoc = {
      user_id: userId,
      status,
      total_value: randomTotal(5, 2000),
      created_at: randomCreatedAt(),
      metadata: generateDynamicMetadata(status),
    };

    docs.push(baseDoc);

    if (docs.length >= batchSize) {
      await insertManyOrders(docs);
      docs.length = 0;
      if ((i + 1) % 10000 === 0) console.log(`${i + 1} inseridos...`);
    }
  }

  if (docs.length > 0) await insertManyOrders(docs);

  console.log("Inserção concluída.");
  console.log("Seed completo!\n");
}
