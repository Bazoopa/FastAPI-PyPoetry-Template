import React, { useEffect, useState } from 'react';
import axios from 'axios';

const MessageList = () => {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/v1/messages/2')
      .then(response => {
        console.log(response.data);  // Log the response data to check its structure
        setMessages(response.data);
      })
      .catch(error => {
        console.error('Error fetching messages:', error);
      });
  }, []);

  return (
    <div>
      <h2>Messages in Chat 2</h2>
      <ul>
        {messages.map(message => (
          <li key={message.id}>
            <strong>{message.username}</strong>: {message.message}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MessageList;
