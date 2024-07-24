import http from 'k6/http';
import {sleep} from 'k6';

export const options = {
    vus: 130,
    duration: '1s',
};

const payload = JSON.stringify({
    
  });


export default function () {

    http.get('http://localhost:4000/customer_data')

  }