const express = require('express');

module.exports = (pool) => {
  const router = express.Router();

  router.get('/customer_data', (req, res) => {
    const query = 'SELECT * FROM customer_data';
    pool.query(query, (err, results) => {
      if (err) {
        console.error('Error fetching customer_data:', err);
        res.status(500).send('Error fetching website_data');
        return;
      }
      res.json(results);
    });
  });

  router.get('/node_data', (req, res) => {
    const query = 'SELECT * FROM node_data';
    pool.query(query, (err, results) => {
      if (err) {
        console.error('Error fetching node_data:', err);
        res.status(500).send('Error fetching node_data');
        return;
      }
      res.json(results);
    });
  });

  router.get('/node_metrics_data', (req, res) => {
    const query = 'SELECT * FROM node_metrics_data';
    pool.query(query, (err, results) => {
      if (err) {
        console.error('Error fetching node_metrics_data:', err);
        res.status(500).send('Error fetching node_metrics_data');
        return;
      }
      res.json(results);
    });
  });

  router.get('/crawl_data', (req, res) => {
    const query = 'SELECT * FROM crawl_data';
    pool.query(query, (err, results) => {
      if (err) {
        console.error('Error fetching crawl_data:', err);
        res.status(500).send('Error fetching crawl_data');
        return;
      }
      res.json(results);
    });
  });

  return router;
};