python -m pip install pytest httpx

- pytest — tests run karta hai.
- httpx — FastAPI app ko HTTP requests ke through test karne mein help karta hai.
Install hone ke baad requirements.txt mein bhi in dependencies ko add karenge.
Step 2 — First test file banao
Tumhare tests/ folder mein test_health.py file banao:

devops-control-center/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── services.py
│   └── routes/
│       ├── health.py
│       └── servers.py
├── tests/
│   └── test_health.py
├── servers.json
└── requirements.txt

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "app": "DevOps Control Center"
    }