import logging
from pydantic import BaseModel

# Configure logging settings (optional)
logging.basicConfig(level=logging.DEBUG)  # Set the desired log level


class ChatBase(BaseModel):
    name: str


class ChatCreate(ChatBase):
    pass


class Chat(ChatBase):
    id: int

    class Config:
        from_attributes = True  # Updated for Pydantic v2 and later
