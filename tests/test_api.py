"""
API Tests for Smart Study Planner

Tests FastAPI endpoints:
- Health check
- Schedule generation endpoint
"""

from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)


# --------------------------------------------------
# Test root endpoint
# --------------------------------------------------
def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert "Smart Study Planner" in response.json()["message"]


# --------------------------------------------------
# Test health endpoint
# --------------------------------------------------
def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


# --------------------------------------------------
# Test schedule generation API
# --------------------------------------------------
def test_generate_schedule():
    payload = {
        "daily_hours": 6,
        "tasks": [
            {
                "subject": "Math",
                "difficulty": 5,
                "hours_needed": 10,
                "deadline": "2026-06-10"
            },
            {
                "subject": "Physics",
                "difficulty": 4,
                "hours_needed": 8,
                "deadline": "2026-06-08"
            }
        ]
    }

    response = client.post("/api/v1/generate-schedule", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert "data" in data
    assert len(data["data"]) > 0
