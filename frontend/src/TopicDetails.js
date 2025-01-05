import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './TopicDetails.css'; // Create a CSS file for styling

function TopicDetails() {
  const { id } = useParams();
  const [topic, setTopic] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:5000/api/topics/${id}`)
      .then((response) => {
        setTopic(response.data);
        setError(null);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error fetching topic details:', error);
        setError('Failed to load topic details. Please try again later.');
        setLoading(false);
      });
  }, [id]);

  if (loading) {
    return <div className="loading">Loading topic details...</div>;
  }

  if (error) {
    return <div className="error-message">{error}</div>;
  }

  return (
    <div className="topic-details-container">
      <h1>{topic.name}</h1>
      <p>{topic.description}</p>
      <div
        className="topic-summary"
        dangerouslySetInnerHTML={{ __html: topic.summary }}
      />
    </div>
  );
}

export default TopicDetails;
