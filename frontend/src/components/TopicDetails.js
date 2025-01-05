import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './TopicDetails.css';

function TopicDetails() {
  const { id } = useParams(); // Extract topic ID from the URL
  const userId = 1; // Replace with dynamic user ID when authentication is implemented
  const [topic, setTopic] = useState(null);
  const [progress, setProgress] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [feedback, setFeedback] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch topic details
    axios.get(`http://127.0.0.1:5000/api/topics/${id}`)
      .then((response) => {
        setTopic(response.data);
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        setError('Failed to load topic details.');
        setLoading(false);
      });

    // Fetch progress for the topic
    axios.get(`http://127.0.0.1:5000/api/progress/${userId}/${id}`)
      .then((response) => {
        setProgress(response.data);
      })
      .catch((err) => {
        console.error(err);
        setProgress(null); // Handle gracefully if no progress is found
      });

    // Fetch questions for the topic
    axios.get(`http://127.0.0.1:5000/api/questions?topic_id=${id}`)
      .then((response) => {
        setQuestions(response.data.questions || []);
      })
      .catch((err) => {
        console.error(err);
        setQuestions([]);
      });
  }, [id, userId]);

  const handleAnswer = (questionId, isCorrect) => {
    // Update feedback based on answer
    setFeedback(isCorrect ? 'Correct!' : 'Incorrect!');

    // Update progress if the answer is correct
    if (isCorrect) {
      axios.put(`http://127.0.0.1:5000/api/progress/${userId}/${id}`, {
        answered_correctly: 1,
      })
        .then((response) => {
          setProgress((prev) => ({
            ...prev,
            answered_correctly: prev.answered_correctly + 1,
            completed: response.data.completed,
          }));
        })
        .catch((err) => {
          console.error('Failed to update progress:', err);
        });
    }
  };

  if (loading) return <div className="loading">Loading...</div>;
  if (error) return <div className="error-message">{error}</div>;

  return (
    <div className="topic-details-container">
      <h1>{topic.name}</h1>
      <p>{topic.description}</p>
      <div className="topic-summary" dangerouslySetInnerHTML={{ __html: topic.summary }} />

      {/* Progress Section */}
      {progress && (
        <div className="progress-section">
          <h2>Progress</h2>
          <p>Questions answered correctly: {progress.answered_correctly}/{progress.total_questions}</p>
          <p>Status: {progress.completed ? 'Completed' : 'In Progress'}</p>
        </div>
      )}

      {/* Questions Section */}
      <div className="questions-section">
        <h2>Questions</h2>
        {questions.length > 0 ? (
          questions.map((question) => (
            <div key={question.id} className="question-item">
              <p>{question.text}</p>
              {question.answers.map((answer) => (
                <button
                  key={answer.id}
                  onClick={() => handleAnswer(question.id, answer.is_correct)}
                >
                  {answer.text}
                </button>
              ))}
            </div>
          ))
        ) : (
          <p>No questions available for this topic.</p>
        )}
      </div>

      {/* Feedback Section */}
      {feedback && (
        <div className={`feedback-message ${feedback === 'Correct!' ? 'correct' : 'incorrect'}`}>
          {feedback}
        </div>
      )}
    </div>
  );
}

export default TopicDetails;
