const express = require('express');

module.exports = (pool) => {
  const router = express.Router();

  router.post('/insert-info', (req, res) => {

    
    // INSERT INTO response_info
    const response_info = req.body.responseinfo[0];
    const response_query = "INSERT INTO response_info (time, response_id, request_id, crawl_id, domain_name, website_status_code, is_blocked, bytes_downloaded, download_speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)";

    pool.query(response_query, [
      response_info.time, response_info.response_id, response_info.request_id, response_info.crawl_id, response_info.domain_name, response_info.website_status_code, response_info.is_blocked, response_info.bytes_downloaded, response_info.download_speed], (err, responseResult) => {
      if (err) {
        console.error('Error inserting into response_info:', err);
        res.status(500).send('Error inserting response_info');
        return;
      }
      console.log("Inserted into response_info successfully");

      // INSERT INTO request_info
      const request_info = req.body.requestinfo[0];
      const request_query = "INSERT INTO request_info (time, request_id, crawl_id, proxy, engine, fingerprint) VALUES (?, ?, ?, ?, ?, ?)";

      pool.query(request_query, [
        request_info.time, request_info.request_id, request_info.crawl_id, request_info.proxy, request_info.engine, request_info.fingerprint], (err, requestResult) => {
        if (err) {
          console.error('Error inserting into request_info:', err);
          res.status(500).send('Error inserting request_info');
          return;
        }
        console.log("Inserted into request_info successfully");


        // INSERT INTO node_info
        const node_info = req.body.nodeinfo[0];
        const node_query = "INSERT INTO node_info (time, node_id, cpu_usage, memory_usage, bandwidth_usage, diskspace_usage) VALUES (?, ?, ?, ?, ?, ?)";

        pool.query(node_query, [
          node_info.time, node_info.node_id, node_info.cpu_usage, node_info.memory_usage, node_info.bandwidth_usage, node_info.diskspace_usage], (err, nodeResult) => {
          if (err) {
            console.error('Error inserting into node_info:', err);
            res.status(500).send('Error inserting node_info');
            return;
          }
          console.log("Inserted into node_info successfully");

          console.log("")
          res.send('Data Inserted Successfully');
          });
      });
    });
  });
  return router;
};
