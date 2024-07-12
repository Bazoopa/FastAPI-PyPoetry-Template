from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from endpoints.base import Base


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)  # Specify the length for VARCHAR

    messages = relationship("Message", back_populates="chat", cascade="all, delete-orphan")
