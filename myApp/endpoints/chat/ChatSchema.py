import logging
from pydantic import BaseModel, ConfigDict

# Configure logging settings (optional)
logging.basicConfig(level=logging.DEBUG)  # Set the desired log level


class ChatBase(BaseModel):
    name: str


class ChatCreate(ChatBase):
    pass


class ChatUpdate(ChatBase):
    pass


class DBChat(ChatBase):
    id: int

    model_config = ConfigDict(from_attributes=True)  # Updated for Pydantic v2 and later
