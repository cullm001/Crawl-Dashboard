# Crawl-Dashboard

### Aggregate Statistics
![image](https://github.com/user-attachments/assets/8697304e-2f5f-42dc-bea1-e6427702c6c4)
### Crawl Statistics
![image](https://github.com/user-attachments/assets/84e0a45e-bbce-4edc-b3cb-e81f855ae7af)
### Cluster Statiscs
![image](https://github.com/user-attachments/assets/a4773226-4d55-438e-9967-6ae64c03ce3f)
### Response Times across Domains
![image](https://github.com/user-attachments/assets/a9ffe184-66a7-42bc-9775-81ee722675f9)

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

### Grafana
#### Install Grafana on Windows Desktop
1. Go to [Grafana Install Page](https://grafana.com/docs/grafana/latest/setup-grafana/installation/)

2. Click on `Windows`

3. Navigate to Grafana download page

4. Choose `OSS` under edition for open source

5. Download and run installer choosing all default options

6. Navigate to C:\\'Program Files'\GrafanaLabs\grafana\bin

7. Run `grafana-server` application

8. Now open `localhost:3000` in a browser

9. Type in `admin` for username and password

10. Update password

#### Or Install Grafana on Another Platform
1. Go to [Grafana Install Page](https://grafana.com/docs/grafana/latest/setup-grafana/installation/)

2. Find your chosen platform and click link to tutorial for grafana installation

3. Follow tutorial and make sure to choose Grafana OSS edition

4. After install open `localhost:3000` in a browser

5. Enter `admin` for both username and password

6. Update password

#### Set up Database Connection
1. Open menu using the hamburger button in the top left corner of Grafana

2. Go to Connections drop down and choose `Data Sources`

3. Click on `Add new data source` and choose MySQL

4. Choose a name for the new Data Source

5. Under `Connection` enter the IP address of the database in `Host URL` and name of the databse in `Database name`

6. Under `Authentication` enter the username and password chosen when setting up the database

7. Scroll all the way down and click on `Save & test` to verify database is accessible

#### Set up Dashboard
1. Open menu using the hamburger button in the top left corner of Grafana

2. Go to `Dashboards`

3. Click on `New` drop down menu in the top right corner and choose `Import`

4. Upload JSON file found at grafana/crawling-dashboard.json

5. Update Dashboard name if necessary

6. Scroll down to `Select a MySQL data source` and choose the new Data Source

7. Scroll down to the bottom and click `Import`

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

### Dashboard Layout

![image](https://github.com/user-attachments/assets/b1cd0b13-bf16-425f-85bb-444cdcf02acf)

**1.** Drop down arrow to hide Grafana's topmost navigation bar
  * Bar is currently hidden in the picture
     
**2.** Kiosk mode button to hide top bar in the picture
  * Press ESC to exit kiosk mode
     
**3.** Drop down menu to set the Dashboard refresh rate
   
**4.** Drop down menu to choose Dashboard time range
   
**5.** `Crawls` variable can be used to repeat Crawl rows
  * The picture above shows a single crawl `crawl_1` chosen under the variable `Crawls`
   
**6.** `Clusters` variable can be used to repeat Cluster rows
    
**7.** `Domains` variable is used to repeat Concurrent Requests vs Response Time for each domain visited
  * Above picture shows all the options currently available for the Domain, with the All value being selected
    
**8.** Aggegrate row shows total gigabytes downloaded for each proxy and the average cost

**9.** Concurrent Request vs Response Time row contains a bar graph that repeats for every domain name chosen in the Domains variable
  * The bar graph displays number of concurrent requests on the x-axis and the last response time for that domain on the y-axis
     
**10.** Cluster drop down row repeats for every cluster chosen in the `Clusters` variable
   * Each cluster row will contain an average cpu, memory, storage, and bandwidth usage for the nodes within the cluster
      
**11.** Crawl drop down row repeats for every crawl chosen in the `Crawls` variable
   * Each crawl row has requests remaining, requests per second, cost, time remaining, gigabytes downloaded, error rate, blocked requests, api status code, and concurrent requests metrics
   * Each crawl row also contains a bar graph to display a count of each http status code received and a line graph to show the download speed over time
   
Any time there is a new crawl, the browser must be refreshed to query for the new `Crawls` `Clusters` and `Domains` variable values

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
