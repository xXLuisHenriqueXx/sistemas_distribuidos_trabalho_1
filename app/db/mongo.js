import mongoose from "mongoose";

const orderSchema = new mongoose.Schema({
  user_id: { type: Number, required: true },
  status: { type: String, required: true, index: true },
  total_value: { type: Number, required: true },
  created_at: { type: Date, default: Date.now, index: true },
});

const Order = mongoose.model("Order", orderSchema);

export async function createMongoConnection() {
  const uri = `mongodb://${process.env.MONGO_HOST || "mongo"}:27017/${
    process.env.DB_NAME || "testdb"
  }`;
  await mongoose.connect(uri);
  return Order;
}

export async function insertOrder(
  Order,
  { user_id, status, total_value, created_at }
) {
  return await Order.create({ user_id, status, total_value, created_at });
}

export async function getOrderById(Order, id) {
  try {
    return await Order.findById(id);
  } catch (err) {
    return null;
  }
}

export async function getOrdersByUserId(Order, uid, limit = 50) {
  const numericId = parseInt(uid, 10);
  if (isNaN(numericId)) return [];
  return await Order.find({ user_id: numericId })
    .sort({ created_at: -1 })
    .limit(limit);
}

export async function getOrdersByStatus(Order, status, limit = 50) {
  return await Order.find({ status }).sort({ created_at: -1 }).limit(limit);
}

export async function getOrdersInRange(Order, fromTs, toTs, limit = 100) {
  return await Order.find({
    created_at: { $gte: new Date(fromTs), $lte: new Date(toTs) },
  })
    .sort({ created_at: -1 })
    .limit(limit);
}

export async function getAllOrderIds(Order) {
  return await Order.find({}, "_id");
}
