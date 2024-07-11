from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session, relationship, DeclarativeBase


class ChatBase(BaseModel):
    name: str


class ChatCreate(ChatBase):
    pass


class ChatUpdate(ChatBase):
    pass


class Chat(ChatBase):
    id: int

    class Config:
        from_attributes = True  # Updated for Pydantic v2 and later


class Base(DeclarativeBase):
    pass


class DBChat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)

    messages = relationship("Message", back_populates="chat")


# Get single chat (by ID!)
def getChat(db: Session, chat_id: int):
    chat = db.query(DBChat).filter(chat_id == DBChat.id).first()
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat


def get_all_chats(db: Session, skip: int = 0, limit: int = 100):
    all_chats = db.query(DBChat).offset(skip).limit(limit).all()
    if not all_chats:
        raise HTTPException(status_code=404, detail="No chats found")
    return all_chats


def get_chat_by_name(db: Session, name: str):
    return db.query(Chat).filter(name == DBChat.name).first()


# todo: can add password hashing here but will work this out later
def create_chat(db: Session, chat: ChatCreate):
    # Check if chat name already exists

    existing_chat = get_chat_by_name(db, name=chat.name)

    # todo: the problem with the tests occurs here -> gotta work out why.
    if existing_chat:
        raise HTTPException(status_code=400, detail="Chat Name Already Exists!")

    # Create new chat
    db_chat = Chat(name=chat.name)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat


def delete_chat_by_id(db: Session, chat_id: int):
    # Check if chat exists
    chat_to_delete = db.query(Chat).filter(chat_id == DBChat.id).first()
    if not chat_to_delete:
        raise HTTPException(status_code=404, detail="Chat not found")

    # Delete the chat
    db.delete(chat_to_delete)
    db.commit()
    return chat_to_delete


def delete_chat_by_name(db: Session, name: str) :
    chat_to_delete = db.query(DBChat).filter(name == DBChat.name).first()
    if not chat_to_delete:
        raise HTTPException(status_code=404, detail="Chat not found")

    # Delete the chat
    db.delete(chat_to_delete)
    db.commit()
    return chat_to_delete


def update_chat_by_id(db: Session, chat_id: int, updated_data: dict):
    chat_to_update = db.query(DBChat).filter(chat_id == DBChat.id).first()
    if not chat_to_update:
        raise HTTPException(status_code=404, detail="Chat not found")

    existing_chat = get_chat_by_name(db, name=updated_data['name'])
    if existing_chat:
        raise HTTPException(status_code=400, detail="Chat Name Already Exists!")

    # Update chat attributes with updated_data
    for key, value in updated_data.items():
        setattr(chat_to_update, key, value)

    db.commit()
    db.refresh(chat_to_update)
    return chat_to_update
