const express = require('express');

module.exports = (pool) => {
  const router = express.Router();

  router.post('/insert-crawl-info', (req, res) => {

    // INSERT INTO crawl_info
    const crawl_info = req.body.crawlinfo[0];
    const crawl_query = "INSERT INTO crawl_info (crawl_id, cluster_id, request_time, response_time, total_requests, requests_per_sec, concurrent_requests, estimated_time_to_complete, avg_cost_per_query, api_status_code, success_rate, error_rate) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

    pool.query(crawl_query, [
      crawl_info.crawl_id, crawl_info.cluster_id, crawl_info.request_time, crawl_info.response_time, crawl_info.total_requests, crawl_info.requests_per_sec, crawl_info.concurrent_requests, crawl_info.estimated_time_to_complete, crawl_info.avg_cost_per_query, crawl_info.api_status_code, crawl_info.success_rate, crawl_info.error_rate], (err, crawlResult) => {
      if (err) {
        console.error('Error inserting into crawl_info:', err);
        res.status(500).send('Error inserting crawl_info');
        return;
      }
      console.log("Inserted into crawl_info successfully");

      console.log("")
      res.send('CrawlInfo Inserted Successfully');
    });
  });
  return router;
};
