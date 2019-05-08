
const defaultHeader = new Headers({'Content-type': 'application/json'});

const config = {
    defaultEndpoint: 'http://localhost:8080/api/todo/',
    GET: {
        method: 'GET',
        headers: defaultHeader,
    },
    POST: {
        method: 'POST',
        headers: defaultHeader,
    },
    DELETE: {
        method: 'DELETE',
        headers: defaultHeader,
    },
    PUT: {
        method: 'PUT',
        headers: defaultHeader,
    },
};

export default config;