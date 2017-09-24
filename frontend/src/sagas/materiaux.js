import { call, put, takeEvery } from 'redux-saga/effects';
import materiaux from '../services/api/materiaux';
import {
    types,
    materiauxSuccess,
    materiauxFail,
} from "../reducers/materiaux/materiaux.action";

export function* fetchListMateriauxSaga(action) {
    try {
//        const listMateriaux = yield call(materiaux.fetchListMateriaux);
        const listMateriaux = [{'id': 1, 'nom': "yolo"}];
        yield put(materiauxSuccess(listMateriaux));
    }
    catch(error) {
        yield put(materiauxFail(error));
    }
}

export function* watchFetchListMateriauxSaga() {
    yield takeEvery(types.LIST_MATERIAUX.REQUEST, fetchListMateriauxSaga)
}