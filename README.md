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
    "time": "2024-07-30T11:42:04",
    "node_id": "node_9099",
    "cpu_usage": 85.09,
    "memory_usage": 48.81,
    "bandwidth_usage": 76.19,
    "diskspace_usage": 54.06
  }
}
```

