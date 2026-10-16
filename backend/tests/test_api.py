"""
API endpoint integration tests using FastAPI TestClient.
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_search():
    res = client.get("/api/search?q=INFY")
    assert res.status_code == 200
    data = res.json()
    assert "results" in data
    assert any("INFY.NS" in r["symbol"] for r in data["results"])

def test_search_generic_symbol():
    # User types an unlisted/smallcap ticker e.g. "MYSTOCK"
    res = client.get("/api/search?q=MYSTOCK")
    assert res.status_code == 200
    data = res.json()
    assert len(data["results"]) > 0
    symbols = [r["symbol"] for r in data["results"]]
    assert "MYSTOCK.NS" in symbols
