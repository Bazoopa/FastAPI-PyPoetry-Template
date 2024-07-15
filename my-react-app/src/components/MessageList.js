import React, { useEffect, useState } from 'react';
import axios from 'axios';

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
        const response = await axios.get('http://localhost:8000/api/v1/chats');
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
        axios.get(`http://localhost:8000/api/v1/chat/${chatId}`),
        axios.get(`http://localhost:8000/api/v1/messages/${chatId}`)
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
      // If the same chat is clicked again, clear messages
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

      const response = await axios.post('http://localhost:8000/api/v1/message/', messageData);
      console.log('Message sent successfully:', response.data);

      // Update local messages state with the new message
      setMessages([...messages, response.data]);

      // Clear input fields after sending the message
      setUsernameInput('');
      setMessageInput('');
    } catch (error) {
      console.error('Error sending message:', error);
      // Handle error scenario as needed
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

      const response = await axios.post('http://localhost:8000/api/v1/chat/', chatData);
      console.log('Chat created successfully:', response.data);

      // Update local chats state with the new chat
      setChats([...chats, response.data]);

      // Clear the new chat name input
      setNewChatName('');
    } catch (error) {
      console.error('Error creating chat:', error);
      // Handle error scenario as needed
    }
  };

  const handleDeleteChat = async () => {
    if (!selectedChat) {
      alert('Please select a chat to delete.');
      return;
    }

    try {
      const response = await axios.delete(`http://localhost:8000/api/v1/chat/${selectedChat.id}`);
      console.log('Chat deleted successfully:', response.data);

      // Remove the deleted chat from local state
      setChats(chats.filter(chat => chat.id !== selectedChat.id));

      // Clear selected chat and messages
      setSelectedChat(null);
      setMessages([]);
    } catch (error) {
      console.error('Error deleting chat:', error);
      // Handle error scenario as needed
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

      {/* New Chat section */}
      <div>
        <input
          type="text"
          placeholder="Enter chat name"
          value={newChatName}
          onChange={(e) => setNewChatName(e.target.value)}
        />
        <button onClick={handleNewChat} style={{ marginTop: '10px' }}>
          Create Chat
        </button>
      </div>

      {selectedChat && (
        <div className="message-display">
          <h2>Messages in Chat {selectedChat.name}</h2>

          {/* Messages section */}
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

          {/* Input fields for username and message */}
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

          {/* Action buttons */}
          <div>
            {/* Send Message button */}
            <button onClick={handleSendMessage}>Send Message</button>
          </div>

          <div>
            {/* Delete Chat button */}
            <button onClick={handleDeleteChat} style={{ marginTop: '10px' }}>
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
