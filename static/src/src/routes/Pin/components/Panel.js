import React from 'react';
import classNames from 'classnames';

export default function Panel (props) {
  return (
    <aside className='side-panel'>
      <p>{props.props.address.street}</p>
      <p>{props.props.address.state}, {props.props.address.postal_code}</p>
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
