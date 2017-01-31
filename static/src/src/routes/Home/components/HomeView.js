import React from 'react';
import DuckImage from '../assets/Duck.jpg';
import Header from '../../../components/Header';
import './HomeView.scss';

export const HomeView = () => (
  <div>
    <Header />
    <h4>Welcome!</h4>
    <img
      alt='This is a duck, because Redux!'
      className='duck'
      src={DuckImage} />
  </div>
)

export default HomeView;
