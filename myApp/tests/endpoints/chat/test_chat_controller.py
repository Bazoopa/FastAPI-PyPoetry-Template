import logging  # Add logging for debugging purposes

import pandas as pd
import pytest
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


def test_root(setup_and_teardown):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bruce's App!"}
    print_database()


def test_create_chat(setup_and_teardown):
    response = client.post("/api/v1/chat/", json={"name": "my_first_test_two"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert "name" in data
    assert data["name"] == "my_first_test_two"
    logging.debug(f"Test create_chat response: {response.text}")
    logging.debug(f"Test create_chat data: {data}")
    print_database()


def test_get_chat(setup_and_teardown):
    response = client.get("/api/v1/chat/1")
    assert response.status_code == 200
    print_database()


def test_get_chats(setup_and_teardown):
    response = client.get("/api/v1/chats/")
    assert response.status_code == 200
    chats = response.json()
    print_database()


def test_delete_chat_by_id(setup_and_teardown):
    response = client.delete("/api/v1/chat/id-delete/1")
    assert response.status_code == 200


def test_delete_chat_by_name(setup_and_teardown):
    chat_name = "Tech Talk Test"
    response = client.delete(f"/api/v1/chat/name-delete/{chat_name}")
    assert response.status_code == 200
    deleted_chat = response.json()
    assert deleted_chat["name"] == chat_name


def test_update_chat_by_id(setup_and_teardown):
    updated_data = {"name": "Updated Chat Name"}
    response = client.put("/api/v1/chat/update/1", json=updated_data)
    assert response.status_code == 200
    updated_chat = response.json()
    assert updated_chat["name"] == "Updated Chat Name"
