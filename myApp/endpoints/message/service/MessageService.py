from fastapi import HTTPException
from sqlalchemy.orm import Session

from myApp.endpoints.message.model.MessageModel import Message

from myApp.endpoints.message.schema import MessageSchema


# todo: add error handling.

def get_message(db: Session, message_id: int):
    message = db.query(Message).filter(Message.id == message_id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not Found")
    return message


def get_all_messages_from_chat(db: Session, chat_id: int, skip: int = 0, limit: int = 100) -> list[MessageSchema]:
    """Get all messages from a specific chat with optional pagination."""
    return db.query(Message).filter(Message.chat_id == chat_id).offset(skip).limit(limit).all()


def create_message(db: Session, message: MessageSchema.MessageCreate):
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
    message_to_delete = db.query(Message).filter(Message.id == message_id).first()
    if not message_to_delete:
        raise HTTPException(status_code=404, detail="message not found")
    db.delete(message_to_delete)
    db.commit()
    return message_to_delete
