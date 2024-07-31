# Crawl-Dashboard

## Table of Contents
 - [Prerequisites](#prerequisites)
 - [Installation](#installation)
   - [Server](#server)
   - [Database](#database)
 - [Usage](#usage)
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
