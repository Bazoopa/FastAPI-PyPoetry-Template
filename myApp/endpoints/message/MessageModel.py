from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from endpoints.base import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), nullable=False)
    message = Column(String(280), nullable=False)
    chat_id = Column(Integer, ForeignKey('chats.id', ondelete='CASCADE'), nullable=False)

    chat = relationship("Chat", back_populates="messages")
