import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from backend.services.explore_service import MarketExploreService
from backend.services.ipo_service import IPOService

def test_sectors():
    sectors = [
        "Information Technology",
        "Banking & Financial Services",
        "Automobile & Auto Components",
        "Oil, Gas & Consumable Fuels",
        "Pharmaceuticals & Healthcare",
        "Cement & Construction Materials",
        "Plastic and Polymers",
        "Textiles",
        "Water Distribution & Utilities",
        "water",
        "plastics",
        "cement",
        "textiles",
        "it",
        "banking",
        "auto"
    ]
    print("=== TESTING SECTOR STOCKS COUNTS ===")
    for s in sectors:
        res = MarketExploreService.get_sector_stocks(s)
        count = res["count"]
        print(f"Sector '{s}' -> Name: '{res['sector_name']}', Count: {count}")
        assert count >= 50, f"Sector {s} returned only {count} stocks, expected >= 50!"
    print(" All sectors successfully returned >= 50 stocks!\n")

def test_closed_ipos():
    print("=== TESTING CLOSED IPOS COUNT ===")
    closed_ipos = IPOService.get_all_ipos(status_filter="closed")
    summary = IPOService.get_summary_metrics()
    print(f"Total Closed IPOs returned: {len(closed_ipos)}")
    print(f"Summary metrics closed_count: {summary['closed_count']}")
    assert len(closed_ipos) >= 150, f"Expected at least 150 closed IPOs, got {len(closed_ipos)}"
    assert summary['closed_count'] >= 150, f"Expected summary.closed_count >= 150, got {summary['closed_count']}"
    print(" All closed IPO criteria successfully met (>= 150 items)!\n")

if __name__ == "__main__":
    test_sectors()
    test_closed_ipos()
