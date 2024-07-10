# from fastapi.testclient import TestClient
#
# from .main import app
#
# client = TestClient(app)
#
# def test_getChat(chat_id: int, db: Session = Depends(get_db)):
#     response = client.get("/items/foo", headers={"X-Token": "coneofsilence"})
#     assert response.status_code == 200
#     assert response.json() == {
#         "id": "foo",
#         "title": "Foo",
#         "description": "There goes my hero",
#     }
#
#
