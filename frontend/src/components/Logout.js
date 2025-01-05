import React from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Logout = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    const sessionToken = localStorage.getItem('session_token');
    axios
      .post('http://127.0.0.1:5000/api/logout', { session_token: sessionToken })
      .then(() => {
        localStorage.removeItem('session_token');
        localStorage.removeItem('user_role');
        navigate('/login'); // Redirect to login page
      })
      .catch((error) => {
        console.error('Logout failed:', error);
      });
  };

  return (
    <button onClick={handleLogout} className="logout-button">
      Logout
    </button>
  );
};

export default Logout;
