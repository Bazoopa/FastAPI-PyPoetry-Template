import React, { useEffect, useState } from 'react';
import axios from 'axios';

const MessageList = ({}) => {
  const [chats, setChats] = useState([]);
  const [selectedChat, setSelectedChat] = useState(null);
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

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

  if (isLoading) {
    return <div>Loading...</div>;
  }

  const handleSendMessage = () => {
    // Placeholder function for sending a message
    console.log('Sending message...');
    // You can implement functionality to send the message here
  };

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

      {selectedChat && (
        <div className="message-display">
          <h2>Messages in Chat {selectedChat.name}</h2>
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

          {/* Text boxes for username and message */}
          <div>
            <input type="text" placeholder="Enter your username" />
          </div>
          <div>
            <textarea rows="4" placeholder="Type your message"></textarea>
          </div>

          {/* Send Message button */}
          <button onClick={handleSendMessage}>Send Message</button>
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
