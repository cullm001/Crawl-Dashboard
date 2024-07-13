const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

const dotenv = require('dotenv');
dotenv.config();

const mysql = require('mysql2');
const bodyParser = require('body-parser');
app.use(bodyParser.json());

const pool = mysql.createPool({
  host: process.env.HOST,
  user: process.env.USERNAME,
  password: process.env.PASSWORD,
  database: process.env.DATABASE,
  connectionLimit: 5
});

const insertCrawlRouter = require('./routes/insert-crawl');
app.use(insertCrawlRouter(pool)); 

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
