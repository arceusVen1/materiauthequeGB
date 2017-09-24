import { types } from "./materiaux.action"

const initialState = {
    loading: false,
    error: null,
    materiaux: [],
};

export default function materiauxReducer(state=initialState, action) {
    switch (action.type) {
        case types.LIST_MATERIAUX.REQUEST:
            return {
                ...state,
                loading: true,
            };
        case types.LIST_MATERIAUX.SUCCESS:
            return {
                error: null,
                loading: false,
                materiaux: action.data,
            };
        case types.LIST_MATERIAUX.FAIL:
            return {
                ...state,
                loading: false,
                error: action.error,
            };
        default:
            return state;
    }
}