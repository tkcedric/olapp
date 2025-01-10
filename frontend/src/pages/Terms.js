import React from 'react';
import '../styles.css'; // Ensure this CSS includes necessary styling

function Terms() {
  return (
    <div className="terms-container">
      <h1>Terms of Service</h1>
      <p>
        By using this platform, you agree to the following:
      </p>
      <h2>1. Purpose and Use</h2>
      <p>
        This platform is designed to provide resources for students preparing for their GCE Ordinary Level Computer Science exams. Users agree to utilize the resources responsibly and ethically. Redistribution or unauthorized sharing of the platform's resources is strictly prohibited.
      </p>
      <h2>2. Registration and Account Creation</h2>
      <p>
        After submitting your registration information, it will be verified by our team. Your account will be created and activated within 24 hours. Please ensure all the details provided during registration are accurate to avoid delays.
      </p>
      <h2>3. Accuracy of Resources</h2>
      <p>
        We strive to provide accurate and up-to-date information. However, we do not guarantee that all resources will be free of errors. Users are encouraged to report any issues or errors to our team via email at gceolcomputerscience@gmail.com.
      </p>
      <h2>4. Prohibited Use</h2>
      <p>
        Users are prohibited from:
        <ul>
          <li>Attempting to reverse engineer, copy, or reproduce the platform or its resources.</li>
          <li>Sharing their login credentials with others.</li>
          <li>Using the platform for purposes unrelated to its educational goals.</li>
        </ul>
      </p>
      <h2>5. Liability</h2>
      <p>
        The platform is provided "as is," and we are not liable for any errors or omissions in the content or for any issues arising from the misuse of the platform.
      </p>
      <h2>Privacy Policy</h2>
      <p>
        Your privacy is important to us.
      </p>
      <ul>
        <li>
          <strong>Personal Information:</strong> Any personal information you provide (e.g., name, email, phone number) will only be used to provide our services. We will not share your information with third parties without your consent.
        </li>
        <li>
          <strong>Payment Details:</strong> Payments are securely processed, and transaction details (e.g., transaction ID) are not stored on our servers.
        </li>
        <li>
          <strong>Data Security:</strong> We follow industry best practices to protect your data.
        </li>
      </ul>
      <p>
        For any concerns or questions about your privacy, contact us at gceolcomputerscience@gmail.com.
      </p>
      <h2>Additional Note</h2>
      <p>
        By agreeing to these terms, you acknowledge that your account will only be activated after your registration details are verified. The verification process is manual and may take up to <strong>24 hours</strong>. If you encounter any delays beyond this period, please contact us at gceolcomputerscience@gmail.com for assistance.
      </p>
    </div>
  );
}

export default Terms;
