# test_database.py

import logging  # Add logging for debugging purposes

import pandas as pd
from database import get_db
from endpoints.base import Base
from main import app
from tests.sqlite.test_data import insert_test_data
from tests.sqlite.test_in_memory_database import client, engine, TestingSessionLocal


def print_database():
    table_name = 'chats'
    df = pd.read_sql_table(table_name, con=engine)
    print(df.head())


# Dependency to override the get_db dependency in the main app
def override_get_db():
    database = TestingSessionLocal()
    yield database
    database.close()


app.dependency_overrides[get_db] = override_get_db


def setup_function():
    logging.debug("Setting up test database...")
    Base.metadata.create_all(bind=engine)
    with TestingSessionLocal() as session:
        insert_test_data(session, engine)
        session.commit()
    logging.debug("Database tables created and data inserted.")


def teardown_function():
    logging.debug("Dropping test database tables...")
    Base.metadata.drop_all(bind=engine)
    logging.debug("Database tables dropped.")


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bruce's App!"}


def test_create_chat():
    response = client.post("/api/v1/chat/", json={"name": "my_first_test_two"})
    assert response.status_code == 200, response.text
    data = response.json()
    # Add assertions to validate the response and data as needed
    assert "name" in data
    assert data["name"] == "my_first_test_two"
    # Optionally, add logging to check the response and data if needed
    logging.debug(f"Test create_chat response: {response.text}")
    logging.debug(f"Test create_chat data: {data}")

    # Add more assertions as needed to validate the response


def test_get_chat():
    response = client.get("/api/v1/chat/1")
    assert response.status_code == 200


def test_get_chats():
    response = client.get("/api/v1/chats/")
    assert response.status_code == 200
    chats = response.json()
    assert len(chats) == 2  # Assuming there are 2 default chats in your test database


def test_delete_chat_by_id():
    # Assuming there is a chat with ID=1 in your initial setup
    response = client.delete("/api/v1/chat/id-delete/1")
    assert response.status_code == 200
    # deleted_chat = response.json()
    # assert deleted_chat["name"] == "General Chat"

#
#
# def test_delete_chat_by_name():
#     # Assuming there is a chat named "Tech Talk" in your initial setup
#     response = client.delete("/api/v1/chat/name-delete/Tech%20Talk")
#     assert response.status_code == 200
#     deleted_chat = response.json()
#     assert deleted_chat["name"] == "Tech Talk"
#
#
# def test_update_chat_by_id():
#     # Assuming there is a chat with ID=1 and you want to update its name
#     updated_data = {"name": "Updated Chat Name"}
#     response = client.put("/api/v1/chat/update/1", json=updated_data)
#     assert response.status_code == 200
#     updated_chat = response.json()
#     assert updated_chat["name"] == "Updated Chat Name"

# test_database.py
