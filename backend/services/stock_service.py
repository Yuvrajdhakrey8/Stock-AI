"""
Stock Data Fetcher & Aggregator Service for Indian Markets (NSE & BSE).
Integrates yfinance, caches responses, and formats data for frontend charts and analytics.
"""
from typing import Dict, Any, Optional, List
import yfinance as yf
import pandas as pd
from cachetools import TTLCache
from .ticker_catalog import normalize_ticker, STOCKS_DATABASE
from .valuation_engine import ValuationEngine
import logging
import concurrent.futures
from .screener_snapshot import get_category_snapshot

logger = logging.getLogger(__name__)

# Cache for 10 minutes to deliver lightning-fast responses & protect against rate limits
stock_cache = TTLCache(maxsize=300, ttl=600)
history_cache = TTLCache(maxsize=300, ttl=600)
screener_cache = TTLCache(maxsize=50, ttl=1800)


class StockService:

    @classmethod
    def get_stock_data(cls, raw_symbol: str) -> Optional[Dict[str, Any]]:
        """
        Fetches stock data, runs valuation engine, and returns full analysis payload.
        """
        symbol = normalize_ticker(raw_symbol)
        
        # Check cache
        if symbol in stock_cache:
            return stock_cache[symbol]

        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info or {}
            
            # Fetch 1 year historical data for charts and technical indicators
            history_df = ticker.history(period="1y")

            # Validate that data was received
            current_price = (
                info.get("currentPrice") or
                info.get("regularMarketPrice") or
                info.get("previousClose")
            )
            
            if not current_price and not history_df.empty:
                current_price = float(history_df["Close"].iloc[-1])

            if not current_price:
                # If still no price, try alternative exchange suffix if not specified
                if symbol.endswith(".NS"):
                    alt_symbol = symbol.replace(".NS", ".BO")
                    return cls.get_stock_data(alt_symbol)
                return None

            current_price = float(current_price)
            prev_close = float(info.get("previousClose") or (history_df["Close"].iloc[-2] if len(history_df) >= 2 else current_price))
            change = round(current_price - prev_close, 2)
            change_percent = round((change / prev_close) * 100, 2) if prev_close > 0 else 0.0

            # Run Hybrid Valuation Engine
            evaluation = ValuationEngine.evaluate_stock(
                current_price=current_price,
                info=info,
                history_df=history_df
            )

            # Format Historical Chart Data (daily points for frontend)
            chart_data = []
            if not history_df.empty:
                # Calculate rolling 50 and 200 SMA on the series for plotting
                history_df["SMA_50"] = history_df["Close"].rolling(window=50, min_periods=10).mean()
                history_df["SMA_200"] = history_df["Close"].rolling(window=200, min_periods=20).mean()

                # Take last 180 trading days for fast frontend rendering
                recent_df = history_df.tail(200)
                for index, row in recent_df.iterrows():
                    date_str = index.strftime("%Y-%m-%d") if hasattr(index, "strftime") else str(index)[:10]
                    chart_data.append({
                        "date": date_str,
                        "open": round(float(row["Open"]), 2) if "Open" in row else None,
                        "high": round(float(row["High"]), 2) if "High" in row else None,
                        "low": round(float(row["Low"]), 2) if "Low" in row else None,
                        "close": round(float(row["Close"]), 2),
                        "volume": int(row["Volume"]) if "Volume" in row else 0,
                        "sma_50": round(float(row["SMA_50"]), 2) if not pd.isna(row["SMA_50"]) else None,
                        "sma_200": round(float(row["SMA_200"]), 2) if not pd.isna(row["SMA_200"]) else None,
                    })

            # Format Key Fundamental Stats
            market_cap = info.get("marketCap")
            pe = info.get("trailingPE") or info.get("forwardPE")
            pb = info.get("priceToBook")
            peg = info.get("pegRatio")
            eps = info.get("trailingEps") or info.get("forwardEps")
            bvps = info.get("bookValue")
            div_yield = (info.get("dividendYield") or 0.0) * 100 if info.get("dividendYield") else 0.0
            roe = (info.get("returnOnEquity") or 0.0) * 100 if info.get("returnOnEquity") else None
            profit_margin = (info.get("profitMargins") or 0.0) * 100 if info.get("profitMargins") else None
            debt_to_equity = info.get("debtToEquity")
            if debt_to_equity and debt_to_equity > 5.0:
                debt_to_equity = debt_to_equity / 100.0

            company_name = info.get("longName") or info.get("shortName") or symbol.split(".")[0]
            sector = info.get("sector") or "Indian Equity"
            industry = info.get("industry") or "Diverse"
            summary = info.get("longBusinessSummary") or "Leading listed Indian corporation."

            # Construct Payload
            result = {
                "symbol": symbol,
                "display_symbol": symbol.replace(".NS", "").replace(".BO", ""),
                "exchange": "NSE" if symbol.endswith(".NS") else "BSE",
                "name": company_name,
                "sector": sector,
                "industry": industry,
                "description": summary,
                "current_price": round(current_price, 2),
                "previous_close": round(prev_close, 2),
                "change": change,
                "change_percent": change_percent,
                "currency": info.get("currency") or "INR",
                "market_cap": market_cap,
                "market_cap_formatted": cls._format_inr_crores(market_cap),
                "volume": info.get("regularMarketVolume") or info.get("volume"),
                "high_52": info.get("fiftyTwoWeekHigh"),
                "low_52": info.get("fiftyTwoWeekLow"),
                "valuation": evaluation,
                "ratios": {
                    "pe_ratio": round(pe, 2) if pe else None,
                    "pb_ratio": round(pb, 2) if pb else None,
                    "peg_ratio": round(peg, 2) if peg else None,
                    "eps": round(eps, 2) if eps else None,
                    "book_value": round(bvps, 2) if bvps else None,
                    "dividend_yield": round(div_yield, 2) if div_yield else 0.0,
                    "roe": round(roe, 2) if roe else None,
                    "profit_margin": round(profit_margin, 2) if profit_margin else None,
                    "debt_to_equity": round(debt_to_equity, 2) if debt_to_equity else None,
                    "beta": round(float(info.get("beta")), 2) if info.get("beta") else None,
                },
                "chart": chart_data,
            }

            # Cache the enriched result
            stock_cache[symbol] = result
            return result

        except Exception as e:
            logger.error(f"Error fetching stock data for {symbol}: {e}")
            return None

    @classmethod
    def get_screener_results(cls, category: str = "nifty50", limit: int = 25) -> List[Dict[str, Any]]:
        """
        Produces screener data for top stocks with their valuation verdicts.
        Uses screener_cache, pre-computed snapshots, and parallel worker threads
        to ensure sub-second response times and zero Lambda timeouts.
        """
        cache_key = f"{category.lower()}_{limit}"
        if cache_key in screener_cache:
            return screener_cache[cache_key]

        # 1. Start with verified baseline snapshot
        base_items = get_category_snapshot(category, limit)
        items_by_sym = {it["symbol"]: it for it in base_items}

        # 2. Select candidates
        from .ticker_catalog import get_screener_stocks
        candidates = get_screener_stocks(category)[:limit]

        # 3. Check what is already in stock_cache
        uncached_syms = []
        for c in candidates:
            sym = c["symbol"]
            if sym in stock_cache:
                data = stock_cache[sym]
                items_by_sym[sym] = {
                    "symbol": data["symbol"],
                    "display_symbol": data["display_symbol"],
                    "name": data["name"],
                    "exchange": data["exchange"],
                    "sector": data["sector"],
                    "current_price": data["current_price"],
                    "change_percent": data["change_percent"],
                    "fair_value": data["valuation"]["fair_value"],
                    "margin_of_safety": data["valuation"]["margin_of_safety_percent"],
                    "composite_score": data["valuation"]["composite_score"],
                    "verdict": data["valuation"]["verdict"],
                    "verdict_badge": data["valuation"]["verdict_badge"],
                    "pe_ratio": data["ratios"]["pe_ratio"],
                    "roe": data["ratios"]["roe"],
                    "rsi": data["valuation"]["rsi"],
                }
            else:
                uncached_syms.append(sym)

        # 4. If there are uncached stocks, refresh them concurrently with a strict 4.5s ceiling
        if uncached_syms:
            def fetch_single(sym: str):
                try:
                    return sym, cls.get_stock_data(sym)
                except Exception as ex:
                    logger.debug(f"Live fetch skipped for {sym}: {ex}")
                    return sym, None

            with concurrent.futures.ThreadPoolExecutor(max_workers=min(len(uncached_syms), 8)) as executor:
                future_to_sym = {executor.submit(fetch_single, sym): sym for sym in uncached_syms}
                done, _ = concurrent.futures.wait(future_to_sym.keys(), timeout=4.5)
                for f in done:
                    try:
                        sym, data = f.result()
                        if data:
                            items_by_sym[sym] = {
                                "symbol": data["symbol"],
                                "display_symbol": data["display_symbol"],
                                "name": data["name"],
                                "exchange": data["exchange"],
                                "sector": data["sector"],
                                "current_price": data["current_price"],
                                "change_percent": data["change_percent"],
                                "fair_value": data["valuation"]["fair_value"],
                                "margin_of_safety": data["valuation"]["margin_of_safety_percent"],
                                "composite_score": data["valuation"]["composite_score"],
                                "verdict": data["valuation"]["verdict"],
                                "verdict_badge": data["valuation"]["verdict_badge"],
                                "pe_ratio": data["ratios"]["pe_ratio"],
                                "roe": data["ratios"]["roe"],
                                "rsi": data["valuation"]["rsi"],
                            }
                    except Exception as ex:
                        logger.debug(f"Future extraction failed: {ex}")

        # Assemble final ordered list
        results = [items_by_sym[c["symbol"]] for c in candidates if c["symbol"] in items_by_sym]
        screener_cache[cache_key] = results
        return results

    @staticmethod
    def _format_inr_crores(amount: Optional[int]) -> str:
        """Formats number into Indian standard (Crores / Lakhs)."""
        if not amount or amount <= 0:
            return "N/A"
        crores = amount / 10000000.0  # 1 Crore = 10 Million
        if crores >= 100000:
            lakh_cr = crores / 100000.0
            return f"₹{lakh_cr:.2f} Lakh Cr"
        elif crores >= 1:
            return f"₹{crores:,.1f} Cr"
        else:
            lakhs = amount / 100000.0
            return f"₹{lakhs:,.1f} Lakhs"
