import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function TopicList() {
  const [topics, setTopics] = useState([]); // Ensure topics is an array
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:5000/api/topics')
      .then((response) => {
        if (Array.isArray(response.data)) {
          setTopics(response.data);
        } else {
          console.error('API response is not an array:', response.data);
          setError(true);
        }
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error fetching topics:', error);
        setError(true);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading topics...</p>;
  if (error) return <p>Error loading topics. Please try again later.</p>;

  return (
    <div>
      <h1>Topics</h1>
      <ul>
        {topics.map((topic) => (
          <li key={topic.id}>
            <Link to={`/topics/${topic.id}`}>{topic.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TopicList;
