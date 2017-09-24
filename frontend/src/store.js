import { compose, createStore, applyMiddleware } from 'redux';
import createSagaMiddleware from 'redux-saga'

import { createLogger } from 'redux-logger';
//import { persistStore, autoRehydrate } from 'redux-persist';
import rootReducer from './reducers';
import rootSaga from './sagas';

// create the saga Middleware
const sagaMiddleware = createSagaMiddleware();

const store = createStore(
    rootReducer,
    //redux dev tool
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),
    compose(
        applyMiddleware(
            createLogger(),
            sagaMiddleware,
        ),
        //autoRehydrate()
    )
);
//persistStore(store);

// run the saga
sagaMiddleware.run(rootSaga);

export default store;
