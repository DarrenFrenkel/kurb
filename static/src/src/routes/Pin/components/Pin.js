import React from 'react';
import classNames from 'classnames';
import { GoogleMapLoader, GoogleMap, Marker } from 'react-google-maps';
import Panel from './Panel';

require('./Pin.scss');

export default function SimpleMap (props) {
  return (
    <section className='page-container'>
      {
        props.activePanel &&
        <Panel
          activePin={props.activePin}
          closePin={props.closePin}
        />
      }
      <button
        className='new-pin--button'
        onClick={props.addPin}
      >+</button>
      <GoogleMapLoader
        containerElement={
          <div
            {...props.containerElementProps}
            className={classNames(
              'map-container',
            )}
          />
        }
        googleMapElement={
          <GoogleMap
            defaultZoom={10}
            defaultCenter={{ lat: -37.810156, lng: 144.958753 }}
          >
            {props.pin.pins.map((marker, index) => {
              const latitude = marker.address.latitude;
              const longitude = marker.address.longitude;
              return (
                <Marker key={index}
                  position={{ lat: latitude, lng: longitude }}
                  onClick={
                    function () {
                      props.showPinDetail(marker.id);
                    }
                  }
                />
              );
            })}
          </GoogleMap>
        }
      />
    </section>
  );
}

SimpleMap.propTypes = {
  containerElementProps: React.PropTypes.object,
  pin: React.PropTypes.object,
  activePin: React.PropTypes.object,
  closePin: React.PropTypes.func,
  addPin: React.PropTypes.func,
  activePanel: React.PropTypes.bool
};
