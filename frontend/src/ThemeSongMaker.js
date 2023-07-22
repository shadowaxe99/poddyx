// Import necessary dependencies
import React, { useState } from 'react';

// Create the ThemeSongMaker component
function ThemeSongMaker() {
  const [themeSong, setThemeSong] = useState('');

  const generateThemeSong = async () => {
    try {
      const response = await fetch('https://api.replicate.ai/facebookresearch/musicgen', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer YOUR_API_TOKEN'
        },
        body: JSON.stringify({
          model_version: 'melody',
          prompt: 'Description of the theme song',
          duration: 30
        })
      });

      const data = await response.json();
      setThemeSong(data);
    } catch (error) {
      console.error('Error generating theme song:', error);
    }
  };

  return (
    <div>
      <h1>Theme Song Maker</h1>
      <button onClick={generateThemeSong}>Generate Theme Song</button>
      {themeSong && (
        <div>
          <h2>Theme Song:</h2>
          <audio src={themeSong} controls />
        </div>
      )}
    </div>
  );
}

export default ThemeSongMaker;