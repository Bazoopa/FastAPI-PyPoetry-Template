import React, { useState, useEffect } from 'react';
import axios from 'axios';

const MessageList = ({ chatId }) => {
  const [chatName, setChatName] = useState('');
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    const fetchChatName = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/api/v1/chat/${chatId}`);
        if (response.data && response.data.name) {
          setChatName(response.data.name);
        } else {
          setChatName('');
        }
      } catch (error) {
        console.error('Error fetching chat name:', error);
        setChatName('');
      }
    };

    fetchChatName();
  }, [chatId]);

  const fetchMessages = async () => {
    try {
      setIsLoading(true);
      setError(null);
      const response = await axios.get(`http://localhost:8000/api/v1/messages/${chatId}`);
      setMessages(response.data);
    } catch (error) {
      console.error('Error fetching messages:', error);
      setError('Error fetching messages. Please try again.');
      setMessages([]);
    } finally {
      setIsLoading(false);
    }
  };

  const toggleOpen = () => {
    setIsOpen(!isOpen);
    if (!isOpen) {
      fetchMessages();
    }
  };

  return (
    <div>
      <button onClick={toggleOpen}>{isOpen ? 'Close' : 'Open'} Messages for {chatName}</button>
      {isOpen && (
        <div>
          {isLoading ? (
            <div>Loading...</div>
          ) : messages.length > 0 ? (
            <div>
              <h2>Messages in Chat {chatName}</h2>
              <ul>
                {messages.map(message => (
                  <li key={message.id}>
                    <strong>{message.username}</strong>: {message.message}
                  </li>
                ))}
              </ul>
            </div>
          ) : (
            <p>No messages found</p>
          )}
          {error && <p>{error}</p>}
        </div>
      )}
    </div>
  );
};

export default MessageList;
