# Crawl-Dashboard

## Database Setup
1. Install MySQL Server
```bash
   sudo apt install mysql-server
```
2. Log in to MySQL
```bash
   mysql -u 'username' -p
```
3. Download / Copy MySQL script
[Setup Script](Database/CrawlDatabase.sql)

4. Change ' "REPLACE WITH DATABASE NAME" ' section with desired database name

6. Paste script into MySQL command line interface

6. Verify setup
```bash
   SHOW DATABASES;
```
```bash
   USE 'database_name';
```
```bash
   SHOW TABLES;
```

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
   npm app.js
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

