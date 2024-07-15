import logging
from pydantic import BaseModel, ConfigDict


logging.basicConfig(level=logging.DEBUG)


class ChatBase(BaseModel):
    name: str


class ChatCreate(ChatBase):
    pass


class ChatUpdate(ChatBase):
    pass


class DBChat(ChatBase):
    id: int

    model_config = ConfigDict(from_attributes=True)  # Updated for Pydantic v2 and later
