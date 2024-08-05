#!/usr/bin/env python3

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


id_counter = 0
def generate_node_info(node_id):
    global id_counter
    id = id_counter
    id_counter += 1
    node_info = {
        "time": datetime.now().isoformat(),
        "id": id,
        "node_id": node_id,
        "cpu_usage": round(random.uniform(0, 100), 2),
        "memory_usage": round(random.uniform(0, 100), 2),
        "bandwidth_usage": round(random.uniform(0, 100), 2),
        "diskspace_usage": round(random.uniform(0, 100), 2)
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

def generate_crawl_node(crawl_id):
    nodes = []
    for _ in range(5):
        nodes.append({
            "crawl_id": crawl_id,
            "node_id": 10 + _
        })

    return nodes

    
request_id_counter = 0
def generate_request_info(crawl_id):
    global request_id_counter
    request_id = request_id_counter
    request_id_counter += 1

    return request_id, {
        "time": datetime.now().isoformat(),
        "request_id": request_id,
        "crawl_id": crawl_id,
        "proxy": f"proxy_{random.randint(1, 5)}",
        "engine": f"engine_{random.randint(1, 5)}",
        "fingerprint": f"fingerprint_{random.randint(1, 100)}"
    }


response_id_counter = 0
def generate_response_info(request_id, crawl_id):
    global response_id_counter
    response_id = response_id_counter
    response_id_counter += 1
    return {
        "time": datetime.now().isoformat(),
        "response_id": response_id,
        "request_id": request_id,
        "web_status_code": random.choice([200, 404, 500]),
        "is_blocked": random.choice([0, 1]),
        "bytes_downloaded": random.randint(1000, 5000),
        "download_speed": round(random.uniform(0.1, 10.0), 2),
        "crawl_id": crawl_id,
        "response_time": round(random.uniform(0.1, 5.0), 2)  
    }

def update_node_data(node_id, crawl_id):
    for _ in range(5):
        #generates and sends request information
        request_id, request_info = generate_request_info(crawl_id)
        send_data_to_api({'request_info': request_info}, request_info_endpoint)

        # #generates response for associated request
        response_info = generate_response_info(request_id, crawl_id)
        send_data_to_api({'response_info': response_info}, response_info_endpoint)

        # sends updated node info
        node_info = generate_node_info(node_id)
        send_data_to_api({'node_info': node_info}, node_info_endpoint)

def start_crawl(crawl_id):

    #creates and send data associated to crawl
    crawl_info = generate_crawl_info(crawl_id)
    send_data_to_api({'crawl_info': crawl_info}, crawl_info_endpoint)

    #creates the relationship between crawl and asssociated nodes
    nodes = generate_crawl_node(crawl_id)
    send_data_to_api({'crawl_node': node}, crawl_node_endpoint)

    #each node performing the crawl sends data
    for node in nodes:

    #generates and sends the information of node
        node_info = generate_node_info(node['node_id'])
        send_data_to_api({'node_info': node_info}, node_info_endpoint)

    #during the crawl, node sends request/response information
        update_node_data(node['node_id'], crawl_id)

if __name__ == "__main__":
    start_crawl(1)
