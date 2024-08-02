import http from 'k6/http';
import {check} from 'k6';


export const options = {
    vus: 100,
    duration: '1s',
};

function gen_node_info() {
    return {
        time: new Date().toISOString().slice(0, 19).replace('T', ' '),
        node_id: `node_${Math.floor(Math.random() * 9000) + 1000}`,
        cpu_usage: (Math.random() * 100).toFixed(2),
        memory_usage: (Math.random() * 100).toFixed(2),
        bandwidth_usage: (Math.random() * 100).toFixed(2),
        diskspace_usage: (Math.random() * 100).toFixed(2)
    };
}

export default function () {
    const url = __ENV.API_ENDPOINT
  
    const payload = JSON.stringify({ node_info: gen_node_info() });

    const params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const res = http.post(url, payload, params);
    check (res, {
        'is status 200' : (r)=>r.status ===200,
        'payload inserted successfully' : (r) => r.body.includes("node_info inserted successfully")
    });

}
