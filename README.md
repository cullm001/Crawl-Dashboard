# Crawl-Dashboard

## Table of Contents
 - [Prerequisites](#prerequisites)
 - [Installation](#installation)
   - [Server](#server)
   - [Database](#database)
 - [Usage](#usage)
 - [Testing](#usage)
   - [Grafana k6](#grafana-k6)
   - [GitHub Actions](#github-actions)
## Prerequisites
1. Install [node.js and npm](https://nodejs.org/en/download/package-manager)

2. Install MySQL Server
```bash
   sudo apt install mysql-server
```
## Installation

### Server

1. Clone the repository
```bash
   git clone https://github.com/cullm001/Crawl-Dashboard.git
```
2. Navigate to project directory
```bash
   cd Crawl-Dashboard
```

3. Install dependencies
 ```bash
   npm install
```  
4. Create an .env file with following variables
```env
  USERNAME=
  HOST=
  DATABASE=
  PASSWORD=
```

### Database
1. Log in to MySQL
```bash
   mysql -u root -p
```
2. Create a Database
```bash
   CREATE DATABASE database_name;
   USE database_name;
```
3. Run SQL Script
```bash
   SOURCE Database/CrawlDatabase.sql;
```
4. Verify setup
```bash
   SHOW TABLES;
```

## Usage
1. Run the Express server
 ```bash
   node app.js
```
2. Send POST requests to the following API Endpoints
 - /api/node_info
```json
{
  "node_info": {
    "time": "2024-07-31T11:09:06.597383",
    "node_id": "node_9871",
    "cpu_usage": 32.64,
    "memory_usage": 54.11,
    "bandwidth_usage": 94.05,
    "diskspace_usage": 50.53
  }
}
```
 - /api/crawl_info
 ```json
{
  "crawl_info": {
    "crawl_id": "crawl_6863",
    "cluster_id": "user_8",
    "request_time": "2024-07-31T11:09:06.597389",
    "response_time": "2024-07-31T11:09:07.597391",
    "total_requests": 332,
    "requests_per_sec": 67,
    "concurrent_requests": 18,
    "estimated_time_to_completion": 50,
    "avg_cost_per_query": 0.87,
    "api_status_code": 404,
    "success_rate": 9.75,
    "error_rate": 71.42
  }
}
```
- /api/crawl_node
```json
{
  "crawl_node": {
    "crawl_id": "crawl_6863",
    "node_id": "node_9871"
  }
}
```

- /api/request_info
```json
{
  "request_info": {
    "time": "2024-07-31T11:09:06.597381",
    "request_id": "req_9779",
    "crawl_id": "crawl_6863",
    "proxy": "proxy_3",
    "engine": "engine_5",
    "fingerprint": "fingerprint_29"
  }
}
```
- /api/response_info
```json
{
  "response_info": {
    "time": "2024-07-31T11:09:06.597360",
    "response_id": "resp_9272",
    "request_id": "req_9779",
    "domain_name": "domain3.com",
    "website_status_code": 404,
    "is_blocked": 0,
    "bytes_downloaded": 3333,
    "download_speed": 6.22
  }
}
```
## Testing
### Grafana k6 
1. Install k6 [here](https://k6.io/docs/get-started/installation/)
2. Navigate to tests directory
```bash
cd tests
```
3. Configure API endpoint variable
```
export API_ENDPOINT= "INSERT_API_ENDPOINT"
```
4. Run the k6 script
```bash
k6 run performance.js
```
<img width="878" alt="Screen Shot 2024-08-02 at 2 00 59 AM" src="https://github.com/user-attachments/assets/5fb67f17-d62f-4f57-bc1e-9ffcb89cc611">



### GitHub Actions 
1. Navigate to the Actions tab
2. Create a new workflow
3. Configure the workflow according to [documentation](https://grafana.com/blog/2024/07/15/performance-testing-with-grafana-k6-and-github-actions/)
```yaml
name: k6 Load Test

on:
  push:
    branches:
      - '**'

jobs:
  run-test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup K6
        uses: grafana/setup-k6-action@v1
      - name: Run local k6 test
        uses: grafana/run-k6-action@v1
        with:
          path: test.js
```
4. Commit the workflow
