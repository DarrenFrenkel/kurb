import React from 'react';

export default function Panel (props) {
  const {
    activePin,
    closePin
  } = props
  return (
    <aside className='side-panel'>
      <div className='side-panel--content'>
        <p>{activePin.address.street}</p>
        <p>{activePin.address.state}, {activePin.address.postal_code}</p>
        <ul className='side-panel--items'>
          {activePin.items.map((item, index) => {
            return (
              <li key={index}>{item.name}</li>
            );
          })}
        </ul>
        <div className='button-container'>
          <button className='side-panel--button'
            onClick={
              function () {
                closePin();
              }}
          >Close</button>
        </div>
      </div>
    </aside>
  );
}

Panel.propTypes = {
};

Panel.propTypes = {
  activePin: React.PropTypes.bool,
  closePin: React.PropTypes.func
};
