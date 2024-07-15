import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './MessageList.css';  // Import the CSS file

const MessageList = () => {
  const [chats, setChats] = useState([]);
  const [selectedChat, setSelectedChat] = useState(null);
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [usernameInput, setUsernameInput] = useState('');
  const [messageInput, setMessageInput] = useState('');
  const [newChatName, setNewChatName] = useState('');

  useEffect(() => {
    const fetchChats = async () => {
      try {
        setIsLoading(true);
        const response = await axios.get('http://bruce.installation00.net:8000/api/v1/chats');
        setChats(response.data);
        setIsLoading(false);
      } catch (error) {
        console.error('Error fetching chats:', error);
        setIsLoading(false);
      }
    };

    fetchChats();
  }, []);

  const fetchMessagesForChat = async (chatId) => {
    try {
      setIsLoading(true);
      const [chatResponse, messagesResponse] = await Promise.all([
        axios.get(`http://bruce.installation00.net:8000/api/v1/chat/${chatId}`),
        axios.get(`http://bruce.installation00.net:8000/api/v1/messages/${chatId}`)
      ]);
      setSelectedChat(chatResponse.data);
      setMessages(messagesResponse.data);
      setIsLoading(false);
    } catch (error) {
      console.error('Error fetching chat or messages:', error);
      setSelectedChat(null);
      setMessages([]);
      setIsLoading(false);
    }
  };

  const handleClickOpen = async (chatId) => {
    if (chatId === selectedChat?.id) {
      setSelectedChat(null);
      setMessages([]);
    } else {
      await fetchMessagesForChat(chatId);
    }
  };

  const handleSendMessage = async () => {
    if (!usernameInput || !messageInput || !selectedChat) {
      alert('Please enter username and message, and select a chat.');
      return;
    }

    try {
      const messageData = {
        username: usernameInput,
        message: messageInput,
        chat_id: selectedChat.id
      };

      const response = await axios.post('http://bruce.installation00.net:8000/api/v1/message/', messageData);
      console.log('Message sent successfully:', response.data);

      setMessages([...messages, response.data]);
      setUsernameInput('');
      setMessageInput('');
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  const handleNewChat = async () => {
    if (!newChatName) {
      alert('Please enter a chat name.');
      return;
    }

    try {
      const chatData = {
        name: newChatName
      };

      const response = await axios.post('http://bruce.installation00.net:8000/api/v1/chat/', chatData);
      console.log('Chat created successfully:', response.data);

      setChats([...chats, response.data]);
      setNewChatName('');
    } catch (error) {
      console.error('Error creating chat:', error);
    }
  };

  const handleDeleteChat = async () => {
    if (!selectedChat) {
      alert('Please select a chat to delete.');
      return;
    }

    const confirmDelete = window.confirm(`Are you sure you want to delete the chat "${selectedChat.name}"?`);
    if (!confirmDelete) {
      return;
    }

    try {
      const response = await axios.delete(`http://bruce.installation00.net:8000/api/v1/chat/id-delete/${selectedChat.id}`);
      console.log('Chat deleted successfully:', response.data);

      setChats(chats.filter(chat => chat.id !== selectedChat.id));
      setSelectedChat(null);
      setMessages([]);
    } catch (error) {
      console.error('Error deleting chat:', error);
    }
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="message-list-container">
      <div className="chat-list">
        {chats.map(chat => (
          <div key={chat.id} className="chat-item">
            <button onClick={() => handleClickOpen(chat.id)}>Open</button>
            <span>{chat.name}</span>
          </div>
        ))}
      </div>

      <div className="new-chat-container">
        <input
          type="text"
          placeholder="Enter chat name"
          value={newChatName}
          onChange={(e) => setNewChatName(e.target.value)}
          className="new-chat-input"
        />
        <button onClick={handleNewChat} className="new-chat-button">
          Create Chat
        </button>
      </div>

      {selectedChat && (
        <div className="message-display">
          <h2 className="message-display-header">Messages in Chat: {selectedChat.name}</h2>

          {messages.length > 0 ? (
            <ul>
              {messages.map(message => (
                <li key={message.id}>
                  <strong>{message.username}</strong>: {message.message}
                </li>
              ))}
            </ul>
          ) : (
            <p>No messages found</p>
          )}

          <div>
            <input
              type="text"
              placeholder="Enter your username"
              value={usernameInput}
              onChange={(e) => setUsernameInput(e.target.value)}
            />
          </div>
          <div>
            <textarea
              rows="4"
              placeholder="Type your message"
              value={messageInput}
              onChange={(e) => setMessageInput(e.target.value)}
            ></textarea>
          </div>

         <div className="action-buttons">
      <button onClick={handleSendMessage}>Send Message</button>
     <button onClick={handleDeleteChat} className="delete-button" style={{ marginTop: '10px' }}>
  Delete Chat
</button>
    </div>
        </div>
      )}

      {!selectedChat && (
        <div className="select-chat-message">
          <p>Please select a chat</p>
        </div>
      )}
    </div>
  );
};

export default MessageList;
