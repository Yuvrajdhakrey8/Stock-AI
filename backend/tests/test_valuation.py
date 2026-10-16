"""
Unit tests for the Hybrid Valuation and Decision Engine.
"""
import pytest
import pandas as pd
import numpy as np
from services.valuation_engine import ValuationEngine
from services.ticker_catalog import normalize_ticker, search_stocks


def test_normalize_ticker():
    assert normalize_ticker("TCS") == "TCS.NS"
    assert normalize_ticker("tcs.ns") == "TCS.NS"
    assert normalize_ticker("500325") == "500325.BO"
    assert normalize_ticker("500325.BO") == "500325.BO"
    assert normalize_ticker("RELIANCE") == "RELIANCE.NS"


def test_search_stocks():
    res = search_stocks("Tata")
    assert len(res) > 0
    symbols = [r["symbol"] for r in res]
    assert any("TCS.NS" in s or "TATAMOTORS.NS" in s for s in symbols)


def test_graham_number():
    # EPS = 100, Book value = 200 => sqrt(22.5 * 100 * 200) = sqrt(450000) = 670.82
    graham = ValuationEngine.calculate_graham_number(eps=100.0, bvps=200.0)
    assert graham is not None
    assert round(graham, 1) == 670.8

    # Negative EPS or BVPS should return None
    assert ValuationEngine.calculate_graham_number(eps=-10, bvps=50) is None
    assert ValuationEngine.calculate_graham_number(eps=10, bvps=-50) is None


def test_dcf_fair_value():
    dcf = ValuationEngine.calculate_dcf_fair_value(
        fcf_per_share=50.0,
        eps=50.0,
        growth_rate=0.12,
        discount_rate=0.115,
        terminal_rate=0.055
    )
    assert dcf is not None
    assert dcf > 50.0


def test_rsi_calculation():
    # Generate 30 prices with steady increase => RSI should be high
    prices = pd.Series([100 + i * 2 for i in range(30)])
    rsi = ValuationEngine.calculate_rsi(prices)
    assert rsi is not None
    assert rsi > 70.0  # Overbought


def test_verdict_best_buy():
    # Mock deeply undervalued company with healthy balance sheet & low RSI
    history_df = pd.DataFrame({
        "Close": [100.0 - i * 0.5 for i in range(50)]  # downward slope -> lower RSI
    })
    info = {
        "currentPrice": 80.0,
        "trailingPE": 12.0,
        "pegRatio": 0.8,
        "returnOnEquity": 0.22,
        "trailingEps": 12.0,
        "bookValue": 70.0,
        "debtToEquity": 15.0,  # low debt
        "fiftyTwoWeekHigh": 140.0,
        "fiftyTwoWeekLow": 75.0,
    }
    eval_result = ValuationEngine.evaluate_stock(current_price=80.0, info=info, history_df=history_df)
    assert eval_result["verdict"] == "BEST BUY"
    assert eval_result["margin_of_safety_percent"] > 0


def test_verdict_expensive():
    # Mock extremely stretched company with PE 100, RSI high
    history_df = pd.DataFrame({
        "Close": [100.0 + i * 3 for i in range(50)]  # sharp upward surge -> overbought RSI
    })
    info = {
        "currentPrice": 250.0,
        "trailingPE": 95.0,
        "pegRatio": 3.8,
        "returnOnEquity": 0.05,
        "trailingEps": 2.5,
        "bookValue": 20.0,
        "debtToEquity": 250.0,  # high debt
        "fiftyTwoWeekHigh": 255.0,
        "fiftyTwoWeekLow": 80.0,
    }
    eval_result = ValuationEngine.evaluate_stock(current_price=250.0, info=info, history_df=history_df)
    assert eval_result["verdict"] == "CURRENTLY EXPENSIVE"
    assert eval_result["margin_of_safety_percent"] < 0
