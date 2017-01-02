// We only need to import the modules necessary for initial render
import CoreLayout from '../layouts/CoreLayout/CoreLayout'
import Home from './Home'
import CounterRoute from './Counter'

/*  Note: Instead of using JSX, we recommend using react-router
    PlainRoute objects to build route definitions.   */

export const createRoutes = (store) => {

  const routes = {
  path        : '/',
  component   : CoreLayout,
  indexRoute  : Home,
  getChildRoutes (location, next) {
      require.ensure([], (require) => {
        next(null, [
          // Provide store for async reducers and middleware
          require('./Counter').default(store),
          require('./Pin').default(store),
        ])
      })
    }
  }
  return routes
}

export default createRoutes
