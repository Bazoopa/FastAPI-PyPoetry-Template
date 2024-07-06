import logging
from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from myApp.DAOs import ChatDAO
from myApp.DTOs import ChatDTO
from myApp.Services import ChatService
from myApp.database import SessionLocal, engine

# Configure logging settings (optional)
logging.basicConfig(level=logging.DEBUG)  # Set the desired log level

ChatDAO.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    logging.debug("Attempting to establish database connection...")
    db = SessionLocal()
    try:
        yield db
        logging.debug("Successfully connected to the database!")
    finally:
        db.close()
        logging.debug("Database connection closed.")


# Example of using get_db()
@router.get("/chat/{chat_id}", response_model=ChatDTO.Chat)
def getChat(chat_id: int, db: Session = Depends(get_db)):
    logging.info(f"Handling request for chat_id: {chat_id}")
    try:
        db_chat = ChatService.getChat(db, chat_id=chat_id)
        if db_chat is None:
            raise HTTPException(status_code=404, detail="Chat not found")
        return db_chat
    except Exception as e:
        logging.error(f"Error fetching chat_id {chat_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error test")



# Get all chats
# @myApp.get("/chats/", response_model=list[ChatDTO.Chat])
# def getChats



# Create a chat
# @myApp.put("/chat/", response_model=list[ChatDTO.Chat])
# def createChat

# Delete a chat
# @myApp.delete("/{chat_id}", response_model=list[ChatDTO.Chat])
# def deleteChat


# @myApp.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
