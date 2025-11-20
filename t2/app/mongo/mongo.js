import mongoose from "mongoose";

const READ_PREFERENCE = process.env.READ_PREFERENCE || "secondaryPreferred";
const WRITE_CONCERN = process.env.WRITE_CONCERN || "1";

const orderSchema = new mongoose.Schema({
  user_id: { type: Number, required: true, index: true },
  status: { type: String, required: true },
  total_value: { type: Number, required: true },
  created_at: { type: Date, default: Date.now },
  metadata: { type: mongoose.Schema.Types.Mixed } 
}, { 
  strict: false,
  read: READ_PREFERENCE 
});

const Order = mongoose.model("Order", orderSchema);

export async function createMongoConnection() {
  const hosts = process.env.MONGO_HOSTS || "mongo1:27017,mongo2:27017,mongo3:27017";
  const dbName = "ecommerce";
  
  const uri = `mongodb://${hosts}/${dbName}?replicaSet=rs0&readPreference=${READ_PREFERENCE}&w=${WRITE_CONCERN}`;
  
  console.log(`🔌 Conectando ao Mongo...`);
  console.log(`   📝 Read Preference: ${READ_PREFERENCE}`);
  console.log(`   💾 Write Concern: ${WRITE_CONCERN}`);
  
  await mongoose.connect(uri, {
    serverSelectionTimeoutMS: 10000,
  });

  mongoose.connection.on('connected', () => console.log('✅ Mongoose conectado.'));
  mongoose.connection.on('error', (err) => console.error('❌ Erro Mongoose:', err.message));
  
  return Order;
}

export async function insertOrder(data) {
  return await Order.create(data);
}

export async function insertManyOrders(docs) {
  return await Order.insertMany(docs, { ordered: false });
}

export async function getOrderById(id) {
  try {
    return await Order.findById(id);
  } catch (err) {
    return null;
  }
}

export async function getOrdersByUserId(uid, limit = 50) {
  const numericId = parseInt(uid, 10);
  if (isNaN(numericId)) return [];
  
  return await Order.find({ user_id: numericId })
    .sort({ created_at: -1 })
    .limit(limit)
    .lean();
}

export async function getOrdersByStatus(status, limit = 50) {
  return await Order.find({ status })
    .sort({ created_at: -1 })
    .limit(limit)
    .lean();
}

export async function getOrdersInRange(fromTs, toTs, limit = 100) {
  return await Order.find({
    created_at: { $gte: new Date(fromTs), $lte: new Date(toTs) },
  })
    .sort({ created_at: -1 })
    .limit(limit)
    .lean();
}

export async function getAllOrderIds() {
  return await Order.find({}, "_id").lean();
}