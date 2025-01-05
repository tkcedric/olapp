import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Home from './components/Home';
import Login from './components/Login';
import Register from './pages/Register';
import ProgressTracker from './components/ProgressTracker';
import Footer from './components/Footer';
import Lesson from './components/Lesson';
import ForgotPassword from './pages/ForgotPassword';
import ResetPassword from './pages/ResetPassword';
import NotFound from './components/NotFound'; // Optional: Handle 404 pages
import './styles.css';

function App() {
  return (
    <div className="app-container">
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/progress/:userId/:topicId" element={<ProgressTracker />} />
        <Route path="/lessons/:courseId" element={<Lesson />} />
        <Route path="/forgot-password" element={<ForgotPassword />} />
        <Route path="/reset-password/:token" element={<ResetPassword />} />
        <Route path="*" element={<NotFound />} /> {/* Fallback for undefined routes */}
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
