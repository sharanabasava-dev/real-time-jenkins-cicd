from app.app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Real-Time Jenkins CI/CD Pipeline Project" in response.data

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "UP"

def test_info():
    client = app.test_client()
    response = client.get("/api/info")
    assert response.status_code == 200
