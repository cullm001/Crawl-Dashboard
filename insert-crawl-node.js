const express = require('express');

module.exports = (pool) => {
  const router = express.Router();

  router.post('/insert-crawl-node', (req, res) => {

    // INSERT INTO crawl_node
    const crawl_node = req.body.crawlnode[0];
    const crawl_node_query = "INSERT INTO crawl_node (crawl_id, node_id) VALUES (?, ?)";

    pool.query(crawl_node_query, [crawl_node.crawl_id, crawl_node.node_id], (err, crawl_nodeResult) => {
      if (err) {
        console.error('Error inserting into crawl_node:', err);
        res.status(500).send('Error inserting crawl_node');
        return;
      }
      console.log("Inserted into crawl_node successfully");
      
      console.log("")
      res.send('Data Inserted Successfully');  
    });
  });
  return router;
};
