import json
import random
import time
import requests
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed

api_endpoint = 'INSERT_ENDPOINT_HERE' 

def generate_mock_data():
    # Generate unique identifiers once
    crawl_id = f"crawl_{random.randint(1000, 9999)}"
    user_id = f"user_{random.randint(1, 10)}"
    node_ids = [f"node_{random.randint(1000, 9999)}" for _ in range(5)]
    request_ids = [f"req_{random.randint(1000, 9999)}" for _ in range(10)]
    response_ids = [f"resp_{random.randint(1000, 9999)}" for _ in range(10)]
    org_id = f"org_{random.randint(1, 5)}"
    proxy = f"proxy_{random.randint(1, 5)}"

    response_info = []
    for response_id, request_id in zip(response_ids, request_ids):
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

    request_info = []
    for request_id in request_ids:
        request_info.append({
            "time": datetime.now().isoformat(),
            "request_id": request_id,
            "crawl_id": crawl_id,
            "proxy": proxy,
            "org_id": org_id,
            "fingerprint": f"fingerprint_{random.randint(1, 100)}"
        })

    node_info = []
    for node_id in node_ids:
        node_info.append({
            "time": datetime.now().isoformat(),
            "node_id": node_id,
            "cpu_usage": round(random.uniform(0, 100), 2),
            "memory_usage": round(random.uniform(0, 100), 2),
            "bandwidth_usage": round(random.uniform(0, 100), 2),
            "diskspace_usage": round(random.uniform(0, 100), 2)
        })

    crawl_node = []
    for node_id in node_ids:
        crawl_node.append({
            "crawl_id": crawl_id,
            "node_id": node_id
        })

    crawl_info = {
        "crawl_id": crawl_id,
        "user_id": user_id,
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
    }

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

def generate_and_send_data():
    mock_data = generate_mock_data()
    send_data_to_api(mock_data)

if __name__ == "__main__":
    while True:
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(generate_and_send_data) for _ in range(5)]
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as exc:
                    print(f'Generated an exception: {exc}')
            time.sleep(.5)
