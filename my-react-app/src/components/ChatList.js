import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ChatList = () => {
  const [chats, setChats] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/v1/chats')
      .then(response => {
        setChats(response.data);
      })
      .catch(error => {
        console.error('Error fetching chats:', error);
      });
  }, []);

  return (
    <div>
      <h2>All Chats</h2>
      <ul>
        {chats.map(chat => (
          <li key={chat.id}>
            {chat.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ChatList;
