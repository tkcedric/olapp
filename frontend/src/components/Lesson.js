import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../styles.css';

function Lesson({ courseId }) {
  const [lessons, setLessons] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:5000/api/lessons/${courseId}`)
      .then((response) => {
        setLessons(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error fetching lessons:', error);
        setError('Failed to load lessons.');
        setLoading(false);
      });
  }, [courseId]);

  if (loading) return <p>Loading lessons...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div className="lessons-container">
      <h2>Lessons</h2>
      <ul>
        {lessons.map((lesson) => (
          <li key={lesson.id} className="lesson-item">
            <h3>{lesson.title}</h3>
            <p>{lesson.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Lesson;
