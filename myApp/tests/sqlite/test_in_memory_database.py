# # test_memory_database.py
#
# from fastapi.testclient import TestClient
# from sqlalchemy import create_engine, StaticPool
# from sqlalchemy.orm import sessionmaker
# from main import app
#
# # Setup the TestClient
# client = TestClient(app)
#
# # Setup the in-memory SQLite database for testing
# DATABASE_URL = "sqlite:///:memory:"
# engine = create_engine(
#     DATABASE_URL,
#     connect_args={
#         "check_same_thread": False,
#     },
#     poolclass=StaticPool,
# )
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
#
#
