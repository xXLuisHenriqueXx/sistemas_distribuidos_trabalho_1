import mongoose from "mongoose";

const postSchema = new mongoose.Schema({
  user_id: Number,
  title: String,
  content: String,
  created_at: { type: Date, default: Date.now },
});

const Post = mongoose.model("Post", postSchema);

export async function createMongoConnection() {
  const uri = `mongodb://${process.env.MONGO_HOST || "mongo"}:27017/${
    process.env.DB_NAME || "testdb"
  }`;
  await mongoose.connect(uri);

  return Post;
}

export async function insertPost(Post, { user_id, title, content }) {
  return await Post.create({ user_id, title, content });
}

export async function getPostById(Post, id) {
  return await Post.findById(id);
}
