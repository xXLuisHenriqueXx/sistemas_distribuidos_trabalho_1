import mongoose from "mongoose";

// --- SCHEMA ATUALIZADO ---
// Reflete a estrutura desnormalizada do seed.js
const postSchema = new mongoose.Schema({
  author: {
    user_id: Number,
    username: String,
    email: String,
  },
  title: String,
  content: String,
  created_at: { type: Date, default: Date.now },
});

// Define o modelo
const Post = mongoose.model("Post", postSchema);

export async function createMongoConnection() {
  const uri = `mongodb://${process.env.MONGO_HOST || "mongo"}:27017/${
    process.env.DB_NAME || "testdb"
  }`;
  await mongoose.connect(uri);

  // Retorna o modelo compilado
  return Post;
}

// --- FUNÇÃO ATUALIZADA ---
// Recebe o payload desnormalizado do server.js
export async function insertPost(Post, { author, title, content, created_at }) {
  return await Post.create({ author, title, content, created_at });
}

// --- FUNÇÃO ATUALIZADA ---
// Busca apenas pelo _id nativo do Mongo
export async function getPostById(Post, id) {
  try {
    // findById é otimizado para buscar pelo _id
    return await Post.findById(id);
  } catch (error) {
    // Se o ID for um formato inválido, retorna nulo
    return null;
  }
}

// --- FUNÇÃO ADICIONADA ---
export async function getPostsByUserId(Post, uid) {
  const numericId = parseInt(uid, 10);
  if (isNaN(numericId)) return [];

  // Busca pelo campo aninhado "author.user_id"
  // O índice criado no seed.js vai acelerar isso
  return await Post.find({ "author.user_id": numericId })
    .sort({ created_at: -1 })
    .limit(50); // Mesmo limit do Postgres para uma comparação justa
}

// --- NOVA FUNÇÃO PARA O LOADTESTER ---
export async function getAllPostIds(Post) {
  // Busca todos os documentos, retornando apenas o campo _id
  return await Post.find({}, '_id');
}