const express = require('express');

module.exports = (pool) => {
  const router = express.Router();

  router.post('/insert-crawl', (req, res) => {

    //Parses JSON for tabel data
     const node_info = req.body.node_info[0];
     const crawl_info = req.body.crawl_info[0];
     const request_info = req.body.request_info[0];
     const response_info = req.body.response_info[0];
    
    // INSERT node_info table
    const node_info_query = "INSERT INTO node_info (time, node_id, cpu_usage, memory_usage, bandwidth_usage, diskspace_usage) VALUES (?, ?, ?, ?, ?, ?)";
    pool.query(node_info_query, [node_info.time, node_info.node_id, node_info.cpu_usage, node_info.memory_usage, node_info.bandwidth_usage, node_info.diskspace_usage], (err, nodeResult) => {
       if (err) {
         console.error('Error inserting into node_info:', err);
         res.status(500).send('Error inserting node_info');
         return;
       }
        console.log("Inserted into node_info successfully");


      // INSERT crawl_info table
      const crawl_info_query = "INSERT INTO crawl_info (crawl_id, cluster_id, request_time, response_time, total_requests, requests_per_sec, concurrent_requests, estimated_time_to_complete, avg_cost_per_query, api_status_code, success_rate, error_rate) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
      pool.query(crawl_info_query, [crawl_info.crawl_id, crawl_info.cluster_id, crawl_info.request_time, crawl_info.response_time, crawl_info.total_requests, crawl_info.requests_per_sec, crawl_info.concurrent_requests, crawl_info.estiamted_time_to_complete, crawl_info.avg_cost_per_query, crawl_info.api_status_code, crawl_info.success_rate, crawl_info.error_rate], (err, nodeMetricsResult) => {
        if (err) {
          console.error('Error inserting into crawl_info:', err);
          res.status(500).send('Error inserting crawl_info');
          return;
        }
        console.log("Inserted into crawl_info successfully"); 


        //INSERT crawl_node table
        const crawl_node_query = "INSERT INTO crawl_node (crawl_id, node_id) VALUES (?, ?)";
        pool.query(crawl_node_query, [crawl_info.crawl_id, node_info.node_id], (err, crawlNodeResult) => {
          if (err) {
            console.error('Error inserting into crawl_node:', err);
            res.status(500).send('Error inserting crawl_node');
            return;
          }
          console.log("Inserted into crawl_node successfully");


          // INSERT request_info table
          const request_info_query = "INSERT INTO request_info (time, request_id, crawl_id, proxy, engine, fingerprint) VALUES (?, ?, ?, ?, ?, ?)";
          pool.query(request_info_query, [
            request_info.time, request_info.request_id, request_info.crawl_id, request_info.proxy, request_info.engine, request_info.fingerprint], (err, requestResult) => {
            if (err) {
              console.error('Error inserting into response_info:', err);
              res.status(500).send('Error inserting response_info');
              return;
            }
            console.log("Inserted into request_info successfully")

            // INSERT response_info table
            const response_info_query = "INSERT INTO response_info (time, response_id, request_id, domain_name, website_status_code, is_blocked, bytes_downloaded, download_speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
            pool.query(response_info_query, [
              response_info.time, response_info.response_id, response_info.request_id, response_info.domain_name, response_info.website_status_code, response_info.is_blocked, response_info.bytes_downloaded, response_info.download_speed], (err, responseResult) => {
              if (err) {
                console.error('Error inserting into response_info:', err);
                res.status(500).send('Error inserting response_info');
                return;
              }
              console.log("Inserted into response_info successfully");

              console.log("")
              res.send('Data Inserted Successfully');
            });
          });
        });
      });
    });
  });

  return router;
};
