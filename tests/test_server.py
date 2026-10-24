from fastapi.testclient import TestClient
from app.main import app
from pathlib import Path
import pytest
import uuid
from app.services import server_analyzer

client = TestClient(app)

@pytest.fixture
def restore_servers_json():
    file_path = Path(__file__).resolve().parent.parent / "servers.json"
    original_data = file_path.read_text(encoding="utf-8")

    yield

    file_path.write_text(original_data, encoding="utf-8")

def test_get_servers():
    response = client.get("/servers")

    assert response.status_code == 200

    data = response.json()

    assert "total_servers" in data
    assert "running_servers" in data
    assert "stopped_servers" in data
    assert "high_cpu_servers" in data

def test_create_server(restore_servers_json):
    server_name = f"pytest-{uuid.uuid4().hex[:8]}"

    response = client.post(
        "/servers",
        json={
            "name": server_name,
            "status": "running",
            "cpu": 25.5
        }
    )

    assert response.status_code == 200
    assert response.json()["server"]["name"] == server_name

def test_duplicate_server(restore_servers_json):
    server_data = {
        "name": f"duplicate-{uuid.uuid4().hex[:8]}",
        "status": "running",
        "cpu": 25.5
    }

    first_response = client.post("/servers", json=server_data)
    second_response = client.post("/servers", json=server_data)

    assert first_response.status_code == 200
    assert second_response.status_code == 409

def test_update_server(restore_servers_json):
    server_data = {
        "name": f"patch-{uuid.uuid4().hex[:8]}",
        "status": "running",
        "cpu": 25.5
    }

    create_response = client.post("/servers", json=server_data)
    assert create_response.status_code == 200

    update_response = client.patch(
        f"/servers/{server_data['name']}",
        json={"cpu": 90.0}
    )

    assert update_response.status_code == 200
    assert update_response.json()["server"]["cpu"] == 90.0

def test_delete_server(restore_servers_json):
    server_data = {
        "name": f"delete-{uuid.uuid4().hex[:8]}",
        "status": "running",
        "cpu": 25.5
    }

    create_response = client.post("/servers", json=server_data)
    assert create_response.status_code == 200

    delete_response = client.delete(
        f"/servers/{server_data['name']}"
    )

    assert delete_response.status_code == 200
    assert delete_response.json()["server"]["name"] == server_data["name"]

    get_response = client.get(
        f"/servers/{server_data['name']}"
    )

    assert get_response.status_code == 404

def test_update_nonexistent_server():
    response = client.patch(
        "/servers/server-does-not-exist",
        json={"cpu": 90.0}
    )

    assert response.status_code == 404

def test_delete_nonexistent_server():
    response = client.delete(
        "/servers/server-does-not-exist"
    )

    assert response.status_code == 404

def test_update_server_empty_body(restore_servers_json):
    server_data = {
        "name": f"empty-{uuid.uuid4().hex[:8]}",
        "status": "running",
        "cpu": 25.5
    }

    client.post("/servers", json=server_data)

    response = client.patch(
        f"/servers/{server_data['name']}",
        json={}
    )

    assert response.status_code == 400

from app.services import server_analyzer

def test_cpu_threshold():
    servers = [
        {"name": "web-01", "status": "running", "cpu": 75},
        {"name": "web-02", "status": "running", "cpu": 85},
        {"name": "db-01", "status": "running", "cpu": 95}
    ]

    result = server_analyzer(servers, cpu_threshold=90)

    assert result["high_cpu_servers"] == ["db-01"]
#     Ek baar flow revise karo
# - yield se pehle → original data save hota hai.
# - yield → test execute hota hai.
# - yield ke baad → cleanup hota hai, original data restore hota hai.