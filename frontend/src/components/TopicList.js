import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './TopicList.css'; // Create a CSS file for styling

function TopicList() {
  const [topics, setTopics] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    axios
      .get('http://127.0.0.1:5000/api/topics')
      .then((response) => {
        if (response.data.topics) {
          setTopics(response.data.topics); // Adjust based on API structure
          setLoading(false);
        } else {
          setError('Unexpected API response');
          setLoading(false);
        }
      })
      .catch((error) => {
        console.error('Error fetching topics:', error);
        setError('Failed to fetch topics. Please try again later.');
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading topics...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <h1>Topics</h1>
      <ul>
        {topics.map((topic) => (
          <li
            key={topic.id}
            className="topic-item"
            onClick={() => navigate(`/topics/${topic.id}`)} // Navigate to topic details on click
          >
            <h2>{topic.name}</h2>
            <p>{topic.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TopicList;
