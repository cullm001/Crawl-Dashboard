import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    vus: 200,
    duration: '1s',
};

function generate_data() {

    
}

export default function () {
    const url = 'URL_ENDPOINT';
    const payload = JSON.stringify(generate_data());

    const params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const res = http.post(url, payload, params);

}
