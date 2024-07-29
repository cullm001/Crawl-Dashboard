import json
import random
import time
import requests
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed

crawl_info_endpoint = 'http://localhost:4000/insert-crawl-info'
crawl_node_endpoint = 'http://localhost:4000/insert-crawl-node'
#node_info_endpoint = 'http://localhost:4000/insert-node-info'
#request_info_endpoint = 'http://localhost:4000/insert-resquest-info'
#response_info_endpoint = 'http://localhost:4000/insert-response-info'
info_endpoint = 'http://localhost:4000/insert-info'

def generate_mock_data():
    crawl_id = f"crawl_{cid}"
    cid = cid + 1
    cluster_id = f"user_{random.randint(1, 10)}"
    node_id = f"node_{random.randint(1, 10)}"
    request_id = f"req_{random.randint(1000, 9999)}"
    response_id = f"resp_{random.randint(1000, 9999)}"
    proxy = f"proxy_{random.randint(1, 5)}"
    engine = f"engine_{random.randint(1, 5)}"
    fingerprint = f"fingerprint_{random.randint(1, 100)}"

    responseinfo = []
    requestinfo = []
    nodeinfo = []

    response_info = {
        "time": datetime.now().isoformat(),
        "response_id": response_id,
        "request_id": request_id,
        "domain_name": f"domain{random.randint(1, 10)}.com",
        "website_status_code": random.choice([200, 404, 500]),
        "is_blocked": random.choice([0, 1]),
        "bytes_downloaded": random.randint(1000, 5000),
        "download_speed": round(random.uniform(0.1, 10.0), 2)
    }

    request_info = {
        "time": datetime.now().isoformat(),
        "request_id": request_id,
        "crawl_id": crawl_id,
        "proxy": proxy,
        "engine": engine,
        "fingerprint": fingerprint
    }

    node_info = {
        "time": datetime.now().isoformat(),
        "node_id": node_id,
        "cpu_usage": round(random.uniform(0, 100), 2),
        "memory_usage": round(random.uniform(0, 100), 2),
        "bandwidth_usage": round(random.uniform(0, 100), 2),
        "diskspace_usage": round(random.uniform(0, 100), 2)
    }

    crawl_node = {
        "crawl_id": crawl_id,
        "node_id": node_id
    }

    responseinfo.append(response_info)
    requestinfo.append(request_info)
    nodeinfo.append(node_info)
    crawlinfo.append(crawl_info)
    crawlnode.append(crawl_node)

    data = {
        "responseinfo": responseinfo,
        "requestinfo": requestinfo,
        "nodeinfo": nodeinfo,
        "crawlnode": crawlnode,
        "crawlinfo": crawlinfo
    }

    return data

def send_data_to_api(data, api_endpoint):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_endpoint, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        print('Data sent successfully.')
    else:
        print('Failed to send data. Status code:', response.status_code)

def generate_and_send_data():
    mock_data = generate_mock_data()
    send_data_to_api(mock_data)

cid = 0
crawlinfos = []
crawlnodes = []
index = -1
crawlids = []
rindex = 0
responseinfo = []
requestinfo = []
nodeinfo = []

while True:
    
    # Start Nodes
    nodeids = []
    for i in range(5):
        index = index + 1
        nodeids.append(index)
        
    # Start a Crawl
    crawl_id = f"crawl_{cid}"
    cluster_id = f"user_{cid}"
    crawlids.append(cid)

    cid = cid + 1

    crawl_info = {
        "crawl_id": crawl_id,
        "cluster_id": cluster_id,
        "request_time": datetime.now().isoformat(),
        "response_time": (datetime.now() + timedelta(seconds=random.randint(1, 5))).isoformat(),
        "total_requests": random.randint(100, 1000),
        "requests_per_sec": random.randint(1, 100),
        "concurrent_requests": random.randint(1, 10),
        "estimated_time_to_complete": random.randint(1, 120),
        "avg_cost_per_query": round(random.uniform(0.01, 1.00), 2),
        "api_status_code": random.choice([200, 404, 500]),
        "success_rate": round(random.uniform(0, 100), 2),
        "error_rate": round(random.uniform(0, 100), 2)
    }

    for i in range(5):
        crawl_node = {
            "crawl_id": crawl_id,
            "node_id": nodeids[i]
        }
        crawlnodes.append(crawl_node)
        data = {
            'crawlnode': crawlnodes
        }
        send_data_to_api(data, crawl_node_endpoint)
        crawlnodes.pop()

    
    crawlinfos.append(crawl_info)
    data = {
        'crawlinfo': crawlinfos
    }
    send_data_to_api(data, crawl_info_endpoint)
    crawlinfos.pop()

    for _ in range(100):

        response_info = {
            "time": datetime.now().isoformat(),
            "response_id": rindex,
            "request_id": rindex,
            "crawl_id": crawl_id,
            "domain_name": f"domain{random.randint(1, 10)}.com",
            "website_status_code": random.choice([200, 404, 500]),
            "is_blocked": random.choice([0, 1]),
            "bytes_downloaded": random.randint(1000, 5000),
            "download_speed": round(random.uniform(0.1, 10.0), 2)
        }

        request_info = {
            "time": datetime.now().isoformat(),
            "request_id": rindex,
            "crawl_id": crawl_id,
            "proxy": f"proxy_{random.randint(1, 5)}",
            "engine": f"engine_{random.randint(1, 5)}",
            "fingerprint": f"fingerprint_{random.randint(1, 100)}"
        }

        node_info = {
            "time": datetime.now().isoformat(),
            "node_id": random.choice(nodeids),
            "cpu_usage": round(random.uniform(0, 100), 2),
            "memory_usage": round(random.uniform(0, 100), 2),
            "bandwidth_usage": round(random.uniform(0, 100), 2),
            "diskspace_usage": round(random.uniform(0, 100), 2)
        }
        rindex = rindex + 1

        responseinfo.append(response_info)
        requestinfo.append(request_info)
        nodeinfo.append(node_info)

        data = {
            'responseinfo': responseinfo,
            'requestinfo': requestinfo,
            'nodeinfo': nodeinfo
        }

        send_data_to_api(data, info_endpoint)

        responseinfo.pop()
        requestinfo.pop()
        nodeinfo.pop()

        time.sleep(2)
    
    #mock_data = generate_mock_data()
    #send_data_to_api(mock_data)
    #print(mock_data)
    time.sleep(1000000)







#if __name__ == "__main__":
#    while True:
#        with ThreadPoolExecutor(max_workers=5) as executor:
#            futures = [executor.submit(generate_and_send_data) for _ in range(5)]
#            for future in as_completed(futures):
#                try:
#                    future.result()
#                except Exception as exc:
#                    print(f'Generated an exception: {exc}')
#            time.sleep(0.5)