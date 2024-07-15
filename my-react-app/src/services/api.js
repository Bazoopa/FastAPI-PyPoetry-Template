// src/services/api.js

import axios from 'axios';

const API_URL = 'http://localhost:8000'; // Adjust to your backend URL

export const getChats = async () => {
  const response = await axios.get(`${API_URL}/chats/`);
  return response.data;
};

export const createChat = async (chatName) => {
  const response = await axios.post(`${API_URL}/chat/`, { name: chatName });
  return response.data;
};

export const getMessages = async (chatId) => {
  const response = await axios.get(`${API_URL}/messages/${chatId}`);
  return response.data;
};

export const createMessage = async (chatId, username, message) => {
  const response = await axios.post(`${API_URL}/message/`, { chat_id: chatId, username, message });
  return response.data;
};
