FROM node:latest

WORKDIR /app

COPY package.json /app/
COPY package-lock.json /app/

RUN npm install

COPY src /app/src

WORKDIR /app/src

CMD ["node", "app.js"]
