import React, { useEffect, useState } from 'react';
import axios from 'axios';
import MessageList from './MessageList';

const ChatList = () => {
  const [chats, setChats] = useState([]);
  const [selectedChatId, setSelectedChatId] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/api/v1/chats')
      .then(response => {
        setChats(response.data);
      })
      .catch(error => {
        console.error('Error fetching chats:', error);
      });
  }, []);

  const handleChatSelect = (chatId) => {
    setSelectedChatId(chatId);
  };

  return (
    <div>
      <h2>All Chats</h2>
      <ul>
        {chats.map(chat => (
          <li key={chat.id} onClick={() => handleChatSelect(chat.id)}>
            {chat.name}
          </li>
        ))}
      </ul>
      {selectedChatId !== null && <MessageList chatId={selectedChatId} />}
    </div>
  );
};

export default ChatList;