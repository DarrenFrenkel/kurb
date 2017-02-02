import { injectReducer } from '../../store/reducers';

export default (store) => ({
  path: 'pin',
  getComponent (nextState, next) {
    require.ensure([
      './containers/PinContainer',
      './modules/pin'
    ], (require) => {
      const Pin = require('./containers/PinContainer').default;
      const pinReducer = require('./modules/pin').default;

      injectReducer(store, {
        key: 'pin',
        reducer: pinReducer
      });
      next(null, Pin);
    });
  }
});
