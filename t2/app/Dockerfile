FROM node:20-slim

WORKDIR /app

COPY package*.json ./

RUN apt-get update && \
    apt-get install -y docker.io && \
    rm -rf /var/lib/apt/lists/*

RUN npm install

COPY . .

CMD ["node", "server.js"]