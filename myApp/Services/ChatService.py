#Need to be able get all chats
#Need to be able to get a single chat
#Need to be able to delete a chat
#Need to be able to create a chat

#Get all chats
# def getChats

from sqlalchemy.orm import Session
from typing import List, Type
from myApp.DAOs import ChatDAO
from sqlalchemy.orm import Session

from myApp.DAOs import ChatDAO
import myApp.DTOs
from myApp.DAOs.ChatDAO import Chat


# Get single chat
def getChat(db: Session, chat_id: int):
    return db.query(ChatDAO.Chat).filter(ChatDAO.Chat.id == chat_id).first()


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()




# Create a chat

# def createChat


# Delete a chat

# def deleteChat
