from sqlalchemy import MetaData

from endpoints.chat.ChatModel import Chat
from endpoints.message.MessageModel import Message


def insert_test_data(session):
    # Insert data into 'chats'
    chats_data = [
        {'name': 'General Chat Test'},
        {'name': 'Tech Talk Test'}
    ]

    for data in chats_data:
        chat = Chat(name=data['name'])
        session.add(chat)

    # Commit the changes to 'chats'
    session.commit()

    # Insert data into 'messages'
    messages_data = [
        {'username': 'user1', 'message': 'This is a test message.', 'chat_id': 1},
        {'username': 'user2', 'message': 'Another test message in General Chat.', 'chat_id': 1},
        {'username': 'user3', 'message': 'A message in Tech Talk.', 'chat_id': 2}
    ]

    for data in messages_data:
        message = Message(username=data['username'],
                          message=data['message'],
                          chat_id=data['chat_id'])
        session.add(message)

    # Commit the changes to 'messages'
    session.commit()
