"""
FastAPI Server for Indian Stock Market Valuation & Analysis.
Exposes REST endpoints for search, valuation reports, screener, and indices.
"""
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List
import logging
from services.ticker_catalog import search_stocks, normalize_ticker
from services.stock_service import StockService
from services.ipo_service import IPOService
from services.explore_service import MarketExploreService

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("stock_app")

app = FastAPI(
    title="Stocks Suggestions - Dhakrey - Indian Stock & IPO Market Valuation API",
    description="Analyzes NSE and BSE listed stocks and live IPOs using a quantitative hybrid fundamental-technical valuation model to determine whether a stock is a Best Buy, At Fair Price, or Currently Expensive.",
    version="1.0.0"
)

# Enable CORS for local Vite frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "app": "Stocks Suggestions - Dhakrey - Indian Stock & IPO Valuation Engine",
        "status": "online",
        "coverage": ["NSE", "BSE"],
        "docs_url": "/docs"
    }


@app.get("/api/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/search")
def search(q: str = Query(default="", min_length=0, description="Company name or ticker symbol")):
    """
    Search stocks across NSE and BSE.
    Supports autocomplete, prefix matching, and arbitrary Indian stock tickers.
    """
    results = search_stocks(query=q, limit=15)
    return {"query": q, "count": len(results), "results": results}


@app.get("/api/stock/{symbol}")
def get_stock_analysis(symbol: str):
    """
    Get comprehensive valuation analysis, financial health scorecard,
    technicals (RSI, 50/200 DMA), and the final investment verdict:
    'BEST BUY', 'AT FAIR PRICE', or 'CURRENTLY EXPENSIVE'.
    """
    clean_sym = normalize_ticker(symbol)
    logger.info(f"Analyzing stock: {clean_sym}")

    data = StockService.get_stock_data(clean_sym)
    if not data:
        raise HTTPException(
            status_code=404,
            detail=f"Stock data for '{symbol}' could not be retrieved. Please check that the ticker is active on NSE (.NS) or BSE (.BO)."
        )

    return data


@app.get("/api/screener")
def get_screener(category: str = Query(default="nifty50", description="Category: nifty50, niftynext50, tech, banking, auto")):
    """
    Returns screened stocks with live valuation badges and margin of safety.
    """
    items = StockService.get_screener_results(category=category, limit=25)
    return {
        "category": category,
        "count": len(items),
        "stocks": items
    }


@app.get("/api/indices")
def get_top_indices():
    """
    Returns quick snapshot of key Indian benchmark indices.
    """
    indices = [
        {"symbol": "^NSEI", "name": "NIFTY 50", "exchange": "NSE"},
        {"symbol": "^BSESN", "name": "BSE SENSEX", "exchange": "BSE"},
        {"symbol": "^NSEBANK", "name": "NIFTY BANK", "exchange": "NSE"},
        {"symbol": "^CNXIT", "name": "NIFTY IT", "exchange": "NSE"},
    ]
    
    results = []
    for idx in indices:
        try:
            import yfinance as yf
            t = yf.Ticker(idx["symbol"])
            fast_info = t.fast_info
            price = fast_info.last_price or 0.0
            prev = fast_info.previous_close or price
            chg = round(price - prev, 2)
            chg_pct = round((chg / prev) * 100, 2) if prev > 0 else 0.0
            results.append({
                "symbol": idx["symbol"],
                "name": idx["name"],
                "price": round(price, 2),
                "change": chg,
                "change_percent": chg_pct
            })
        except Exception:
            continue

    return {"indices": results}


@app.get("/api/market/explore")
def get_market_explore():
    """
    Returns market explore data:
    1. Most traded stocks (Top 10 + see more)
    2. Top movers today (Gainers, Losers, Volume Shockers with 1D sparkline)
    3. Sectors trending today (Gainers/Losers visual ratio and 1D price change)
    Following Groww design layout.
    """
    return MarketExploreService.get_explore_data()


@app.get("/api/market/sector/{sector_name}")
def get_market_sector_stocks(sector_name: str):
    """
    Returns the list of stocks in a specific sector with 1D change, volume,
    1W volume anomaly %, 52W high/low performance slider, RSI, and MACD.
    """
    return MarketExploreService.get_sector_stocks(sector_name)


@app.get("/api/ipo/summary")
def get_ipo_summary(
    type: str = Query(default="all", description="Type: all, mainboard, sme")
):
    """
    Returns dashboard summary metrics across Indian IPOs:
    Open count, upcoming count, average listing gain %, best & worst performers.
    Supports filtering metrics by IPO type (all, mainboard, sme).
    """
    return IPOService.get_summary_metrics(type_filter=type)


@app.get("/api/ipo/list")
def get_ipo_list(
    status: str = Query(default="all", description="Status: all, open, upcoming, closed, listed"),
    type: str = Query(default="all", description="Type: all, mainboard, sme"),
    refresh: bool = Query(default=False, description="Force fetch fresh live market data")
):
    """
    Returns live filtered IPOs with closing-day GMP, day-by-day subscriptions,
    retail 1-lot profit, listing gains, and recommendations.
    """
    ipos = IPOService.get_all_ipos(status_filter=status, type_filter=type, refresh=refresh)
    return {
        "status_filter": status,
        "type_filter": type,
        "count": len(ipos),
        "ipos": ipos
    }


@app.get("/api/ipo/compare")
def compare_ipos(ids: str = Query(..., description="Comma-separated IPO IDs, e.g. bajaj-housing-finance,waaree-energies")):
    """
    Compare 2 or more IPOs side-by-side.
    """
    id_list = [i.strip() for i in ids.split(",") if i.strip()]
    compared = IPOService.compare_ipos(id_list)
    return {"count": len(compared), "ipos": compared}


@app.get("/api/ipo/{ipo_id}")
def get_ipo_detail(ipo_id: str):
    """
    Get detailed research report for an IPO.
    """
    ipo = IPOService.get_ipo_by_id(ipo_id)
    if not ipo:
        raise HTTPException(status_code=404, detail=f"IPO with ID '{ipo_id}' not found.")
    return ipo


# AWS Lambda serverless handler for API Gateway integration
try:
    from mangum import Mangum
    handler = Mangum(app, lifespan="off")
except ImportError:
    handler = None


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

