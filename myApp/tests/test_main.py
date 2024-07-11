# test_database.py

import logging  # Add logging for debugging purposes
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, MetaData, StaticPool
from sqlalchemy.orm import sessionmaker

from main import app
from database import Base, get_db

# Setup the TestClient
client = TestClient(app)

# Setup the in-memory SQLite database for testing
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False,
    },
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to override the get_db dependency in the main app
def override_get_db():
    database = TestingSessionLocal()
    yield database
    database.close()


app.dependency_overrides[get_db] = override_get_db


def setup_function():
    logging.debug("Setting up test database...")
    Base.metadata.create_all(bind=engine)
    logging.debug("Database tables created.")


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
