from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from myApp.database import Base


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)

    messages = relationship("Message", back_populates="chat")
