import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import '../styles.css';

function Login() {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });

  const [message, setMessage] = useState('');
  const [error, setError] = useState('');
  const [showPassword, setShowPassword] = useState(false); // Toggle state for password visibility
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setError(''); // Reset error message
    axios
      .post('http://127.0.0.1:5000/api/login', formData)
      .then((response) => {
        const { session_token, role } = response.data;
        localStorage.setItem('session_token', session_token);
        localStorage.setItem('user_role', role);
        setMessage('Login successful!');
        setTimeout(() => navigate('/'), 2000); // Redirect to home page after 2 seconds
      })
      .catch((error) => {
        console.error('Login failed:', error.response?.data);
        setError(
          error.response?.data?.message || 'Login failed. Please try again.'
        );
      });
  };

  return (
    <div className="login-container">
      <h1>Login</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <div>
          <input
            type={showPassword ? 'text' : 'password'} // Switch between text and password
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            required
          />
          <div
            className="password-toggle"
            onClick={() => setShowPassword((prev) => !prev)}
          >
            {showPassword ? 'Hide Password' : 'Show Password'}
          </div>
        </div>
        <button type="submit">Login</button>
      </form>
      {message && <p className="success-message">{message}</p>}
      {error && <p className="error-message">{error}</p>}
    </div>
  );
}

export default Login;
