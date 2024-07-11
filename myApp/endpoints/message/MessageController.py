import logging

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from database import get_db, engine  # Adjust import as needed
from endpoints.message import MessageModel, MessageSchema, MessageService

# Configure logging settings (optional)
logging.basicConfig(level=logging.DEBUG)  # Set the desired log level

# Create database tables if they do not exist

router = APIRouter()


# Example of using get_db()
@router.get("/message/{message_id}", response_model=MessageSchema.Message, tags=["Message"])
def get_message(message_id: int, db: Session = Depends(get_db)):
    return MessageService.get_message(db, message_id=message_id)


@router.get("/messages/{chat_id}", response_model=list[MessageSchema.Message], tags=["Message"])
def get_messages(chat_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return MessageService.get_all_messages_from_chat(db, chat_id, skip=skip, limit=limit)


@router.post("/message/", response_model=MessageSchema.Message, tags=["Message"])
def create_message(message: MessageSchema.MessageCreate, db: Session = Depends(get_db)):
    return MessageService.create_message(db=db, message=message)


@router.delete("/message/{message_id}", response_model=MessageSchema.Message, tags=["Message"])
def delete_message(message_id: int, db: Session = Depends(get_db)):
    return MessageService.delete_message_by_id(db=db, message_id=message_id)


# @router.put("/message/{message_id}", response_model=MessageSchema)
# def update_message(message_id: int, updated_data: MessageUpdate, db: Session = Depends(get_db)):
#     return MessageService.update_message(db=db, message_id=message_id, updated_data=updated_data.dict(exclude_unset=True))
