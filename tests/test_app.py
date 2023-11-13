from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_product(mock_db_session):
    response = client.post(
        "/products/", json={"name": "Test Product", "description": "Test Description"}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["description"] == "Test Description"

    mock_db_session.add.assert_called()
    mock_db_session.commit.assert_called()
