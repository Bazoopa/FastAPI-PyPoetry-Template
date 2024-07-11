# test_database.py

import logging  # Add logging for debugging purposes
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from main import app
from database import get_db, Base

client = TestClient(app)

# SQLite in-memory database URL for testing
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    return TestingSessionLocal()


app.dependency_overrides[get_db] = override_get_db


def override_get_db():
    return TestingSessionLocal()


app.dependency_overrides[get_db] = override_get_db


def setup_function():
    logging.debug("Setting up test database...")
    Base.metadata.create_all(bind=engine)
    logging.debug("Database tables created.")


def teardown_function():
    Base.metadata.drop_all(bind=engine)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bruce's App!"}


def test_create_chat():
    response = client.post("/api/v1/chat/", json={"name": "my_first_test"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "my_first_test"

    # Optionally, add logging to check the response and data if needed
    logging.debug(f"Test create_chat response: {response.text}")
    logging.debug(f"Test create_chat data: {data}")

    # Add more assertions as needed to validate the response
