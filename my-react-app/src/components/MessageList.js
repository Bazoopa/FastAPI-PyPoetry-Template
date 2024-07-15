import React, { useEffect, useState } from 'react';
import axios from 'axios';

const MessageList = ({ chatId }) => {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false); // Adjusted initial state

  useEffect(() => {
    if (chatId) { // Only fetch messages if chatId is truthy
      setIsLoading(true); // Start loading

      axios.get(`http://localhost:8000/api/v1/messages/${chatId}`)
        .then(response => {
          setMessages(response.data);
          setIsLoading(false);
        })
        .catch(error => {
          console.error('Error fetching messages:', error);
          setMessages([]);
          setIsLoading(false);
        });
    } else {
      // Reset state if chatId is null
      setMessages([]);
      setIsLoading(false);
    }
  }, [chatId]);

  if (!chatId) {
    return null; // Return nothing if chatId is null
  }

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      {messages.length > 0 && (
        <h2>Messages in Chat {chatId}</h2>
      )}
      <ul>
        {messages.length > 0 ? (
          messages.map(message => (
            <li key={message.id}>
              <strong>{message.username}</strong>: {message.message}
            </li>
          ))
        ) : (
          <li>No messages found</li>
        )}
      </ul>
    </div>
  );
};

export default MessageList;
