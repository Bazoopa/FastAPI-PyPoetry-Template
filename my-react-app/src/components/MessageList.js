import React, { useEffect, useState } from 'react';
import axios from 'axios';

const MessageList = ({ chatId }) => {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    if (chatId !== null) {
      axios.get(`http://localhost:8000/api/v1/messages/${chatId}`)
        .then(response => {
          setMessages(response.data);
        })
        .catch(error => {
          console.error('Error fetching messages:', error);
        });
    }
  }, [chatId]);

  return (
    <div>
      <h2>Messages in Chat {chatId}</h2>
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
