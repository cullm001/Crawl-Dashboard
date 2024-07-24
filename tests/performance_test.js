import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    vus: 200,
    duration: '1s',
};

function generate_data() {

    
}

export default function () {
    const url = 'http://localhost:4000/insert-crawl';
    const payload = JSON.stringify(generate_data());

    const params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const res = http.post(url, payload, params);

}
