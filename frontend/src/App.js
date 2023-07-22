// Import necessary dependencies
import React, { useState } from 'react';

// Create the App component
function App() {
  const [feedback, setFeedback] = useState('');
  const [agentFeedback, setAgentFeedback] = useState('');

  const handleFeedbackChange = (event) => {
    setFeedback(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Call API or perform necessary actions with the feedback
    // For demonstration purposes, set the agent feedback to a random response
    const randomResponses = [
      "Thank you for your feedback!",
      "We appreciate your input.",
      "Your feedback has been noted.",
      "We will take your suggestions into consideration."
    ];
    const randomIndex = Math.floor(Math.random() * randomResponses.length);
    setAgentFeedback(randomResponses[randomIndex]);
    setFeedback('');
  };

  return (
    <div>
      <h1>AI Agent Radio Producer</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Feedback:
          <input type="text" value={feedback} onChange={handleFeedbackChange} />
        </label>
        <button type="submit">Submit</button>
      </form>
      {agentFeedback && (
        <div>
          <h2>Agent Feedback:</h2>
          <p>{agentFeedback}</p>
        </div>
      )}
    </div>
  );
}

export default App;