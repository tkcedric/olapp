import React, { useEffect, useState } from "react";

const TopicList = () => {
  const [topics, setTopics] = useState([]); // State to store the topics
  const [error, setError] = useState(null); // State to handle errors

  useEffect(() => {
    // Fetch topics from the API
    fetch("/api/topics")
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        if (Array.isArray(data.topics)) {
          setTopics(data.topics); // Update topics state
        } else {
          throw new Error("API response does not contain a valid topics array.");
        }
      })
      .catch((err) => {
        console.error("Error fetching topics:", err);

        // Fallback to mock data for debugging
        const mockData = {
          current_page: 1,
          pages: 1,
          topics: [
            {
              description: "Learn the basics of programming.",
              id: 1,
              is_free: true,
              name: "Introduction to Programming",
              summary: "<p>This topic covers variables, data types, and control structures.</p>",
            },
            {
              description: "Learn about arrays, linked lists, stacks, and queues.",
              id: 2,
              is_free: false,
              name: "Data Structures",
              summary: "<p>Understand how data is organized and manipulated.</p>",
            },
          ],
          total: 2,
        };

        console.log("Using mock data due to error:", mockData);
        setTopics(mockData.topics); // Set mock data
        setError("Error loading topics from API. Displaying mock data.");
      });
  }, []);

  return (
    <div>
      <h1>Topics</h1>
      {error && <div style={{ color: "red" }}>{error}</div>} {/* Display error message */}
      {topics.length > 0 ? (
        topics.map((topic) => (
          <div key={topic.id}>
            <h2>{topic.name}</h2>
            <p>{topic.description}</p>
            <div dangerouslySetInnerHTML={{ __html: topic.summary }}></div>
          </div>
        ))
      ) : (
        <p>Loading topics...</p>
      )}
    </div>
  );
};

export default TopicList;
