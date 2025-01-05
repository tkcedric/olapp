import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { API_BASE_URL } from '../config'; // Centralized configuration for API URLs
import '../styles.css'; // Use global styles for consistency

function Register() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    role: 'student', // Default role
  });

  const [message, setMessage] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false); // Loading state

  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setError(''); // Reset error message
    setLoading(true); // Set loading state
    axios
      .post(`${API_BASE_URL}/register`, formData)
      .then((response) => {
        setMessage(response.data.message);
        setLoading(false);
        setTimeout(() => navigate('/login'), 2000); // Redirect after 2 seconds
      })
      .catch((error) => {
        console.error('Registration failed:', error.response?.data);
        setError(
          error.response?.data?.message || 'Registration failed. Please try again.'
        );
        setLoading(false);
      });
  };

  return (
    <div className="register-container">
      <h1>Register</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
          required
          autoComplete="username"
          aria-label="Username"
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
          autoComplete="email"
          aria-label="Email"
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
          autoComplete="new-password"
          aria-label="Password"
        />
        <select
          name="role"
          value={formData.role}
          onChange={handleChange}
          required
          aria-label="Role"
        >
          <option value="student">Student</option>
          <option value="admin">Admin</option>
        </select>
        <button type="submit" disabled={loading}>
          {loading ? 'Registering...' : 'Register'}
        </button>
      </form>
      {message && <p className="success-message">{message}</p>}
      {error && <p className="error-message">{error}</p>}
    </div>
  );
}

export default Register;
