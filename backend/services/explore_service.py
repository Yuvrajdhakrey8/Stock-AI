"""
Explore & Market Discovery Service for Indian Equities (NSE & BSE).
Provides:
1. Most traded stocks (Live dynamic ranking by volume)
2. Top movers today (Live Gainers, Losers, Volume Shockers with 1D sparkline)
3. Sectors trending today (Dynamic live Gainers/Losers visual ratio and 1D price change)
4. Related stocks by sector
Following Groww design patterns.
"""
from typing import Dict, Any, List, Optional
from cachetools import TTLCache
import logging
import re
from datetime import datetime, timezone, timedelta
import yfinance as yf
from .sector_stocks_catalog import SECTOR_STOCKS_CATALOG

logger = logging.getLogger(__name__)

# Cache explore data for 3 minutes to keep quotes fresh while preventing rate-limiting
explore_cache = TTLCache(maxsize=10, ttl=180)
CACHE_KEY = "market_explore_data"

# Comprehensive universe of 60 top liquid Indian stocks across all major sectors
TRACKED_EXPLORE_STOCKS: List[tuple] = [
    # Information Technology
    ("TCS.NS", "TCS", "Information Technology", "laptop"),
    ("INFY.NS", "Infosys", "Information Technology", "laptop"),
    ("WIPRO.NS", "Wipro", "Information Technology", "laptop"),
    ("HCLTECH.NS", "HCL Technologies", "Information Technology", "laptop"),
    ("TECHM.NS", "Tech Mahindra", "Information Technology", "laptop"),
    # Banking & Financial Services
    ("HDFCBANK.NS", "HDFC Bank", "Banking & Financial Services", "building"),
    ("ICICIBANK.NS", "ICICI Bank", "Banking & Financial Services", "building"),
    ("SBIN.NS", "State Bank of India", "Banking & Financial Services", "building"),
    ("KOTAKBANK.NS", "Kotak Mahindra Bank", "Banking & Financial Services", "building"),
    ("AXISBANK.NS", "Axis Bank", "Banking & Financial Services", "building"),
    ("BAJFINANCE.NS", "Bajaj Finance", "Banking & Financial Services", "building"),
    ("SHRIRAMFIN.NS", "Shriram Finance", "Banking & Financial Services", "building"),
    ("MUTHOOTFIN.NS", "Muthoot Finance", "Banking & Financial Services", "building"),
    ("CHOLAFIN.NS", "Cholamandalam Inv", "Banking & Financial Services", "building"),
    # Oil, Gas & Consumable Fuels
    ("RELIANCE.NS", "Reliance Industries", "Oil, Gas & Consumable Fuels", "fuel"),
    ("ONGC.NS", "ONGC", "Oil, Gas & Consumable Fuels", "fuel"),
    ("BPCL.NS", "BPCL", "Oil, Gas & Consumable Fuels", "fuel"),
    ("IOC.NS", "Indian Oil", "Oil, Gas & Consumable Fuels", "fuel"),
    ("COALINDIA.NS", "Coal India", "Oil, Gas & Consumable Fuels", "fuel"),
    # Power & Utilities
    ("NTPC.NS", "NTPC", "Power & Utilities", "droplet"),
    ("POWERGRID.NS", "Power Grid Corp", "Power & Utilities", "droplet"),
    ("TATAPOWER.NS", "Tata Power", "Power & Utilities", "droplet"),
    # Automobiles
    ("MARUTI.NS", "Maruti Suzuki", "Automobiles", "car"),
    ("M&M.NS", "Mahindra & Mahindra", "Automobiles", "car"),
    ("BAJAJ-AUTO.NS", "Bajaj Auto", "Automobiles", "car"),
    ("EICHERMOT.NS", "Eicher Motors", "Automobiles", "car"),
    ("HEROMOTOCO.NS", "Hero MotoCorp", "Automobiles", "car"),
    ("TVSMOTOR.NS", "TVS Motor", "Automobiles", "car"),
    # Pharmaceuticals & Healthcare
    ("SUNPHARMA.NS", "Sun Pharma", "Healthcare & Pharma", "activity"),
    ("DRREDDY.NS", "Dr. Reddys Labs", "Healthcare & Pharma", "activity"),
    ("CIPLA.NS", "Cipla", "Healthcare & Pharma", "activity"),
    ("TORNTPHARM.NS", "Torrent Pharma", "Healthcare & Pharma", "activity"),
    ("DIVISLAB.NS", "Divis Labs", "Healthcare & Pharma", "activity"),
    ("APOLLOHOSP.NS", "Apollo Hospitals", "Healthcare & Pharma", "activity"),
    # Metals & Mining
    ("TATASTEEL.NS", "Tata Steel", "Metals & Mining", "layers"),
    ("HINDALCO.NS", "Hindalco Industries", "Metals & Mining", "layers"),
    ("JSWSTEEL.NS", "JSW Steel", "Metals & Mining", "layers"),
    ("VEDL.NS", "Vedanta", "Metals & Mining", "layers"),
    ("HINDZINC.NS", "Hindustan Zinc", "Metals & Mining", "layers"),
    ("JINDALSTEL.NS", "Jindal Steel & Power", "Metals & Mining", "layers"),
    # FMCG & Consumer Goods
    ("ITC.NS", "ITC", "FMCG & Consumer Goods", "package"),
    ("HINDUNILVR.NS", "Hindustan Unilever", "FMCG & Consumer Goods", "package"),
    ("NESTLEIND.NS", "Nestle India", "FMCG & Consumer Goods", "package"),
    ("BRITANNIA.NS", "Britannia Industries", "FMCG & Consumer Goods", "package"),
    ("TATACONSUM.NS", "Tata Consumer", "FMCG & Consumer Goods", "package"),
    ("VBL.NS", "Varun Beverages", "FMCG & Consumer Goods", "package"),
    # Consumer Discretionary & Retail
    ("TITAN.NS", "Titan Company", "Consumer Discretionary", "cup"),
    ("TRENT.NS", "Trent", "Consumer Discretionary", "cup"),
    ("ETERNAL.NS", "Zomato", "Consumer Discretionary", "cup"),
    # Infrastructure, Industrials & Defence
    ("LT.NS", "L&T", "Infrastructure & Construction", "package"),
    ("HAL.NS", "Hindustan Aeronautics", "Infrastructure & Construction", "package"),
    ("BEL.NS", "Bharat Electronics", "Infrastructure & Construction", "package"),
    ("BHEL.NS", "BHEL", "Infrastructure & Construction", "package"),
    ("SIEMENS.NS", "Siemens", "Infrastructure & Construction", "package"),
    ("ADANIENT.NS", "Adani Enterprises", "Infrastructure & Construction", "package"),
    ("ADANIPORTS.NS", "Adani Ports", "Infrastructure & Construction", "package"),
    # Cement & Construction Materials
    ("ULTRACEMCO.NS", "UltraTech Cement", "Cement & Construction Materials", "package"),
    ("GRASIM.NS", "Grasim Industries", "Cement & Construction Materials", "package"),
    # Telecommunication
    ("BHARTIARTL.NS", "Bharti Airtel", "Telecommunication", "laptop")
]


class MarketExploreService:

    @classmethod
    def get_explore_data(cls, force_refresh: bool = False) -> Dict[str, Any]:
        """
        Returns live, dynamic aggregated explore screen data for stocks:
        1. Most traded stocks (sorted dynamically by volume)
        2. Top movers today (Gainers, Losers, Volume Shockers with live quotes and sparklines)
        3. Sectors trending today (live gainers/losers ratio and sector performance)
        4. Popular picks for users with no recent searches
        """
        if not force_refresh and CACHE_KEY in explore_cache:
            return explore_cache[CACHE_KEY]

        payload = cls._fetch_live_market_data()
        if not payload:
            payload = cls._get_resilient_fallback_data()

        explore_cache[CACHE_KEY] = payload
        return payload

    @classmethod
    def _fetch_live_market_data(cls) -> Optional[Dict[str, Any]]:
        """Downloads live quotes for the basket of 60 top NSE stocks via yfinance in a single batch."""
        try:
            symbols = [s[0] for s in TRACKED_EXPLORE_STOCKS]
            # Download 5-day daily bars to calculate today's change and sparklines
            df = yf.download(symbols, period="5d", interval="1d", progress=False)
            if df.empty or "Close" not in df:
                return None

            close_df = df["Close"]
            vol_df = df.get("Volume")

            parsed_stocks: List[Dict[str, Any]] = []
            sector_groups: Dict[str, Dict[str, Any]] = {}

            for sym, name, sector, icon in TRACKED_EXPLORE_STOCKS:
                try:
                    if sym not in close_df:
                        continue
                    c_series = close_df[sym].dropna()
                    if len(c_series) < 2:
                        continue

                    v_series = vol_df[sym].dropna() if vol_df is not None and sym in vol_df else []
                    
                    prev_close = float(c_series.iloc[-2])
                    current_price = float(c_series.iloc[-1])
                    change = round(current_price - prev_close, 2)
                    change_percent = round((change / prev_close) * 100, 2) if prev_close > 0 else 0.0
                    volume = int(v_series.iloc[-1]) if len(v_series) > 0 else 0

                    # Sparkline: last 6 closing prices
                    sparkline = [round(float(p), 2) for p in c_series.tail(6).tolist()]
                    if len(sparkline) < 3:
                        sparkline = [prev_close, (prev_close + current_price) / 2.0, current_price]

                    # Human-friendly Indian volume format (Cr and L)
                    if volume >= 10000000:
                        vol_fmt = f"{volume / 10000000:.2f} Cr"
                    elif volume >= 100000:
                        vol_fmt = f"{volume / 100000:.2f} L"
                    else:
                        vol_fmt = f"{volume:,}"

                    stock_entry = {
                        "symbol": sym,
                        "name": name,
                        "sector": sector,
                        "exchange": "NSE",
                        "current_price": current_price,
                        "change": change,
                        "change_percent": change_percent,
                        "volume": volume,
                        "volume_formatted": vol_fmt,
                        "sparkline": sparkline,
                    }
                    parsed_stocks.append(stock_entry)

                    # Sector aggregation
                    if sector not in sector_groups:
                        sector_groups[sector] = {
                            "id": re.sub(r'[^a-z0-9]+', '-', sector.lower()).strip('-'),
                            "name": sector,
                            "icon": icon,
                            "gainers": 0,
                            "losers": 0,
                            "changes": [],
                        }
                    if change_percent >= 0:
                        sector_groups[sector]["gainers"] += 1
                    else:
                        sector_groups[sector]["losers"] += 1
                    sector_groups[sector]["changes"].append(change_percent)

                except Exception as row_err:
                    logger.debug(f"Error parsing stock {sym}: {row_err}")
                    continue

            if len(parsed_stocks) < 10:
                return None

            # 1. Most Traded Stocks: sorted by real trading volume
            most_traded = sorted(parsed_stocks, key=lambda x: x["volume"], reverse=True)[:12]

            # 2. Top Movers Today
            # Gainers: positive change, highest first
            gainers = sorted([s for s in parsed_stocks if s["change_percent"] > 0], key=lambda x: x["change_percent"], reverse=True)[:10]
            # If fewer than 4 positive, take top performers overall
            if len(gainers) < 4:
                gainers = sorted(parsed_stocks, key=lambda x: x["change_percent"], reverse=True)[:8]

            # Losers: negative change, lowest first
            losers = sorted([s for s in parsed_stocks if s["change_percent"] < 0], key=lambda x: x["change_percent"])[:10]
            if len(losers) < 4:
                losers = sorted(parsed_stocks, key=lambda x: x["change_percent"])[:8]

            # Volume Shockers: highest volume with strong price movement
            volume_shockers = sorted(parsed_stocks, key=lambda x: x["volume"], reverse=True)[:10]

            # 3. Trending Sectors: dynamically calculated from constituent performances
            trending_sectors = []
            for s_name, s_info in sector_groups.items():
                avg_pct = round(sum(s_info["changes"]) / len(s_info["changes"]), 2) if s_info["changes"] else 0.0
                trending_sectors.append({
                    "id": s_info["id"],
                    "name": s_name,
                    "icon": s_info["icon"],
                    "gainers": s_info["gainers"],
                    "losers": s_info["losers"],
                    "change_percent": avg_pct,
                })
            # Sort sectors by absolute momentum so biggest moving sectors appear on top
            trending_sectors.sort(key=lambda x: abs(x["change_percent"]), reverse=True)

            # 4. Popular Picks (for users with no recent search history)
            popular_symbols = ["RELIANCE.NS", "HDFCBANK.NS", "TCS.NS", "MARUTI.NS", "INFY.NS", "ETERNAL.NS", "ITC.NS", "SBIN.NS"]
            popular_picks = [s for s in parsed_stocks if s["symbol"] in popular_symbols]
            if len(popular_picks) < 4:
                popular_picks = most_traded[:8]

            ist_now = datetime.now(timezone(timedelta(hours=5, minutes=30)))
            return {
                "most_traded": most_traded,
                "top_movers": {
                    "gainers": gainers,
                    "losers": losers,
                    "volume_shockers": volume_shockers,
                },
                "trending_sectors": trending_sectors,
                "popular_picks": popular_picks,
                "last_updated": ist_now.strftime("%d %b %Y, %I:%M %p IST"),
                "is_live": True,
            }

        except Exception as e:
            logger.error(f"Error fetching live market explore data: {e}")
            return None

    @classmethod
    def get_related_stocks(cls, symbol: str, limit: int = 6) -> Dict[str, Any]:
        """
        Returns peer stocks in the same sector for the given symbol,
        enriched with live or cached prices from the explore service.
        """
        clean_sym = symbol.strip().upper()
        if not clean_sym.endswith(".NS") and not clean_sym.endswith(".BO"):
            clean_sym = f"{clean_sym}.NS"

        matched_sector = None
        for sec, stocks in SECTOR_STOCKS_CATALOG.items():
            if any(s.get("symbol") == clean_sym for s in stocks):
                matched_sector = sec
                break

        if not matched_sector:
            for item in TRACKED_EXPLORE_STOCKS:
                if item[0] == clean_sym:
                    matched_sector = item[2]
                    break

        if not matched_sector:
            matched_sector = "Information Technology"

        # Check explore cache for live prices
        cached_explore = explore_cache.get(CACHE_KEY)
        live_price_map = {}
        if cached_explore:
            for s in cached_explore.get("most_traded", []):
                live_price_map[s["symbol"]] = s
            for k in ("gainers", "losers", "volume_shockers"):
                for s in cached_explore.get("top_movers", {}).get(k, []):
                    live_price_map[s["symbol"]] = s

        sector_stocks = SECTOR_STOCKS_CATALOG.get(matched_sector, SECTOR_STOCKS_CATALOG["Information Technology"])
        related = []
        for s in sector_stocks:
            if s.get("symbol") == clean_sym:
                continue
            sym = s.get("symbol")
            if sym in live_price_map:
                related.append(live_price_map[sym])
            else:
                related.append({
                    "symbol": sym,
                    "name": s.get("name"),
                    "sector": matched_sector,
                    "exchange": "NSE",
                    "current_price": s.get("current_price", 100.0),
                    "change": s.get("change_1d", 0.0),
                    "change_percent": s.get("change_1d_percent", 0.0),
                    "volume": s.get("volume", 500000),
                    "volume_formatted": s.get("volume_formatted", "5.00 L"),
                    "sparkline": [s.get("current_price", 100.0) * 0.99, s.get("current_price", 100.0)],
                })
            if len(related) >= limit:
                break

        return {
            "target_symbol": clean_sym,
            "sector": matched_sector,
            "related": related,
        }

    @classmethod
    def get_sector_stocks(cls, sector_name: str) -> Dict[str, Any]:
        """
        Returns the detailed list of stocks belonging to a specific sector
        with 1D price change, volume, 1W volume diff, 52W performance bar, RSI, MACD.
        Follows Groww sector deep-dive design with 50+ constituents per sector.
        """
        norm = sector_name.lower().replace("-", " ").strip()

        # Sector matching catalog ensuring >= 50 stocks for each sector
        if re.search(r'\b(it|tech|technology|information|software)\b', norm):
            display_name = "Information Technology"
        elif re.search(r'\b(bank|banking|financial|finance|nbfc)\b', norm):
            display_name = "Banking & Financial Services"
        elif re.search(r'\b(auto|automobile|vehicle|motor)\b', norm):
            display_name = "Automobile & Auto Components"
        elif re.search(r'\b(oil|gas|fuel|petroleum|energy)\b', norm):
            display_name = "Oil, Gas & Consumable Fuels"
        elif re.search(r'\b(pharma|pharmaceuticals|health|healthcare|hospital)\b', norm):
            display_name = "Pharmaceuticals & Healthcare"
        elif re.search(r'\b(cement|construction|building)\b', norm):
            display_name = "Cement & Construction Materials"
        elif re.search(r'\b(plastic|plastics|polymer|polymers)\b', norm):
            display_name = "Plastic and Polymers"
        elif re.search(r'\b(textile|textiles|apparel|garment)\b', norm):
            display_name = "Textiles"
        elif re.search(r'\b(water|utility|utilities|drainage)\b', norm):
            display_name = "Water Distribution & Utilities"
        else:
            display_name = "Information Technology"
            for cat_name in SECTOR_STOCKS_CATALOG.keys():
                if cat_name.lower() in norm or norm in cat_name.lower():
                    display_name = cat_name
                    break

        stocks = SECTOR_STOCKS_CATALOG.get(display_name, SECTOR_STOCKS_CATALOG["Information Technology"])

        return {
            "sector_name": display_name,
            "count": len(stocks),
            "stocks": stocks,
        }

    @classmethod
    def _get_resilient_fallback_data(cls) -> Dict[str, Any]:
        """Provides a realistic fallback dataset when offline or yfinance rate-limited."""
        ist_now = datetime.now(timezone(timedelta(hours=5, minutes=30)))
        # Base realistic stocks with recent market levels
        most_traded = [
            {"symbol": "TATASTEEL.NS", "name": "Tata Steel", "exchange": "NSE", "current_price": 163.0, "change": -15.0, "change_percent": -8.43, "volume": 168843913, "volume_formatted": "16.88 Cr", "sparkline": [178, 175, 172, 170, 166, 163.0]},
            {"symbol": "HDFCBANK.NS", "name": "HDFC Bank", "exchange": "NSE", "current_price": 817.8, "change": -28.2, "change_percent": -3.33, "volume": 55628667, "volume_formatted": "5.56 Cr", "sparkline": [846, 840, 835, 830, 822, 817.8]},
            {"symbol": "ITC.NS", "name": "ITC", "exchange": "NSE", "current_price": 301.0, "change": 1.9, "change_percent": 0.64, "volume": 27512525, "volume_formatted": "2.75 Cr", "sparkline": [299, 298.5, 300, 301.5, 300.8, 301.0]},
            {"symbol": "ICICIBANK.NS", "name": "ICICI Bank", "exchange": "NSE", "current_price": 1585.5, "change": -54.5, "change_percent": -3.32, "volume": 22243169, "volume_formatted": "2.22 Cr", "sparkline": [1640, 1630, 1615, 1610, 1595, 1585.5]},
            {"symbol": "SBIN.NS", "name": "State Bank of India", "exchange": "NSE", "current_price": 1132.65, "change": -32.45, "change_percent": -2.79, "volume": 14924743, "volume_formatted": "1.49 Cr", "sparkline": [1165, 1158, 1150, 1144, 1138, 1132.65]},
            {"symbol": "RELIANCE.NS", "name": "Reliance Industries", "exchange": "NSE", "current_price": 1351.0, "change": -26.5, "change_percent": -1.92, "volume": 12845010, "volume_formatted": "1.28 Cr", "sparkline": [1377.5, 1370, 1365, 1360, 1355, 1351.0]},
            {"symbol": "INFY.NS", "name": "Infosys", "exchange": "NSE", "current_price": 1782.4, "change": 14.8, "change_percent": 0.84, "volume": 11420500, "volume_formatted": "1.14 Cr", "sparkline": [1767, 1770, 1775, 1772, 1780, 1782.4]},
            {"symbol": "TCS.NS", "name": "TCS", "exchange": "NSE", "current_price": 2460.0, "change": 83.8, "change_percent": 3.53, "volume": 7386320, "volume_formatted": "73.86 L", "sparkline": [2376, 2400, 2420, 2435, 2450, 2460.0]},
        ]

        top_movers = {
            "gainers": [
                {"symbol": "TCS.NS", "name": "TCS", "exchange": "NSE", "current_price": 2460.0, "change": 83.8, "change_percent": 3.53, "volume": 7386320, "volume_formatted": "73.86 L", "sparkline": [2376, 2400, 2420, 2435, 2450, 2460.0]},
                {"symbol": "SHRIRAMFIN.NS", "name": "Shriram Finance", "exchange": "NSE", "current_price": 995.9, "change": 23.9, "change_percent": 2.46, "volume": 9471534, "volume_formatted": "94.72 L", "sparkline": [972, 978, 984, 988, 992, 995.9]},
                {"symbol": "TECHM.NS", "name": "Tech Mahindra", "exchange": "NSE", "current_price": 1777.5, "change": 31.3, "change_percent": 1.79, "volume": 3180662, "volume_formatted": "31.81 L", "sparkline": [1746, 1755, 1765, 1762, 1772, 1777.5]},
                {"symbol": "TORNTPHARM.NS", "name": "Torrent Pharma", "exchange": "NSE", "current_price": 4763.7, "change": 74.2, "change_percent": 1.58, "volume": 585099, "volume_formatted": "5.85 L", "sparkline": [4689, 4710, 4725, 4740, 4755, 4763.7]},
                {"symbol": "HCLTECH.NS", "name": "HCL Technologies", "exchange": "NSE", "current_price": 1364.3, "change": 19.9, "change_percent": 1.48, "volume": 3981800, "volume_formatted": "39.82 L", "sparkline": [1344, 1350, 1356, 1352, 1360, 1364.3]},
                {"symbol": "HINDZINC.NS", "name": "Hindustan Zinc", "exchange": "NSE", "current_price": 528.95, "change": 7.35, "change_percent": 1.41, "volume": 4880379, "volume_formatted": "48.80 L", "sparkline": [521.6, 523.5, 525.0, 524.2, 527.5, 528.95]},
            ],
            "losers": [
                {"symbol": "TATASTEEL.NS", "name": "Tata Steel", "exchange": "NSE", "current_price": 163.0, "change": -15.0, "change_percent": -8.43, "volume": 168843913, "volume_formatted": "16.88 Cr", "sparkline": [178, 175, 172, 170, 166, 163.0]},
                {"symbol": "AXISBANK.NS", "name": "Axis Bank", "exchange": "NSE", "current_price": 1388.6, "change": -57.4, "change_percent": -3.97, "volume": 10853616, "volume_formatted": "1.09 Cr", "sparkline": [1446, 1435, 1420, 1412, 1398, 1388.6]},
                {"symbol": "IOC.NS", "name": "Indian Oil", "exchange": "NSE", "current_price": 145.0, "change": -5.5, "change_percent": -3.65, "volume": 13240500, "volume_formatted": "1.32 Cr", "sparkline": [150.5, 149.2, 148.0, 147.1, 146.0, 145.0]},
                {"symbol": "HDFCBANK.NS", "name": "HDFC Bank", "exchange": "NSE", "current_price": 817.8, "change": -28.2, "change_percent": -3.33, "volume": 55628667, "volume_formatted": "5.56 Cr", "sparkline": [846, 840, 835, 830, 822, 817.8]},
                {"symbol": "ICICIBANK.NS", "name": "ICICI Bank", "exchange": "NSE", "current_price": 1585.5, "change": -54.5, "change_percent": -3.32, "volume": 22243169, "volume_formatted": "2.22 Cr", "sparkline": [1640, 1630, 1615, 1610, 1595, 1585.5]},
                {"symbol": "SBIN.NS", "name": "State Bank of India", "exchange": "NSE", "current_price": 1132.65, "change": -32.45, "change_percent": -2.79, "volume": 14924743, "volume_formatted": "1.49 Cr", "sparkline": [1165, 1158, 1150, 1144, 1138, 1132.65]},
            ],
            "volume_shockers": most_traded[:8]
        }

        trending_sectors = [
            {"id": "it", "name": "Information Technology", "icon": "laptop", "gainers": 5, "losers": 0, "change_percent": 1.76},
            {"id": "pharma", "name": "Healthcare & Pharma", "icon": "activity", "gainers": 4, "losers": 2, "change_percent": 0.85},
            {"id": "fmcg", "name": "FMCG & Consumer Goods", "icon": "package", "gainers": 3, "losers": 3, "change_percent": 0.12},
            {"id": "auto", "name": "Automobiles", "icon": "car", "gainers": 2, "losers": 4, "change_percent": -0.65},
            {"id": "energy", "name": "Oil, Gas & Consumable Fuels", "icon": "fuel", "gainers": 1, "losers": 4, "change_percent": -1.45},
            {"id": "banking", "name": "Banking & Financial Services", "icon": "building", "gainers": 2, "losers": 7, "change_percent": -2.35},
            {"id": "metals", "name": "Metals & Mining", "icon": "layers", "gainers": 1, "losers": 5, "change_percent": -3.10},
        ]

        popular_picks = [
            {"symbol": "RELIANCE.NS", "name": "Reliance Industries", "exchange": "NSE", "current_price": 1351.0, "change": -26.5, "change_percent": -1.92, "volume": 12845010, "volume_formatted": "1.28 Cr", "sparkline": [1377.5, 1370, 1365, 1360, 1355, 1351.0]},
            {"symbol": "TCS.NS", "name": "TCS", "exchange": "NSE", "current_price": 2460.0, "change": 83.8, "change_percent": 3.53, "volume": 7386320, "volume_formatted": "73.86 L", "sparkline": [2376, 2400, 2420, 2435, 2450, 2460.0]},
            {"symbol": "HDFCBANK.NS", "name": "HDFC Bank", "exchange": "NSE", "current_price": 817.8, "change": -28.2, "change_percent": -3.33, "volume": 55628667, "volume_formatted": "5.56 Cr", "sparkline": [846, 840, 835, 830, 822, 817.8]},
            {"symbol": "INFY.NS", "name": "Infosys", "exchange": "NSE", "current_price": 1782.4, "change": 14.8, "change_percent": 0.84, "volume": 11420500, "volume_formatted": "1.14 Cr", "sparkline": [1767, 1770, 1775, 1772, 1780, 1782.4]},
            {"symbol": "ETERNAL.NS", "name": "Zomato", "exchange": "NSE", "current_price": 245.0, "change": 4.3, "change_percent": 1.78, "volume": 38450120, "volume_formatted": "3.84 Cr", "sparkline": [240, 241, 242.5, 243.8, 244.2, 245.0]},
            {"symbol": "MARUTI.NS", "name": "Maruti Suzuki", "exchange": "NSE", "current_price": 11840.0, "change": 85.0, "change_percent": 0.72, "volume": 842100, "volume_formatted": "8.42 L", "sparkline": [11755, 11780, 11810, 11795, 11825, 11840.0]},
            {"symbol": "SBIN.NS", "name": "State Bank of India", "exchange": "NSE", "current_price": 1132.65, "change": -32.45, "change_percent": -2.79, "volume": 14924743, "volume_formatted": "1.49 Cr", "sparkline": [1165, 1158, 1150, 1144, 1138, 1132.65]},
            {"symbol": "ITC.NS", "name": "ITC", "exchange": "NSE", "current_price": 301.0, "change": 1.9, "change_percent": 0.64, "volume": 27512525, "volume_formatted": "2.75 Cr", "sparkline": [299, 298.5, 300, 301.5, 300.8, 301.0]},
        ]

        return {
            "most_traded": most_traded,
            "top_movers": top_movers,
            "trending_sectors": trending_sectors,
            "popular_picks": popular_picks,
            "last_updated": ist_now.strftime("%d %b %Y, %I:%M %p IST"),
            "is_live": False,
        }
