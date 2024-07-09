from fastapi import HTTPException
from sqlalchemy.orm import Session

from myApp.endpoints.chat.model import ChatModel
from myApp.endpoints.chat.schema import ChatSchema


# Get single chat (by ID!)
def getChat(db: Session, chat_id: int):
    chat = db.query(ChatModel.Chat).filter(ChatModel.Chat.id == chat_id).first()
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat


def get_all_chats(db: Session, skip: int = 0, limit: int = 100):
    all_chats = db.query(ChatModel.Chat).offset(skip).limit(limit).all()
    if not all_chats:
        raise HTTPException(status_code=404, detail="No chats found")
    return all_chats


def get_chat_by_name(db: Session, name: str):
    return db.query(ChatModel.Chat).filter(ChatModel.Chat.name == name).first()


# todo: can add password hashing here but will work this out later
def create_chat(db: Session, chat: ChatSchema.ChatCreate):
    # Check if chat name already exists
    existing_chat = get_chat_by_name(db, name=chat.name)
    if existing_chat:
        raise HTTPException(status_code=400, detail="Chat Name Already Exists!")

    # Create new chat
    db_chat = ChatModel.Chat(name=chat.name)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat


def delete_chat_by_id(db: Session, chat_id: int):
    # Check if chat exists
    chat_to_delete = db.query(ChatModel.Chat).filter(ChatModel.Chat.id == chat_id).first()
    if not chat_to_delete:
        raise HTTPException(status_code=404, detail="Chat not found")

    # Delete the chat
    db.delete(chat_to_delete)
    db.commit()
    return chat_to_delete


def delete_chat_by_name(db: Session, name: str):
    chat_to_delete = db.query(ChatModel.Chat).filter(ChatModel.Chat.name == name).first()
    if not chat_to_delete:
        raise HTTPException(status_code=404, detail="Chat not found")

    # Delete the chat
    db.delete(chat_to_delete)
    db.commit()
    return chat_to_delete


def update_chat_by_id(db: Session, chat_id: int, updated_data: dict):
    chat_to_update = db.query(ChatModel.Chat).filter(ChatModel.Chat.id == chat_id).first()
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
