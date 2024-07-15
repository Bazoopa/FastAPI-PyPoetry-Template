import React, { useEffect, useState } from 'react';
import axios from 'axios';

const MessageList = ({ chatId }) => {
  const [chatName, setChatName] = useState('');
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const fetchChatNameAndMessages = async () => {
      if (chatId) {
        setIsLoading(true);

        try {
          // Fetch chat name
          const chatResponse = await axios.get(`http://localhost:8000/api/v1/chat/${chatId}`);
          if (chatResponse.data && chatResponse.data.name) {
            setChatName(chatResponse.data.name);
          } else {
            setChatName('');
          }

          // Fetch messages
          const messagesResponse = await axios.get(`http://localhost:8000/api/v1/messages/${chatId}`);
          setMessages(messagesResponse.data);

          setIsLoading(false);
        } catch (error) {
          console.error('Error fetching data:', error);
          setChatName('');
          setMessages([]);
          setIsLoading(false);
        }
      } else {
        setChatName('');
        setMessages([]);
        setIsLoading(false);
      }
    };

    fetchChatNameAndMessages();
  }, [chatId]);

  // Display loading indicator while fetching data
  if (isLoading) {
    return <div>Loading...</div>;
  }

  // Display messages if chatId is valid and messages are present
  if (chatId && messages.length > 0) {
    return (
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
    );
  }

  // Display message when there are no messages for the selected chat
  if (chatId && messages.length === 0) {
    return (
      <div>
        <h2>Messages in Chat {chatName}</h2>
        <p>No messages found</p>
      </div>
    );
  }

  // Default case: No chat selected message should not appear if chatId is falsy
  return null;
};

export default MessageList;
