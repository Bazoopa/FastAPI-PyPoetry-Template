import logging  # Add logging for debugging purposes
import pandas as pd
import pytest
from database.database import get_db
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


@pytest.fixture(scope="function")
def setup_and_teardown():
    logging.debug("Setting up test database...")
    Base.metadata.create_all(bind=engine)
    with TestingSessionLocal() as session:
        insert_test_data(session)
        session.commit()
    yield
    logging.debug("Dropping test database tables...")
    Base.metadata.drop_all(bind=engine)
    logging.debug("Database tables dropped.")


def test_get_message(setup_and_teardown):
    response = client.get("/api/v1/message/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["username"] == "user1"
    assert data["message"] == "This is a test message."
    logging.debug(f"Test get_message response: {response.text}")


def test_get_messages(setup_and_teardown):
    chat_id = 1
    response = client.get(f"/api/v1/messages/{chat_id}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["username"] == "user1"
    assert data[0]["message"] == "This is a test message."
    assert data[1]["username"] == "user2"
    assert data[1]["message"] == "Another test message in General Chat."
    logging.debug(f"Test get_messages response: {response.text}")


def test_create_message(setup_and_teardown):
    message_data = {"chat_id": 1, "username": "user4", "message": "New test message"}
    response = client.post("/api/v1/message/", json=message_data)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["username"] == "user4"
    assert data["message"] == "New test message"
    logging.debug(f"Test create_message response: {response.text}")


def test_delete_message(setup_and_teardown):
    response = client.delete("/api/v1/message/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["username"] == "user1"
    assert data["message"] == "This is a test message."
    logging.debug(f"Test delete_message response: {response.text}")
