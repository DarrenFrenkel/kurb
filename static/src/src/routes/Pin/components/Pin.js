/* @flow */
import React from 'react';

export const Pin = (props) => {
  return (
    <div>
      <div>
        <h3>
          List of Pins
        </h3>
        <ul>
          {props.pin.pins.map(pin =>
            <li key={pin.pk}>
              {pin.address_street}
            </li>
          )}
        </ul>
      </div>
    </div>
)
}

Pin.propTypes = {
  pin: React.PropTypes.object,
  activePin: React.PropTypes.object,
  fetchPins: React.PropTypes.func.isRequired,
  showPinDetail: React.PropTypes.func.isRequired
}

export default Pin;
