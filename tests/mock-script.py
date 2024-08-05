#!/usr/bin/env python3

import json
import random
import time
import requests
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock, Event

api_endpoint = 'API_ENDPOINT'

total_requests_counter = 0
successful_requests = 0
lock = Lock()
stop_event = Event()

def generate_and_send_data():
    global total_requests_counter
    global successful_requests

    node_id = f"node_{random.randint(1000, 9999)}"
    node_info = {
        "time": datetime.now().isoformat(),
        "node_id": node_id,
        "cpu_usage": round(random.uniform(0, 100), 2),
        "memory_usage": round(random.uniform(0, 100), 2),
        "bandwidth_usage": round(random.uniform(0, 100), 2),
        "diskspace_usage": round(random.uniform(0, 100), 2)
    }

    data = {"node_info": node_info}

    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_endpoint, data=json.dumps(data), headers=headers)
    with lock:
        total_requests_counter += 1
        if response.status_code == 200:
            successful_requests +=1


def count_requests_for_one_second():
    global total_requests_counter
    start_time = time.time()
    while time.time() - start_time < 1:
        time.sleep(0.01) 
    with lock:
        print(f"Total requests in one second: {total_requests_counter}")
        print(f"Successful requests: {successful_requests}")
    stop_event.set()

if __name__ == "__main__":
    ThreadPoolExecutor(max_workers=1).submit(count_requests_for_one_second)
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(generate_and_send_data) for _ in range(1000)]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as exc:
                print(f'Generated an exception: {exc}')
