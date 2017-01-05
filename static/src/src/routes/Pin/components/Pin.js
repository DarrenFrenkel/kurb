/* @flow */
import React from 'react';

import {GoogleMapLoader, GoogleMap, Marker} from 'react-google-maps';

export default function SimpleMap (props) {
  return (
    <section style={{ height: '100%' }}>
      <GoogleMapLoader
        containerElement={
          <div
            {...props.containerElementProps}
            style={{
              height: '80%',
            }}
          />
        }
        googleMapElement={
          <GoogleMap
            ref={(map) => console.log(map)}
            defaultZoom={10}
            defaultCenter={{ lat: -37.810156, lng: 144.958753 }}
          >
            {props.pin.pins.map((marker, index) => {
              const latitude = marker.latitude
              const longitude = marker.longitude
              return (
                <Marker
                  position={{ lat: latitude, lng: longitude }}
                />
              );
            })}
          </GoogleMap>
        }
      />
    </section>
  );
}

