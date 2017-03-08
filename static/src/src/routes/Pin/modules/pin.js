/* @flow */

// ------------------------------------
// Constants
// ------------------------------------
export const REQUEST_PINS = 'REQUEST_PINS';
export const RECIEVE_PINS = 'RECIEVE_PINS';
export const SHOW_PIN_DETAIL = 'SHOW_PIN_DETAIL';
export const CLOSE_PIN = 'CLOSE_PIN';

// ------------------------------------
// Actions
// ------------------------------------

export function requestPins () {
  return {
    type: REQUEST_PINS
  };
}

export function recievePins (value) {
  return {
    type: RECIEVE_PINS,
    payload: {
      pins: value
    }
  };
}

export function showPinDetail (value) {
  return {
    type: SHOW_PIN_DETAIL,
    payload: {
      pinId: value
    }
  };
}

export function closePin (value) {
  return {
    type: CLOSE_PIN
  };
}

export const fetchPins = () => {
  return (dispatch) => {
    // dispatch(requestPins());

    return fetch('http://127.0.0.1:8000/api/v1/pins/')
    // TODO: Need to catch an error if the api request fails
      .then(data => data.text())
      // .then(text => dispatch(recievePins(text)));
  };
};

export const actions = {
  requestPins,
  recievePins,
  fetchPins,
  showPinDetail,
  closePin
};

// ------------------------------------
// Action Handlers
// ------------------------------------

const PIN_ACTION_HANDLERS = {
  [REQUEST_PINS]: (state) => {
    return ({ ...state, fetching: true });
  },
  [RECIEVE_PINS]: (state, action) => {
    return ({ ...state, pins: action.payload.pins, fetching: false });
  },
  [SHOW_PIN_DETAIL]: (state, action) => {
    return ({ ...state, activePin: action.payload.pinId });
  },
  [CLOSE_PIN]: (state) => {
    return ({ ...state, activePin: null });
  }
};

// ------------------------------------
// Reducer
// ------------------------------------

const pins = window && window.INITIAL_STATE && window.INITIAL_STATE.pins
  ? window.INITIAL_STATE.pins
  : []

const initialState = { fetching: false, activePin: null, pins: pins };

export default function pinReducer (state = initialState, action) {
  const handler = PIN_ACTION_HANDLERS[action.type];

  return handler ? handler(state, action) : state;
}
