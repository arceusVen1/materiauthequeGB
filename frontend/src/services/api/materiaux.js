import { fetch } from "./fetch"

const materiaux = {
    fetchListMateriau() {
        return fetch('/materiaux').then(response => {
            response.body
        });
    },
};

export default materiaux;

