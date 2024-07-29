import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    vus: 100,
    duration: '1s',
};

function generate_data() {
    let crawl_id = `crawl_${Math.floor(Math.random() * 9999)}`;
    let cluster_id = `user_${Math.floor(Math.random() * 10) + 1}`;
    let node_id = `node_${Math.floor(Math.random() * 9000) + 1000}`;
    let request_id = `req_${Math.floor(Math.random() * 9000) + 1000}`;
    let response_id = `resp_${Math.floor(Math.random() * 9000) + 1000}`;
    let proxy = `proxy_${Math.floor(Math.random() * 5) + 1}`;
    let engine = `engine_${Math.floor(Math.random() * 5) + 1}`;
    let fingerprint = `fingerprint_${Math.floor(Math.random() * 100) + 1}`;

    const response_info = {
        time: new Date().toISOString().slice(0, 19).replace('T', ' '),
        response_id: response_id,
        request_id: request_id,
        domain_name: `domain${Math.floor(Math.random() * 10) + 1}.com`,
        website_status_code: [200, 404, 500][Math.floor(Math.random() * 3)],
        bytes_downloaded: Math.floor(Math.random() * 4001) + 1000,
        is_blocked: Math.floor(Math.random() * 2),
        download_speed: (Math.random() * 9.9 + 0.1).toFixed(2)
    };

    const request_info = {
        time: new Date().toISOString().slice(0, 19).replace('T', ' '),
        request_id: request_id,
        crawl_id: crawl_id,
        proxy: proxy,
        engine: engine,
        fingerprint: fingerprint
    };

    const node_info = {
        time: new Date().toISOString().slice(0, 19).replace('T', ' '),
        node_id: node_id,
        cpu_usage: (Math.random() * 100).toFixed(2),
        memory_usage: (Math.random() * 100).toFixed(2),
        bandwidth_usage: (Math.random() * 100).toFixed(2),
        diskspace_usage: (Math.random() * 100).toFixed(2)
    };

    const crawl_node = {
        crawl_id: crawl_id,
        node_id: node_id
    };

    const crawl_info = {
        crawl_id: crawl_id,
        user_id: cluster_id,
        request_time: new Date().toISOString().slice(0, 19).replace('T', ' '),
        response_time: new Date(Date.now() + Math.floor(Math.random() * 5000) + 1000).toISOString().slice(0, 19).replace('T', ' '),
        requests_per_sec: Math.floor(Math.random() * 9999),
        concurrent_requests: Math.floor(Math.random() * 50) + 1,
        total_requests: Math.floor(Math.random() * 9999),
        avg_cost_per_query: (Math.random() * (.99) + 0.01).toFixed(2),
        estimated_time_to_completion: Math.floor(Math.random() * 120) + 1,
        api_status_code: [200, 404, 500][Math.floor(Math.random() * 3)],
        success_rate: (Math.random() * 100).toFixed(2),
        error_rate: (Math.random() * 100).toFixed(2)
    };

    const data = {
        response_info: response_info,
        request_info: request_info,
        node_info: node_info,
        crawl_node: crawl_node,
        crawl_info: crawl_info
    };

    return data;
}

export default function () {
    const url = 'API_ENDPOINT';
    const payload = JSON.stringify(generate_data());

    const params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const res = http.post(url, payload, params);

}
