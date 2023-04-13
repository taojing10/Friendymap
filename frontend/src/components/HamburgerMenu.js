import React from 'react';
import { slide as Menu } from 'react-burger-menu';
import './HamburgerMenu.css';

const HamburgerMenu = ({ onCreateEventClick, onLoginClick }) => {
  return (
    <Menu>
      <button className="menu-item" onClick={onLoginClick}>
        Login
      </button>
      <button className="menu-item" onClick={onCreateEventClick}>
        Create Event
      </button>
    </Menu>
  );
};

export default HamburgerMenu;

