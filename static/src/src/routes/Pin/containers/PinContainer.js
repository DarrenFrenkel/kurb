/* @flow */
import { connect } from 'react-redux';
import { fetchPins, showPinDetail, closePin } from '../modules/pin';

import Pin from '../components/Pin';

const mapActionCreators = {
  fetchPins,
  showPinDetail,
  closePin
}

const mapStateToProps = (state) => {
  return {
    activePin: state.pin.pins.find(data => data.id === state.pin.activePin),
    pin: state.pin
  };
};

export default connect(mapStateToProps, mapActionCreators)(Pin);
