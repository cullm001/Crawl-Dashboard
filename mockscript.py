import json
import random
import time
import requests
from datetime import datetime, timedelta

api_endpoint = 'INSERT_ENDPOINT_HERE'  # Update this to your actual endpoint

def generate_mock_data():
    response_info = []
    request_ids = []
    for _ in range(10):
        request_id = f"req_{random.randint(1000, 9999)}"
        request_ids.append(request_id)
        response_id = f"resp_{random.randint(1000, 9999)}"
        response_info.append({
            "time": datetime.now().isoformat(),
            "response_id": response_id,
            "request_id": request_id,
            "domain_name": f"domain{random.randint(1, 10)}.com",
            "website_status_code": random.choice([200, 404, 500]),
            "bytes_downloaded": random.randint(1000, 5000),
            "js_blocked": random.choice([0, 1]),
            "download_speed": round(random.uniform(0.1, 10.0), 2)
        })

    crawl_ids = []
    request_info = []
    for request_id in request_ids:
        crawl_id = f"crawl_{random.randint(1000, 9999)}"
        crawl_ids.append(crawl_id)
        request_info.append({
            "time": datetime.now().isoformat(),
            "request_id": request_id,
            "crawl_id": crawl_id,
            "proxy": f"proxy_{random.randint(1, 5)}",
            "org_id": f"org_{random.randint(1, 5)}",
            "fingerprint": f"fingerprint_{random.randint(1, 100)}"
        })

    node_ids = []
    node_info = []
    for _ in range(5):
        node_id = f"node_{random.randint(1000, 9999)}"
        node_ids.append(node_id)
        node_info.append({
            "time": datetime.now().isoformat(),
            "node_id": node_id,
            "cpu_usage": round(random.uniform(0, 100), 2),
            "memory_usage": round(random.uniform(0, 100), 2),
            "bandwidth_usage": round(random.uniform(0, 100), 2),
            "diskspace_usage": round(random.uniform(0, 100), 2)
        })

    crawl_node = []
    for crawl_id in crawl_ids:
        node_id = random.choice(node_ids)
        crawl_node.append({
            "crawl_id": crawl_id,
            "node_id": node_id
        })

    crawl_info = []
    for crawl_id in crawl_ids:
        crawl_info.append({
            "crawl_id": crawl_id,
            "user_id": f"user_{random.randint(1, 10)}",
            "request_time": datetime.now().isoformat(),
            "response_time": (datetime.now() + timedelta(seconds=random.randint(1, 5))).isoformat(),
            "requests_per_sec": random.randint(1, 100),
            "concurrent_requests": random.randint(1, 50),
            "total_requests": random.randint(100, 1000),
            "avg_cost_per_query": round(random.uniform(0.01, 1.00), 2),
            "estimated_time_to_completion": random.randint(1, 120),
            "api_status_code": random.choice([200, 404, 500]),
            "success_rate": round(random.uniform(0, 100), 2),
            "error_rate": round(random.uniform(0, 100), 2)
        })

    data = {
        "response_info": response_info,
        "request_info": request_info,
        "node_info": node_info,
        "crawl_node": crawl_node,
        "crawl_info": crawl_info
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
    time.sleep(.5)
