// src/components/ChatList.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { List, Button } from 'semantic-ui-react';

const ChatList = ({ onSelectChat }) => {
  const [chats, setChats] = useState([]);

  useEffect(() => {
    axios.get('/api/chats/')
      .then(response => {
        setChats(response.data);
      })
      .catch(error => {
        console.error('Error fetching chats:', error);
      });
  }, []);

  return (
    <List>
      {chats.map(chat => (
        <List.Item key={chat.id}>
          <Button onClick={() => onSelectChat(chat.id)}>
            {chat.name}
          </Button>
        </List.Item>
      ))}
    </List>
  );
};

export default ChatList;
