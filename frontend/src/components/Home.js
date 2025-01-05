import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

function Home() {
  return (
    <div className="home-container">
      <div className="hero-section">
        <h1>Welcome to the GCE O/L Computer Science Revision App</h1>
        <p>
          Your ultimate tool to excel in your GCE Ordinary Level Computer Science exams! 
          Get an A grade with our comprehensive and organized resources.
        </p>
        <Link to="/register" className="cta-button">
          Get Started Now!
        </Link>
      </div>

      <div className="features-section">
        <h2>Why Choose This App?</h2>
        <ul>
          <li>✔ Access GCE questions from 2010 to date.</li>
          <li>✔ Questions organized by topics for efficient revision.</li>
          <li>✔ Includes Paper 1 (MCQs), Paper 2 (structured), and Paper 3 (programming tasks).</li>
          <li>✔ Learn Python programming with easy-to-follow lessons.</li>
          <li>✔ Track your progress and identify areas for improvement.</li>
        </ul>
      </div>

      <div className="publicity-section">
        <h2>Make the Most of Our App</h2>
        <p>
          Advertise your business here! Contact us to learn more about advertising opportunities on this app.
        </p>
        <div className="ad-space">
          <p>Your Ad Here</p>
        </div>
      </div>
    </div>
  );
}

export default Home;
