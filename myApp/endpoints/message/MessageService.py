from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, relationship, DeclarativeBase


class MessageBase(BaseModel):
    username: str
    message: str


class MessageCreate(MessageBase):
    chat_id: int


class MessageUpdate(MessageBase):
    pass


class Message(MessageBase):
    id: int
    chat_id: int

    class Config:
        from_attributes = True  # Updated for Pydantic v2 and later


class Base(DeclarativeBase):
    pass


class DBMessage(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), nullable=False)
    message = Column(String(280), nullable=False)
    chat_id = Column(Integer, ForeignKey('chats.id', ondelete='CASCADE'), nullable=False)

    chat = relationship("Chat", back_populates="messages")


def get_message(db: Session, message_id: int):
    message = db.query(Message).filter(message_id == DBMessage.id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not Found")
    return message


def get_all_messages_from_chat(db: Session, chat_id: int, skip: int = 0, limit: int = 100):
    """Get all messages from a specific chat with optional pagination."""
    return db.query(Message).filter(chat_id == DBMessage.chat_id).offset(skip).limit(limit).all()


def create_message(db: Session, message: MessageCreate):
    try:
        db_message = Message(username=message.username, message=message.message, chat_id=message.chat_id)
        db.add(db_message)
        db.commit()
        db.refresh(db_message)
        return db_message
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Chat doesn't exist!"
        )


def delete_message_by_id(db: Session, message_id: int):
    message_to_delete = db.query(DBMessage).filter(message_id == DBMessage.id).first()
    if not message_to_delete:
        raise HTTPException(status_code=404, detail="message not found")
    db.delete(message_to_delete)
    db.commit()
    return message_to_delete
