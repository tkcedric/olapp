import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Progress() {
  const [progress, setProgress] = useState([]);
  const userId = 1; // Replace with actual user ID

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:5000/api/progress/${userId}`)
      .then((response) => {
        setProgress(response.data);
      })
      .catch((error) => {
        console.error('Error fetching progress:', error);
      });
  }, [userId]);

  return (
    <div>
      <h1>My Progress</h1>
      <ul>
        {progress.map((record) => (
          <li key={record.id}>
            Topic ID: {record.topic_id}, Correct Answers: {record.answered_correctly} /{' '}
            {record.total_questions}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Progress;
