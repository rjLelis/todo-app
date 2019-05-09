
const defaultHeader = new Headers({'Content-type': 'application/json'});

const config = {
    defaultEndpoint: 'http://localhost:8080/api/todo/',
    GET: () => {
        return {
            method: 'GET',
            headers: defaultHeader,
        }
    },
    POST: item => {
        return {
            method: 'POST',
            body: JSON.stringify(item),
            headers: defaultHeader,
        }
    },
    DELETE: () => {
        return {
            method: 'DELETE',
            headers: defaultHeader,
        }
    },
    PUT: () => {
        return {
            method: 'PUT',
            headers: defaultHeader,
        }
    },
};

export default config;