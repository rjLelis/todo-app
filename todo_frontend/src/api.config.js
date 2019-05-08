
const defaultHeader = new Headers({'Content-type': 'application/json'});

const conf = {
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

export default conf;