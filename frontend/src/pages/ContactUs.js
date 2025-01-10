import React from 'react';
import '../styles.css';

function ContactUs() {
  return (
    <div className="contact-us-container">
      <h1>Contact Us</h1>
      <p>We'd love to hear from you! You can reach us through the following channels:</p>
      <ul>
        <li>
          <strong>Facebook:</strong>{' '}
          <a href="https://web.facebook.com/profile.php?id=61571677856779" target="_blank" rel="noopener noreferrer">
            Visit our Facebook page
          </a>
        </li>
        <li>
          <strong>Email:</strong> <a href="mailto:gceolcomputerscience@gmail.com">gceolcomputerscience@gmail.com</a>
        </li>
        <li>
          <strong>WhatsApp:</strong> +237620477832
        </li>
      </ul>
    </div>
  );
}

export default ContactUs;
