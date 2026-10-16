"""
Unit and integration tests for Live IPO Service and endpoints.
"""
from fastapi.testclient import TestClient
from main import app
from services.ipo_service import IPOService

client = TestClient(app)

def test_get_all_ipos():
    ipos = IPOService.get_all_ipos()
    assert len(ipos) >= 5
    # Verify properties on the first returned live IPO
    first = ipos[0]
    assert "name" in first
    assert "status" in first
    assert "issue_price" in first
    assert "gmp_closing_percent" in first
    assert "subscription" in first


def test_ipo_filters():
    # Filter by SME
    sme = IPOService.get_all_ipos(type_filter="sme")
    assert all(i["ipo_type"] == "SME" for i in sme)


def test_ipo_summary_metrics():
    summary = IPOService.get_summary_metrics()
    assert "open_count" in summary
    assert "upcoming_count" in summary
    assert "last_updated" in summary


def test_api_ipo_endpoints():
    res = client.get("/api/ipo/summary")
    assert res.status_code == 200
    assert "open_count" in res.json()

    res_list = client.get("/api/ipo/list?status=all")
    assert res_list.status_code == 200
    data = res_list.json()
    assert data["count"] > 0
    first_id = data["ipos"][0]["id"]

    res_single = client.get(f"/api/ipo/{first_id}")
    assert res_single.status_code == 200
    assert "name" in res_single.json()

    # Compare endpoint
    if len(data["ipos"]) >= 2:
        id1 = data["ipos"][0]["id"]
        id2 = data["ipos"][1]["id"]
        res_cmp = client.get(f"/api/ipo/compare?ids={id1},{id2}")
        assert res_cmp.status_code == 200
        assert res_cmp.json()["count"] == 2
