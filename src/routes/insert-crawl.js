const express = require('express');

module.exports = (pool) => {
  const router = express.Router();

  router.post('/node_info', (req, res) => {
    const node_info_query = "INSERT INTO node_info (time,  node_id, cpu_usage, memory_usage, bandwidth_usage, diskspace_usage, crawl_id) VALUES ( ?, ?, ?, ?, ?, ?, ?)";
    pool.query(node_info_query, [req.body.time, req.body.node_id, req.body.cpu_usage, req.body.memory_usage, req.body.bandwidth_usage, req.body.diskspace_usage, req.body.crawl_id], (err, nodeResult) => {
      if (err) {
        console.error('Error inserting into node_info:', err);
        res.status(500).send('Error inserting node_info');
        return;
      }
    res.send("node_info inserted successfully");
    });
  });

  router.post('/crawl_info', (req, res) => {
    const crawl_info_query = "INSERT INTO crawl_info (crawl_id, cluster_id, total_requests, requests_per_sec, concurrent_requests, api_status_code, cost, domain_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
    pool.query(crawl_info_query, [req.body.crawl_id, req.body.cluster_id, req.body.total_requests, req.body.requests_per_sec, req.body.concurrent_requests, req.body.api_status_code, req.body.cost, req.body.domain_name], (err, crawlResult) => {
      if (err) {
        console.error('Error inserting into crawl_info:', err);
        res.status(500).send('Error inserting crawl_info');
        return;
      }
      res.send("crawl_info inserted successfully");
    });
  });


  router.post('/request_info', (req, res) => {
    const request_info_query = "INSERT INTO request_info (time, request_id, crawl_id, proxy, engine, fingerprint) VALUES (?, ?, ?, ?, ?, ?)";
    pool.query(request_info_query, [
      req.body.time, req.body.request_id, req.body.crawl_id, req.body.proxy, req.body.engine, req.body.fingerprint], (err, requestResult) => {
      if (err) {
        console.error('Error inserting into request_info:', err);
        res.status(500).send('Error inserting request_info');
        return;
      }
      res.send("request_info inserted successfully");
    });
  });

  router.post('/response_info', (req, res) => {
    const response_info_query = "INSERT INTO response_info (time, response_id, request_id, crawl_id, web_status_code, is_blocked, bytes_downloaded, download_speed, response_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)";
    pool.query(response_info_query, [
      req.body.time, req.body.response_id, req.body.request_id, req.body.crawl_id, req.body.web_status_code, req.body.is_blocked, req.body.bytes_downloaded, req.body.download_speed, req.body.response_time], (err, responseResult) => {
      if (err) {
        console.error('Error inserting into response_info:', err);
        res.status(500).send('Error inserting response_info');
        return;
      }

      res.send("response_info inserted successfully");
    });
  });

  return router;
};
    