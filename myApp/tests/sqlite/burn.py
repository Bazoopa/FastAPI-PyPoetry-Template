from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create an in-memory SQLite database
engine = create_engine('sqlite:///:memory:', echo=True)

# Create a base class for declarative ORM models
Base = declarative_base()

# Define a User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    fullname = Column(String)

    def __repr__(self):
        return f"<User(username='{self.username}', fullname='{self.fullname}')>"

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Add some test data
test_users = [
    User(username='john_doe', fullname='John Doe'),
    User(username='jane_smith', fullname='Jane Smith'),
    User(username='bob_jones', fullname='Bob Jones')
]

session.add_all(test_users)
session.commit()

# Query all users and print them
users = session.query(User).all()
for user in users:
    print(user)
