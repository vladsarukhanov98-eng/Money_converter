from fastapi.testclient import TestClient
from money_converter import app


client = TestClient(app)


def test_health():
    response = client.get("health")
    assert response.status_code == 200
    assert response.json() == {"Status": "OK"}


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Сервис работает"}


def test_convert_defaults():
    response = client.get("/convert")
    assert response.status_code == 200
    assert response.json()["Доллары"] == 0.0


def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert "Version" in response.json()