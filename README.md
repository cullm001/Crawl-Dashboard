# Crawl-Dashboard

## Installation
1. Clone the repository
```bash
   git clone https://github.com/cullm001/Crawl-Dashboard.git
```
2. Navigate to project directory
```bash
   cd Crawl-Dashboard
```
3. Install [node.js](https://nodejs.org/en/download/package-manager)

4. Install dependencies
 ```bash
   npm install
```  
5. Create an .env file with following variables
```env
  USERNAME=
  HOST=
  DATABASE=
  PASSWORD=
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
    "time": "2024-07-30T11:42:04",
    "node_id": "node_9099",
    "cpu_usage": 85.09,
    "memory_usage": 48.81,
    "bandwidth_usage": 76.19,
    "diskspace_usage": 54.06
  }
}
```

## Database Setup
1. Install MySQL Server
```bash
   sudo apt install mysql-server
```
2. Log in to MySQL
```bash
   mysql -u root -p
```
3. Create a Database
```bash
   CREATE DATABASE database_name;
   USE database_name;
```
4. Run SQL Script
```bash
   SOURCE Database/CrawlDatabase.sql;
```
5. Verify setup
```bash
   SHOW TABLES;
```


