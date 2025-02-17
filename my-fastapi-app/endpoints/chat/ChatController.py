import logging

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from database.database_connection import get_db
from endpoints.chat import ChatSchema, ChatService

logging.basicConfig(level=logging.DEBUG)

router = APIRouter()


@router.get("/chat/{chat_id}", response_model=ChatSchema.DBChat, tags=["Chat"])
def getChat(chat_id: int, db: Session = Depends(get_db)):
    return ChatService.getChat(db, chat_id=chat_id)


# Get all chats
@router.get("/chats/", response_model=list[ChatSchema.DBChat], tags=["Chat"])
def getChats(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return ChatService.get_all_chats(db, skip=skip, limit=limit)


# Create a chat
@router.post("/chat/", response_model=ChatSchema.DBChat, tags=["Chat"])
def create_chat(chat: ChatSchema.ChatCreate, db: Session = Depends(get_db)):
    return ChatService.create_chat(db=db, chat=chat)


# Delete a chat (by id)
@router.delete("/chat/id-delete/{chat_id}", response_model=ChatSchema.DBChat, tags=["Chat"])
def deleteChat_by_id(chat_id: int, db: Session = Depends(get_db)):
    return ChatService.delete_chat_by_id(db=db, chat_id=chat_id)


# delete a chat by name. These could be merged into 1, but it would break Single responsibility principle.
@router.delete("/chat/name-delete/{chat_name}", response_model=ChatSchema.DBChat, tags=["Chat"])
def delete_chat_by_name(chat_name: str, db: Session = Depends(get_db)):
    return ChatService.delete_chat_by_name(db=db, name=chat_name)


# Update a chat name, I may remove this from being usable at a later date.
@router.put("/chat/update/{chat_id}", response_model=ChatSchema.DBChat, tags=["Chat"])
def update_chat_by_id(chat_id: int, updated_data: ChatSchema.ChatUpdate, db: Session = Depends(get_db)):
    return ChatService.update_chat_by_id(db=db, chat_id=chat_id,
                                         updated_data=updated_data.model_dump(exclude_unset=True))
