from endpoints.chat.ChatModel import Chat
from endpoints.message.MessageModel import Message


def insert_test_data(session, engine):
    # Define the data
    chats_data = [
        {'name': 'General Chat Test'},
        {'name': 'Tech Talk Test'}
    ]

    messages_data = [
        {'username': 'user1', 'message': 'This is a test message.', 'chat_id': 1},
        {'username': 'user2', 'message': 'Another test message in General Chat.', 'chat_id': 1},
        {'username': 'user3', 'message': 'A message in Tech Talk.', 'chat_id': 2}
    ]

    # Insert the data
    for data in chats_data:
        new_chat = Chat(**data)
        session.add(new_chat)

    for data in messages_data:
        # Ensure chat_id exists in the database or handle its creation here
        chat_id = data.pop('chat_id')
        chat = session.query(Chat).filter(Chat.id == chat_id).first()
        if not chat:
            chat = Chat(id=chat_id, name=f'Chat {chat_id}')  # Example of handling missing chat_id
            session.add(chat)
        new_message = Message(chat=chat, **data)
        session.add(new_message)

    session.commit()
