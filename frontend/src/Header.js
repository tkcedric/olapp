import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import logo from '../assets/ic_launcher.png';
import '../styles.css';

function Header() {
  const navigate = useNavigate();
  const isLoggedIn = !!localStorage.getItem('session_token');
  const userId = localStorage.getItem('user_id'); // Store user_id during login

  const handleLogout = () => {
    localStorage.removeItem('session_token');
    localStorage.removeItem('user_role');
    localStorage.removeItem('user_id');
    navigate('/login');
  };

  return (
    <header className="app-header">
      <div className="header-left">
        <img src={logo} alt="App Logo" className="app-logo" />
        <h1>GCE O/L Computer Science</h1>
      </div>
      <div className="header-right">
        <Link to="/">Home</Link>
        {isLoggedIn ? (
          <>
            <Link to={`/progress/${userId}/1`}>My Progress</Link> {/* Example Topic ID */}
            <button onClick={handleLogout} className="logout-button">
              Logout
            </button>
          </>
        ) : (
          <>
            <Link to="/login">Login</Link>
            <Link to="/register">Register</Link>
          </>
        )}
      </div>
    </header>
  );
}

export default Header;
