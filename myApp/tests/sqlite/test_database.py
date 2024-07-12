# database.py
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Create an engine to connect to the SQLite in-memory database
engine = create_engine('sqlite:///:memory:', echo=True)

# Define a metadata object to hold database schema information
metadata = MetaData()

# Define 'chats' table
chats_table = Table(
    'chats',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255), nullable=False)
)

# Define 'messages' table
messages_table = Table(
    'messages',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(255), nullable=False),
    Column('message', String(280), nullable=False),
    Column('chat_id', Integer, ForeignKey('chats.id', ondelete='CASCADE'))
)

# Create all tables in the engine
metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Insert data into 'chats'
chats_data = [
    {'name': 'General Chat Test'},
    {'name': 'Tech Talk Test'}
]

for data in chats_data:
    session.execute(chats_table.insert().values(data))

# Insert data into 'messages'
messages_data = [
    {'username': 'user1', 'message': 'This is a test message.', 'chat_id': 1},
    {'username': 'user2', 'message': 'Another test message in General Chat.', 'chat_id': 1},
    {'username': 'user3', 'message': 'A message in Tech Talk.', 'chat_id': 2}
]

for data in messages_data:
    session.execute(messages_table.insert().values(data))

# Commit the changes
session.commit()

# Close the session
session.close()

# Define Base for declarative models
Base = declarative_base()



