import http from 'k6/http';

export const options = {
    vus: 100,
    duration: '1s',
};

export default function () {
    const url = 'API_ENDPOINT';

    const node_info = {
        time: new Date().toISOString().slice(0, 19).replace('T', ' '),
        node_id: `node_${Math.floor(Math.random() * 9000) + 1000}`,
        cpu_usage: (Math.random() * 100).toFixed(2),
        memory_usage: (Math.random() * 100).toFixed(2),
        bandwidth_usage: (Math.random() * 100).toFixed(2),
        diskspace_usage: (Math.random() * 100).toFixed(2)
    };

    const payload = JSON.stringify({ node_info });

    const params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const res = http.post(url, payload, params);

}
