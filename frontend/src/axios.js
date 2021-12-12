import axios from 'axios'

const getAPI = axios.create({
    baseURL: 'http://127.0.0.1:5000',
    timeout: 20000,
    headers: {"Access-Control-Allow-Origin": "*"},
})

export {
    getAPI
}