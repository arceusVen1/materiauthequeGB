export const types = {
    LIST_MATERIAUX: {
        REQUEST: 'LIST_MATERIAUX.REQUEST',
        SUCCESS: 'LIST_MATERIAUX.SUCCESS',
        FAIL: 'LIST_MATERIAUX.FAIL',
    },
};

export const requestMateriaux = () => ({
    type: types.LIST_MATERIAUX.REQUEST
});

export const materiauxSuccess = data => ({
    type: types.LIST_MATERIAUX.SUCCESS,
    data,
});

export const materiauxFail = error => ({
    type: types.LIST_MATERIAUX.FAIL,
    error,
});

