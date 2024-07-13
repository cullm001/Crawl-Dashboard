const express = require('express');
const dotenv = require('dotenv');
const mysql = require('mysql2');
const bodyParser = require('body-parser');

dotenv.config();
const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

const pool = mysql.createPool({
  host: process.env.HOST,
  user: process.env.USERNAME,
  password: process.env.PASSWORD,
  database: process.env.DATABASE,
  connectionLimit: 5
});

app.post('/', (req, res) => {

  const customer_data = req.body.customer_data[0];
  const crawl_data = req.body.crawl_data[0];
  const node_metrics_data = req.body.node_metrics_data[0];
  const node_data = req.body.node_data[0];

  // INSERT INTO customer_data
  const customer_query = `
    INSERT INTO customer_data (api_key, customer_name, contact_email, created_at) 
    VALUES (?, ?, ?, ?)
  `;
  pool.query(customer_query, [
    customer_data.api_key, customer_data.customer_name, customer_data.contact_email, customer_data.created_at
  ], (err, customerResult) => {
    if (err) {
      console.error('Error inserting into customer_data:', err);
      res.status(500).send('Error occurred');
      return;
    }

    // INSERT INTO crawl_data
    const crawl_query = `
      INSERT INTO crawl_data (id, request_time, response_time, concurrent_requests, total_requests, requests_per_second, estimated_time_to_completion, average_cost_per_query, bytes_downloaded, api_status_code, success_rate, error_rate, parameter_usage, website_status_code, customer_api_key, node_cpu_usage, node_memory_usage, node_bandwidth_usage, node_disk_space_usage) 
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `;
    pool.query(crawl_query, [
      crawl_data.id, crawl_data.request_time, crawl_data.response_time, crawl_data.concurrent_requests, crawl_data.total_requests, crawl_data.requests_per_second, crawl_data.estimated_time_to_completion, crawl_data.average_cost_per_query, crawl_data.bytes_downloaded, crawl_data.api_status_code, crawl_data.success_rate, crawl_data.error_rate, crawl_data.parameter_usage, crawl_data.website_status_code, crawl_data.customer_api_key, crawl_data.node_cpu_usage, crawl_data.node_memory_usage, crawl_data.node_bandwidth_usage, crawl_data.node_disk_space_usage
    ], (err, crawlResult) => {
      if (err) {
        console.error('Error inserting into crawl_data:', err);
        res.status(500).send('Error occurred');
        return;
      }

      // INSERT INTO node_data
      const node_query = `
        INSERT INTO node_data (node_id, node_name, created_at) 
        VALUES (?, ?, ?)
      `;
      pool.query(node_query, [
        node_data.node_id, node_data.node_name, node_data.created_at
      ], (err, nodeResult) => {
        if (err) {
          console.error('Error inserting into node_data:', err);
          res.status(500).send('Error occurred');
          return;
        }

        // INSERT INTO node_metrics_data
        const node_metrics_query = `
          INSERT INTO node_metrics_data (id, node_id, metric_time, cpu_usage, memory_usage, bandwidth_usage, disk_space_usage) 
          VALUES (?, ?, ?, ?, ?, ?, ?)
        `;
        pool.query(node_metrics_query, [
          node_metrics_data.id, node_metrics_data.node_id, node_metrics_data.metric_time, node_metrics_data.cpu_usage, node_metrics_data.memory_usage, node_metrics_data.bandwidth_usage, node_metrics_data.disk_space_usage
        ], (err, nodeMetricsResult) => {
          if (err) {
            console.error('Error inserting into node_metrics_data:', err);
            res.status(500).send('Error occurred');
            return;
          }

          res.send('Data Inserted Successfully');
        });
      });
    });
  });
});


app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
