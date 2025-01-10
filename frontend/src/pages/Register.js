import React, { useState } from 'react';
import '../styles.css';
import { API_BASE_URL } from '../config'; // Ensure this is properly configured
import axios from 'axios';

function Register() {
  const [role, setRole] = useState(''); // Track the selected role
  const [formData, setFormData] = useState({
    school: '',
    email: '',
    phoneNumber: '',
    transactionId: '',
    name: '', // For student's or teacher's name
    password: '', // For student's password
    studentName: '', // For teacher's form
    studentEmail: '', // For teacher's form
    studentPhoneNumber: '', // For teacher's form
    studentPassword: '', // For teacher's form
  });
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleRoleSelection = (selectedRole) => {
    setRole(selectedRole);
    setMessage('');
    setError('');
    setFormData({
      school: '',
      email: '',
      phoneNumber: '',
      transactionId: '',
      name: '',
      password: '',
      studentName: '',
      studentEmail: '',
      studentPhoneNumber: '',
      studentPassword: '',
    });
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  
  const handleSubmit = (e) => {
      e.preventDefault();
  
      if (!formData.school || !formData.email || !formData.phoneNumber || !formData.transactionId) {
          setError('All fields are required.');
          return;
      }
  
      const emailContent = `
          Role: ${role}
          School: ${formData.school}
          Name: ${formData.name}
          Email: ${formData.email}
          Phone Number: ${formData.phoneNumber}
          Transaction ID: ${formData.transactionId}
          ${role === 'student' ? `Password: ${formData.password}` : ''}
          ${role === 'teacher' ? `Student's Name: ${formData.studentName}` : ''}
          ${role === 'teacher' ? `Student's Email: ${formData.studentEmail}` : ''}
          ${role === 'teacher' ? `Student's Phone Number: ${formData.studentPhoneNumber}` : ''}
          ${role === 'teacher' ? `Student's Password: ${formData.studentPassword}` : ''}
      `;
  
      axios
          .post(`${API_BASE_URL}/send-email`, {
              role,
              content: emailContent,
          })
          .then((response) => {
              setMessage('Your information has been sent successfully!');
              setError('');
          })
          .catch((error) => {
              console.error('Failed to send email:', error);
              setError('Failed to send your information. Please try again.');
          });
  };
  

  return (
    <div className="register-container">
      {!role ? (
        <div>
          <h1>I am a:</h1>
          <div className="role-selection">
            <button className="role-button" onClick={() => handleRoleSelection('student')}>
              Student
            </button>
            <button className="role-button" onClick={() => handleRoleSelection('teacher')}>
              Teacher
            </button>
          </div>
        </div>
      ) : (
        <>
          <div className="transaction-details">
            <h3>Transaction Details</h3>
            <p>
              **Payment is to be made to the phone number: <strong>678429258</strong>
              <br />
              Account Name: <strong>Tala Kuate Cedric</strong>**
            </p>
          </div>
          <form className="registration-form" onSubmit={handleSubmit}>
            <h1>{role === 'student' ? 'Student Registration' : 'Teacher Registration'}</h1>
            <input
              type="text"
              name="school"
              placeholder="School"
              value={formData.school}
              onChange={handleChange}
              required
            />
            <input
              type="text"
              name="name"
              placeholder="Your Name"
              value={formData.name}
              onChange={handleChange}
              required
            />
            <input
              type="email"
              name="email"
              placeholder="Your Email"
              value={formData.email}
              onChange={handleChange}
              required
            />
            <input
              type="text"
              name="phoneNumber"
              placeholder="Your Phone Number"
              value={formData.phoneNumber}
              onChange={handleChange}
              required
            />
            {role === 'student' && (
              <input
                type="password"
                name="password"
                placeholder="Your Password"
                value={formData.password}
                onChange={handleChange}
                required
              />
            )}
            {role === 'teacher' && (
              <>
                <input
                  type="text"
                  name="studentName"
                  placeholder="Student's Name"
                  value={formData.studentName}
                  onChange={handleChange}
                  required
                />
                <input
                  type="email"
                  name="studentEmail"
                  placeholder="Student's Email"
                  value={formData.studentEmail}
                  onChange={handleChange}
                  required
                />
                <input
                  type="text"
                  name="studentPhoneNumber"
                  placeholder="Student's Phone Number"
                  value={formData.studentPhoneNumber}
                  onChange={handleChange}
                  required
                />
                <input
                  type="password"
                  name="studentPassword"
                  placeholder="Student's Password"
                  value={formData.studentPassword}
                  onChange={handleChange}
                  required
                />
              </>
            )}
            <input
              type="text"
              name="transactionId"
              placeholder="Transaction ID"
              value={formData.transactionId}
              onChange={handleChange}
              required
            />
            <button type="submit" className="submit-button">
              Send Your Information for Registration
            </button>
            <button type="button" onClick={() => setRole('')} className="back-button">
              Back
            </button>
          </form>
        </>
      )}
      {message && <p className="success-message">{message}</p>}
      {error && <p className="error-message">{error}</p>}
    </div>
  );
}

export default Register;
