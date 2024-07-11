# # test_main.py
#
# import pytest
# from fastapi.testclient import TestClient
# from main import app
#
# SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///:memory:"
#
# client = TestClient(app)
#
#
# # Test cases for GET /
# def test_root():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Bruce's App!"}
#
#
# # Test cases for GET /api/v1/chat/{chat_id}
# def test_get_chat():
#     response = client.get("/api/v1/chat/1")
#     assert response.status_code == 200
#     # Assert based on expected response
#
#
# #
# # Test cases for GET /api/v1/chats/
# def test_get_chats():
#     response = client.get("/api/v1/chats/")
#     assert response.status_code == 200
#     # Assert based on expected response
# #
# # # Test cases for POST /api/v1/chat/
# # def test_create_chat():
# #     chat_data = {"id": "test_chat", "name": "Test Chat", "description": "Test Description"}
# #     response = client.post("/api/v1/chat/", json=chat_data)
# #     assert response.status_code == 200
# #     # Assert based on expected response
# #
# # # Test cases for DELETE /api/v1/chat/id-delete/{chat_id}
# # def test_delete_chat_by_id():
# #     response = client.delete("/api/v1/chat/id-delete/1")
# #     assert response.status_code == 200
# #     # Assert based on expected response
# #
# # # Test cases for DELETE /api/v1/chat/name-delete/{chat_name}
# # def test_delete_chat_by_name():
# #     response = client.delete("/api/v1/chat/name-delete/test_chat")
# #     assert response.status_code == 200
# #     # Assert based on expected response
# #
# # # Test cases for PUT /api/v1/chat/update/{chat_id}
# # def test_update_chat_by_id():
# #     chat_id = 1
# #     update_data = {"name": "Updated Chat Name"}
# #     response = client.put(f"/api/v1/chat/update/{chat_id}", json=update_data)
# #     assert response.status_code == 200
# #     # Assert based on expected response
