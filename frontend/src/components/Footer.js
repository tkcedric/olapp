import React from 'react';
import '../styles.css';

function Footer() {
  return (
    <footer className="app-footer">
      <p>
        Copyright © 2024 by <strong>tkc@Co.</strong> All rights reserved.
      </p>
      <p>
        <a href="/terms">Terms of Service</a> | <a href="/terms">Privacy Policy</a> {/* making privacy and terms to display the same page */}
       {/*<a href="/terms">Terms of Service</a> | <a href="/privacy">Privacy Policy</a> */}
      </p>
    </footer>
  );
}

export default Footer;
