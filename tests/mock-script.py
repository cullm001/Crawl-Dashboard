

import json
import random
import time
import requests
from datetime import datetime,  timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock, Event



crawl_info_endpoint = 
crawl_node_endpoint = 
response_info_endpoint = 
request_info_endpoint = 
node_info_endpoint = 

session = requests.Session()

crawl_num = 1

def send_data_to_api(data, api_endpoint):
    headers = {'Content-Type': 'application/json'}
    print(f"Sending data to {api_endpoint}: {json.dumps(data, indent=2)}")
    response = session.post(api_endpoint, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        print(f'Data sent successfully to {api_endpoint}.')
        return True
    elif response.status_code == 409:  
        print(f'Duplicate entry detected for {api_endpoint}. Skipping insertion.')
        return False
    else:
        print(f'Failed to send data to {api_endpoint}. Status code: {response.status_code}')
        print(f'Response text: {response.text}') 
        return False


def generate_node_info(crawl_id, node_id):
    node_info = {
        "time": datetime.utcnow().isoformat(),
        "node_id": node_id,
        "cpu_usage": round(random.uniform(0, 100), 2),
        "memory_usage": round(random.uniform(0, 100), 2),
        "bandwidth_usage": round(random.uniform(0, 100), 2),
        "diskspace_usage": round(random.uniform(0, 100), 2),
        "crawl_id": crawl_id
    }

    return node_info



def generate_crawl_info(crawl_id):
    crawl_info = {
            "crawl_id": crawl_id,
            "cluster_id": random.choice(["cluster_1", "cluster_2", "cluster_3"]),
            "total_requests": random.randint(100, 1000),
            "requests_per_sec": random.randint(1, 100),
            "concurrent_requests": random.randint(1, 50),
            "api_status_code": random.choice([200, 404, 500]),
            "cost": random.randint(0,100),
            "domain_name": f"domain{random.randint(1, 10)}.com"
        }
    return crawl_info

    
request_id_counter = 0
def generate_request_info(crawl_id):
    global request_id_counter
    request_id = f'{crawl_num}-{request_id_counter}'
    request_id_counter += 1

    return request_id, {
        "time": datetime.utcnow().isoformat(),
        "request_id": request_id,
        "crawl_id": crawl_id,
        "proxy": f"proxy_{random.randint(1, 5)}",
        "engine": f"engine_{random.randint(1, 5)}",
        "fingerprint": f"fingerprint_{random.randint(1, 100)}"
    }


response_id_counter = 0
def generate_response_info(request_id, crawl_id):
    global response_id_counter
    response_id = f'{crawl_num}-{response_id_counter}'
    response_id_counter += 1
    return {
        "time": datetime.utcnow().isoformat(),
        "response_id": response_id,
        "request_id": request_id,
        "crawl_id": crawl_id,
        "web_status_code": random.choice([200, 404, 500]),
        "is_blocked": random.choice([0, 1]), 
        "bytes_downloaded": random.randint(1000, 5000),
        "download_speed": round(random.uniform(0.1, 10.0), 2),
        "response_time": round(random.uniform(0.1, 5.0), 2)  
    }

#each node continuously sends request/response data and sends its own updated information
def update_node_data(crawl_id, node_id):
    while True:
        request_id, request_info = generate_request_info(crawl_id)
        send_data_to_api({'request_info': request_info}, request_info_endpoint)

        response_info = generate_response_info(request_id, crawl_id)
        send_data_to_api({'response_info': response_info}, response_info_endpoint)

        node_info = generate_node_info(crawl_id, node_id)
        send_data_to_api({'node_info': node_info}, node_info_endpoint)

        time.sleep(3)

#sends data associated to the crawl, generates and sends information of nodes performing the crawl
def start_crawl(crawl_id):

    crawl_info = generate_crawl_info(crawl_id)
    send_data_to_api({'crawl_info': crawl_info}, crawl_info_endpoint)


    for _ in range(3):
        node_id = f'{crawl_id}-{_}'
        node_info = generate_node_info(crawl_id, node_id)


        send_data_to_api({'node_info': node_info}, node_info_endpoint)


        update_node_data(crawl_id, node_id)

if __name__ == "__main__":
    start_crawl(crawl_num)
