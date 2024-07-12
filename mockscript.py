import json
import random
import time
import requests
from datetime import datetime, timedelta

api_endpoint = 'INSERT_ENDPOINT_HERE'

def generate_mock_data():
    customers = [
        {"api_key": "cust123", "customer_name": "Customer A", "contact_email": "contactA@example.com", "created_at": "2024-06-25T12:00:00"},
        {"api_key": "cust456", "customer_name": "Customer B", "contact_email": "contactB@example.com", "created_at": "2024-06-26T12:00:00"}
    ]

    nodes = [
        {"node_id": 1, "node_name": "Node A", "created_at": "2024-06-25T12:00:00"},
        {"node_id": 2, "node_name": "Node B", "created_at": "2024-06-26T12:00:00"}
    ]

    node_metrics = []
    crawl_metrics = []

    for _ in range(10):  
        node_id = random.choice([1, 2])
        customer = random.choice(customers)
        
        metric_time = datetime.now().isoformat()
        cpu_usage = round(random.uniform(50, 80), 2)
        memory_usage = round(random.uniform(50, 80), 2)
        bandwidth_usage = round(random.uniform(20, 60), 2)
        disk_space_usage = round(random.uniform(20, 60), 2)

        node_metric = {
            "id": random.randint(1, 1000),
            "node_id": node_id,
            "metric_time": metric_time,
            "cpu_usage": cpu_usage,
            "memory_usage": memory_usage,
            "bandwidth_usage": bandwidth_usage,
            "disk_space_usage": disk_space_usage
        }
        node_metrics.append(node_metric)

        request_time = datetime.now().isoformat()
        response_time = random.randint(50, 500)
        concurrent_requests = random.randint(1, 100)
        total_requests = random.randint(1, 1000)
        requests_per_second = random.randint(1, 10)
        estimated_time_to_completion = random.randint(1, 120)
        average_cost_per_query = round(random.uniform(0.01, 0.05), 2)
        bytes_downloaded = random.randint(1000000, 5000000)
        api_status_code = random.choice([200, 404, 500])
        success_rate = round(random.uniform(95, 100), 2)
        error_rate = 100 - success_rate
        parameter_usage = random.choice(["proxy1", "proxy2"])
        website_status_code = random.choice([200, 404, 500])

        crawl_metric = {
            "id": random.randint(1, 1000),
            "request_time": request_time,
            "response_time": response_time,
            "concurrent_requests": concurrent_requests,
            "total_requests": total_requests,
            "requests_per_second": requests_per_second,
            "estimated_time_to_completion": estimated_time_to_completion,
            "average_cost_per_query": average_cost_per_query,
            "bytes_downloaded": bytes_downloaded,
            "api_status_code": api_status_code,
            "success_rate": success_rate,
            "error_rate": error_rate,
            "parameter_usage": parameter_usage,
            "website_status_code": website_status_code,
            "customer_api_key": customer["api_key"],
            "node_cpu_usage": cpu_usage,
            "node_memory_usage": memory_usage,
            "node_bandwidth_usage": bandwidth_usage,
            "node_disk_space_usage": disk_space_usage
        }
        crawl_metrics.append(crawl_metric)

    data = {
        "customers": customers,
        "nodes": nodes,
        "node_metrics": node_metrics,
        "crawl_metrics": crawl_metrics
    }

    return data

def send_data_to_api(data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_endpoint, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        print('Data sent successfully.')
    else:
        print('Failed to send data. Status code:', response.status_code)

while True:
    mock_data = generate_mock_data()
    send_data_to_api(mock_data)
    time.sleep(10)  
