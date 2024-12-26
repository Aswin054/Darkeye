import React from 'react';
import { 
  BsGrid1X2Fill, 
  BsFillGearFill,
  BsEyeFill,
  BsDatabaseLock,
  BsDatabaseFill,
  BsGraphUp,
  BsArrowCounterclockwise 
} from 'react-icons/bs';
import { Link } from "react-router-dom";

function Sidebar({ openSidebarToggle, OpenSidebar }) {
  return (
    <aside id="sidebar" className={openSidebarToggle ? "sidebar-responsive" : "sidebar"}>
      <div className="sidebar-title">
        <div className="sidebar-brand">
          <BsEyeFill className="icon_header" /> DARK-EYE
        </div>
        <span className="icon close_icon" onClick={OpenSidebar}>X</span>
      </div>

      <ul className="sidebar-list">
        <li className="sidebar-list-item">
          <Link to="/Dashboard">
            <BsGrid1X2Fill className="icon" /> Dashboard
          </Link>
        </li>
        <li className="sidebar-list-item">
          <Link to="/DataCollection">
            <BsDatabaseLock className="icon" /> Data Collection
          </Link>
        </li>
        <li className="sidebar-list-item">
          <Link to="/DataPreprocessing">
            <BsDatabaseFill className="icon" /> Data Preprocessing
          </Link>
        </li>
        <li className="sidebar-list-item">
          <Link to="/Visualization">
            <BsGraphUp className="icon" /> Visualization
          </Link>
        </li>
        <li className="sidebar-list-item">
          <Link to="/Alerts">
            <BsArrowCounterclockwise className="icon" /> Alerts
          </Link>
        </li>
        <li className="sidebar-list-item">
          <Link to="/Settings">
            <BsFillGearFill className="icon" /> Settings
          </Link>
        </li>
      </ul>
    </aside>
  );
}

export default Sidebar;
