from pydantic import BaseModel, Field


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

    class Config:
        from_attributes = True  # Updated for Pydantic v2 and later
