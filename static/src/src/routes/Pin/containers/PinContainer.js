/* @flow */
import { connect } from 'react-redux';
import { fetchPins, showPinDetail, closePin, addPin } from '../modules/pin';

import Pin from '../components/Pin';

const mapActionCreators = {
  fetchPins,
  showPinDetail,
  closePin,
  addPin
};

const mapStateToProps = (state) => {
  return {
    activePin: state.pin.activePin,
    pin: state.pin,
    activePanel: state.pin.activePanel
  };
};

export default connect(mapStateToProps, mapActionCreators)(Pin);
