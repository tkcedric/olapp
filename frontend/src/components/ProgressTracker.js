// src/components/ProgressTracker.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../ProgressTracker.css';

const ProgressTracker = ({ userId, topicId }) => {
  const [progress, setProgress] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch user progress for the topic
    axios
      .get(`http://127.0.0.1:5000/api/progress/${userId}/${topicId}`)
      .then((response) => {
        setProgress(response.data);
      })
      .catch((error) => {
        setError(error.response?.data?.error || 'Error fetching progress.');
      });
  }, [userId, topicId]);

  const handleUpdateProgress = (answeredCorrectly) => {
    // Update progress with the specified number of correctly answered questions
    axios
      .put(`http://127.0.0.1:5000/api/progress/${userId}/${topicId}`, {
        answered_correctly: answeredCorrectly,
      })
      .then((response) => {
        setProgress(response.data.progress);
      })
      .catch((error) => {
        setError(error.response?.data?.error || 'Error updating progress.');
      });
  };

  const handleMarkAsCompleted = () => {
    // Mark the progress as completed by updating with total questions
    handleUpdateProgress(progress.total_questions);
  };

  if (error) {
    return <div className="progress-error">{error}</div>;
  }

  if (!progress) {
    return <div className="progress-loading">Loading progress...</div>;
  }

  return (
    <div className="progress-tracker">
      <h3>Progress Tracker</h3>
      <p>
        <strong>Topic:</strong> {progress.topic_id}
      </p>
      <p>
        <strong>Answered Correctly:</strong> {progress.answered_correctly} / {progress.total_questions}
      </p>
      <p>
        <strong>Completed:</strong> {progress.completed ? 'Yes' : 'No'}
      </p>
      {!progress.completed && (
        <>
          <button
            onClick={() => handleUpdateProgress(progress.answered_correctly + 1)}
            className="update-progress-btn"
          >
            Mark One More Correct
          </button>
          <button onClick={handleMarkAsCompleted} className="mark-complete-btn">
            Mark as Completed
          </button>
        </>
      )}
    </div>
  );
};

export default ProgressTracker;
