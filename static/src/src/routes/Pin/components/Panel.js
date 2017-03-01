import React from 'react';

export default function Panel (props) {
  const {
    activePin,
    closePin
  } = props
  return (
    <aside className='side-panel'>
      <p>{activePin.address_number} {activePin.address_street}</p>
      <p>{activePin.address_city}, {activePin.address_postal_code}</p>
      {activePin.items.map((item, index) => {
        return (
          <li key={index}>{item.name}</li>
        );
      })}
      <button
        onClick={
          function () {
            closePin();
          }}
      >Close</button>
    </aside>
  );
}

Panel.propTypes = {
};

Panel.propTypes = {
  activePin: React.PropTypes.bool,
  closePin: React.PropTypes.func
};
