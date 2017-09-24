import { watchFetchListMateriauxSaga } from "./materiaux";
import {all} from 'redux-saga/effects';

export default function* rootSaga() {
    yield all([
        watchFetchListMateriauxSaga(),
    ]);
}