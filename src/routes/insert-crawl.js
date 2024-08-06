const express = require('express');

module.exports = (pool) => {
  const router = express.Router();

  router.post('/node_info', (req, res) => {
    const node_info = req.body.node_info;
    const node_info_query = "INSERT INTO node_info (time,  node_id, cpu_usage, memory_usage, bandwidth_usage, diskspace_usage, crawl_id) VALUES ( ?, ?, ?, ?, ?, ?, ?)";
    pool.query(node_info_query, [node_info.time, node_info.node_id, node_info.cpu_usage, node_info.memory_usage, node_info.bandwidth_usage, node_info.diskspace_usage, node_info.crawl_id], (err, nodeResult) => {
      if (err) {
        console.error('Error inserting into node_info:', err);
        res.status(500).send('Error inserting node_info');
        return;
      }
    res.send("node_info inserted successfully");
    });
  });

  router.post('/crawl_info', (req, res) => {
    const crawl_info = req.body.crawl_info;
    const crawl_info_query = "INSERT INTO crawl_info (crawl_id, cluster_id, total_requests, requests_per_sec, concurrent_requests, api_status_code, cost, domain_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
    pool.query(crawl_info_query, [crawl_info.crawl_id, crawl_info.cluster_id, crawl_info.total_requests, crawl_info.requests_per_sec, crawl_info.concurrent_requests, crawl_info.api_status_code, crawl_info.cost, crawl_info.domain_name], (err, result) => {
      if (err) {
        console.error('Error inserting into crawl_info:', err);
        res.status(500).send('Error inserting crawl_info');
        return;
      }
      res.send("crawl_info inserted successfully");
    });
  });


  router.post('/request_info', (req, res) => {
    const request_info = req.body.request_info;
    const request_info_query = "INSERT INTO request_info (time, request_id, crawl_id, proxy, engine, fingerprint) VALUES (?, ?, ?, ?, ?, ?)";
    pool.query(request_info_query, [
      request_info.time, request_info.request_id, request_info.crawl_id, request_info.proxy, request_info.engine, request_info.fingerprint], (err, requestResult) => {
      if (err) {
        console.error('Error inserting into request_info:', err);
        res.status(500).send('Error inserting request_info');
        return;
      }
      res.send("request_info inserted successfully");
    });
  });

  router.post('/response_info', (req, res) => {
    const response_info = req.body.response_info;
    const response_info_query = "INSERT INTO response_info (time, response_id, request_id, crawl_id, web_status_code, is_blocked, bytes_downloaded, download_speed, response_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)";
    pool.query(response_info_query, [
      response_info.time, response_info.response_id, response_info.request_id, response_info.crawl_id, response_info.web_status_code, response_info.is_blocked, response_info.bytes_downloaded, response_info.download_speed, response_info.response_time], (err, responseResult) => {
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
    