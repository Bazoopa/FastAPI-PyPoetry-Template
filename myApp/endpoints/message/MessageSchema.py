from pydantic import BaseModel, ConfigDict, Field


class MessageBase(BaseModel):
    username: str
    message: str


class MessageCreate(MessageBase):
    chat_id: int


class MessageUpdate(MessageBase):
    pass


class Message(MessageBase):
    id: int
    chat_id: int

    model_config = ConfigDict(from_attributes=True)  # Updated for Pydantic v2 and later
