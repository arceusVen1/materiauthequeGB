const myInit = { method: 'GET',
    headers : {
        'Accept'        : 'application/json',
        'Content-Type'  : 'application/json'
    },
    cache: 'default' };

export const fetchListMateriau = async () => {
    const resp = await fetch('http://localhost:8000/api/materiaux/', myInit)
    console.log(resp)
    const data = await resp.json();
    return data;
};


