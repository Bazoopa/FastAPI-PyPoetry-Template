from sqlalchemy import MetaData, Table


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

    # Define the tables
    metadata = MetaData()
    metadata.reflect(bind=engine)  # Bind metadata to the engine
    chats_table = metadata.tables['chats']
    messages_table = metadata.tables['messages']

    # Insert the data
    for data in chats_data:
        session.execute(chats_table.insert().values(data))

    for data in messages_data:
        session.execute(messages_table.insert().values(data))
