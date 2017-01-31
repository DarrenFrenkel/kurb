import React from 'react';
import classNames from 'classnames';

export default function Panel (props) {
  return (
    <aside className='side-panel'>
      <p>{props.props.address_number} {props.props.address_street}</p>
      <p>{props.props.address_city}, {props.props.address_postal_code}</p>
      {props.props.items.map((item, index) => {
        return (
          <li key={index}>{item.name}</li>
        );
      })}

    </aside>
  );
}

Panel.propTypes = {
};
