import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import logo from '../assets/ic_launcher.png'; // Adjust if the path differs
import '../styles.css'; // Ensure this contains necessary styles

function Header() {
  const navigate = useNavigate();
  const isLoggedIn = !!localStorage.getItem('session_token'); // Check if user is logged in

  const handleLogout = () => {
    // Clear user session and redirect to login
    localStorage.removeItem('session_token');
    localStorage.removeItem('user_role');
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
            <Link to="/progress">My Progress</Link>
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
