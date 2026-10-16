"""
Hybrid Valuation and Decision Engine for Indian Stocks (NSE & BSE).
Combines Fundamental Intrinsic Valuation (DCF, Graham Number, Multiples, Balance Sheet Health)
with Technical Timing (RSI, 50 & 200 DMA, 52-Week Discount).
Generates clear verdicts: BEST BUY, AT FAIR PRICE, or CURRENTLY EXPENSIVE.
"""
from typing import Dict, Any, List, Optional
import math
import pandas as pd
import numpy as np


class ValuationEngine:
    
    @staticmethod
    def calculate_rsi(prices: pd.Series, period: int = 14) -> Optional[float]:
        """Calculates 14-period Relative Strength Index."""
        if len(prices) < period + 1:
            return None
        delta = prices.diff()
        gain = delta.where(delta > 0, 0.0)
        loss = -delta.where(delta < 0, 0.0)

        avg_gain = gain.rolling(window=period, min_periods=period).mean()
        avg_loss = loss.rolling(window=period, min_periods=period).mean()

        # Exponential moving smoothing
        for i in range(period, len(prices)):
            avg_gain.iloc[i] = (avg_gain.iloc[i - 1] * (period - 1) + gain.iloc[i]) / period
            avg_loss.iloc[i] = (avg_loss.iloc[i - 1] * (period - 1) + loss.iloc[i]) / period

        last_gain = avg_gain.iloc[-1]
        last_loss = avg_loss.iloc[-1]

        if np.isnan(last_gain) or np.isnan(last_loss):
            return 50.0
        if last_loss == 0:
            return 100.0 if last_gain > 0 else 50.0
        if last_gain == 0:
            return 0.0

        rs = last_gain / last_loss
        rsi = 100 - (100 / (1 + rs))
        return round(float(rsi), 2)

    @staticmethod
    def calculate_moving_averages(prices: pd.Series) -> Dict[str, Optional[float]]:
        """Calculates 50-day and 200-day Simple Moving Averages."""
        dma_50 = float(prices.tail(50).mean()) if len(prices) >= 50 else None
        dma_200 = float(prices.tail(200).mean()) if len(prices) >= 200 else None
        return {
            "dma_50": round(dma_50, 2) if dma_50 else None,
            "dma_200": round(dma_200, 2) if dma_200 else None,
        }

    @classmethod
    def calculate_graham_number(cls, eps: Optional[float], bvps: Optional[float]) -> Optional[float]:
        """
        Benjamin Graham Number: sqrt(22.5 * EPS * BVPS)
        Represents the maximum fair price for conservative value investors.
        """
        if eps is not None and bvps is not None and eps > 0 and bvps > 0:
            val = math.sqrt(22.5 * eps * bvps)
            return round(val, 2)
        return None

    @classmethod
    def calculate_dcf_fair_value(
        cls,
        fcf_per_share: Optional[float],
        eps: Optional[float],
        growth_rate: Optional[float],
        discount_rate: float = 0.115,  # 11.5% discount rate (India G-Sec ~7% + 4.5% ERP)
        terminal_rate: float = 0.055,  # 5.5% long-term India GDP sustainable growth
        projection_years: int = 5
    ) -> Optional[float]:
        """
        Calculates conservative 2-stage Discounted Cash Flow (DCF) intrinsic value.
        Uses Free Cash Flow per share or adjusted EPS as proxy.
        """
        base_cash = fcf_per_share if (fcf_per_share and fcf_per_share > 0) else eps
        if not base_cash or base_cash <= 0:
            return None

        # Sanitize growth rate (cap between 6% and 22% for conservatism)
        if growth_rate is None or growth_rate <= 0:
            g = 0.10  # default 10% expected growth
        else:
            g = min(max(growth_rate, 0.06), 0.22)

        pv_future_cash = 0.0
        current_cf = base_cash

        for t in range(1, projection_years + 1):
            current_cf *= (1 + g)
            discount_factor = (1 + discount_rate) ** t
            pv_future_cash += current_cf / discount_factor

        # Terminal Value calculation using Gordon Growth model
        terminal_cash = current_cf * (1 + terminal_rate)
        if discount_rate <= terminal_rate:
            terminal_value = 0.0
        else:
            terminal_value = terminal_cash / (discount_rate - terminal_rate)

        pv_terminal = terminal_value / ((1 + discount_rate) ** projection_years)
        intrinsic_value = pv_future_cash + pv_terminal

        return round(float(intrinsic_value), 2)

    @classmethod
    def evaluate_stock(
        cls,
        current_price: float,
        info: Dict[str, Any],
        history_df: Optional[pd.DataFrame] = None
    ) -> Dict[str, Any]:
        """
        Performs full hybrid evaluation.
        Produces:
          - Fundamental Score (0-100)
          - Technical Score (0-100)
          - Composite Score (0-100)
          - Target Fair Value & Margin of Safety %
          - Verdict: 'BEST BUY', 'AT FAIR PRICE', or 'CURRENTLY EXPENSIVE'
          - Key Pros, Cons, and Detailed Breakdown
        """
        if current_price <= 0:
            current_price = info.get("regularMarketPrice") or info.get("currentPrice") or 1.0

        # Extract Fundamental Inputs
        pe = info.get("trailingPE") or info.get("forwardPE")
        sector_pe = info.get("sectorPE") or 26.0  # approximate Indian market median
        pb = info.get("priceToBook")
        peg = info.get("pegRatio")
        roe = info.get("returnOnEquity")
        if roe and roe > 1.0:  # If expressed as percentage > 1
            roe = roe / 100.0
        
        eps = info.get("trailingEps") or info.get("forwardEps")
        bvps = info.get("bookValue")
        debt_to_equity = info.get("debtToEquity")
        div_yield = info.get("dividendYield")
        growth_rate = info.get("earningsGrowth") or info.get("revenueGrowth")
        fcf = info.get("freeCashflow")
        shares = info.get("sharesOutstanding")
        fcf_per_share = (fcf / shares) if (fcf and shares and shares > 0) else None

        # 1. Fundamental Calculations
        graham = cls.calculate_graham_number(eps, bvps)
        dcf = cls.calculate_dcf_fair_value(fcf_per_share, eps, growth_rate)

        # Estimate Composite Fair Value
        fair_value_candidates = []
        if dcf and dcf > 0:
            fair_value_candidates.append(dcf)
        if graham and graham > 0:
            fair_value_candidates.append(graham)
        
        # If neither DCF nor Graham can be computed (e.g. loss making or missing stats),
        # use P/E multiple fair value anchor or analyst target
        target_mean = info.get("targetMeanPrice")
        if target_mean and target_mean > 0:
            fair_value_candidates.append(float(target_mean))
        
        if pe and eps and eps > 0:
            # Justified P/E fair value
            benchmark_pe = min(sector_pe, 30.0)
            fair_pe_val = eps * benchmark_pe
            fair_value_candidates.append(fair_pe_val)

        if fair_value_candidates:
            # Trim extreme outliers if multiple exist
            if len(fair_value_candidates) >= 3:
                fair_value_candidates.sort()
                fair_value = sum(fair_value_candidates[1:-1]) / len(fair_value_candidates[1:-1])
            else:
                fair_value = sum(fair_value_candidates) / len(fair_value_candidates)
            fair_value = round(fair_value, 2)
        else:
            fair_value = round(current_price * 1.05, 2)  # Neutral fallback

        # Margin of safety = (Fair Value - Current Price) / Current Price
        margin_of_safety = round(((fair_value - current_price) / current_price) * 100, 2)

        # Fundamental Scoring (0-100)
        fund_points = 50.0  # Base neutral
        pros: List[str] = []
        cons: List[str] = []

        # Margin of safety score impact
        if margin_of_safety >= 25:
            fund_points += 20
            pros.append(f"Significant discount: Trading {margin_of_safety:.1f}% below estimated Intrinsic Value (₹{fair_value})")
        elif margin_of_safety >= 10:
            fund_points += 12
            pros.append(f"Good value: Trading {margin_of_safety:.1f}% below estimated Intrinsic Value (₹{fair_value})")
        elif margin_of_safety <= -25:
            fund_points -= 20
            cons.append(f"Stretched valuation: Trading {abs(margin_of_safety):.1f}% above estimated Intrinsic Value (₹{fair_value})")
        elif margin_of_safety <= -10:
            fund_points -= 10
            cons.append(f"Premium pricing: Trading {abs(margin_of_safety):.1f}% above Fair Value (₹{fair_value})")
        else:
            pros.append(f"Fairly priced: Stock trades within ±10% of estimated Fair Value (₹{fair_value})")

        # P/E evaluation
        if pe:
            if pe < 18 and pe > 0:
                fund_points += 10
                pros.append(f"Attractive P/E of {pe:.1f}x (Lower than market median)")
            elif pe > 50:
                fund_points -= 12
                cons.append(f"Elevated P/E ratio of {pe:.1f}x indicates high valuation expectations")
        
        # PEG ratio
        if peg:
            if 0 < peg <= 1.2:
                fund_points += 10
                pros.append(f"Attractive PEG ratio of {peg:.2f} (High earnings growth relative to price)")
            elif peg > 2.5:
                fund_points -= 8
                cons.append(f"High PEG ratio of {peg:.2f} implies growth may not justify current price")

        # Return on Equity (ROE)
        if roe:
            roe_pct = roe * 100 if roe < 1.0 else roe
            if roe_pct >= 18:
                fund_points += 10
                pros.append(f"High Return on Equity (ROE) of {roe_pct:.1f}% indicates strong capital efficiency")
            elif roe_pct < 8:
                fund_points -= 8
                cons.append(f"Subdued Return on Equity of {roe_pct:.1f}%")

        # Debt to Equity
        is_financial = "bank" in str(info.get("sector", "")).lower() or "finance" in str(info.get("sector", "")).lower()
        if not is_financial and debt_to_equity is not None:
            # yfinance often returns debtToEquity as percentage (e.g. 50 = 0.5)
            de_ratio = debt_to_equity / 100.0 if debt_to_equity > 5.0 else debt_to_equity
            if de_ratio < 0.3:
                fund_points += 8
                pros.append("Virtually debt-free balance sheet (Low financial leverage risk)")
            elif de_ratio > 1.5:
                fund_points -= 10
                cons.append(f"High Debt-to-Equity ratio of {de_ratio:.2f} poses leverage risk")

        fundamental_score = max(5.0, min(95.0, fund_points))

        # 2. Technical Calculations & Scoring (0-100)
        tech_points = 50.0
        rsi = None
        dma_50 = None
        dma_200 = None
        high_52 = info.get("fiftyTwoWeekHigh")
        low_52 = info.get("fiftyTwoWeekLow")

        if history_df is not None and not history_df.empty and "Close" in history_df.columns:
            close_prices = history_df["Close"].dropna()
            rsi = cls.calculate_rsi(close_prices)
            mas = cls.calculate_moving_averages(close_prices)
            dma_50 = mas["dma_50"]
            dma_200 = mas["dma_200"]

        # RSI scoring
        if rsi is not None:
            if rsi <= 32:
                tech_points += 20
                pros.append(f"RSI is oversold at {rsi:.1f} — high probability of a technical rebound")
            elif rsi <= 45:
                tech_points += 10
                pros.append(f"RSI at {rsi:.1f} is in favorable accumulation zone")
            elif rsi >= 72:
                tech_points -= 18
                cons.append(f"RSI is overbought at {rsi:.1f} — vulnerable to short-term pullbacks")
            elif rsi >= 62:
                tech_points -= 6

        # Moving Average scoring
        if dma_200:
            if current_price > dma_200:
                dist_pct = ((current_price - dma_200) / dma_200) * 100
                if dist_pct < 15:
                    tech_points += 10
                    pros.append(f"Trading above 200 DMA (₹{dma_200}) confirming solid primary uptrend")
                elif dist_pct > 35:
                    tech_points -= 8
                    cons.append(f"Stock is extended {dist_pct:.1f}% above its 200 DMA")
            else:
                dist_pct = ((dma_200 - current_price) / dma_200) * 100
                tech_points -= 8
                cons.append(f"Trading below 200 DMA (₹{dma_200}) — downtrend or consolidation in progress")

        # Golden Cross check
        if dma_50 and dma_200:
            if dma_50 > dma_200:
                tech_points += 6
                pros.append("Bullish Golden Cross: 50 DMA is positioned above 200 DMA")
            else:
                tech_points -= 6
                cons.append("50 DMA is below 200 DMA, suggesting ongoing consolidation")

        # 52-Week Range
        if high_52 and high_52 > 0:
            discount_from_high = ((high_52 - current_price) / high_52) * 100
            if discount_from_high >= 25:
                tech_points += 8
                pros.append(f"Trading at a {discount_from_high:.1f}% discount from its 52-week High of ₹{high_52}")
            elif discount_from_high < 5:
                cons.append("Trading near its 52-week High, leaving less immediate upside cushion")

        technical_score = max(5.0, min(95.0, tech_points))

        # 3. Composite Hybrid Score (60% Fundamental, 40% Technical)
        composite_score = round((0.60 * fundamental_score) + (0.40 * technical_score), 1)

        # 4. Final Verdict Determination
        # Criteria:
        # "BEST BUY": Composite score >= 68, or Margin of Safety >= 15% with decent technicals
        # "CURRENTLY EXPENSIVE": Composite score < 44 or Margin of Safety <= -18%
        # "AT FAIR PRICE": Middle zone, healthy for systematic SIP / hold
        if composite_score >= 68 and margin_of_safety >= 5.0:
            verdict = "BEST BUY"
            verdict_badge = "success"
            verdict_desc = "Significantly undervalued with attractive entry timing. High margin of safety for long-term investment."
            action_call = "Strong Buy / Accumulate on Dips"
        elif margin_of_safety >= 25.0 and technical_score >= 40:
            verdict = "BEST BUY"
            verdict_badge = "success"
            verdict_desc = "Substantial fundamental discount to intrinsic value. Excellent value proposition."
            action_call = "Strong Buy / Value Opportunity"
        elif composite_score <= 42 or margin_of_safety <= -20.0 or (pe and pe > 75 and rsi and rsi > 68):
            verdict = "CURRENTLY EXPENSIVE"
            verdict_badge = "danger"
            verdict_desc = "Valuation multiples are currently stretched relative to earnings power. High risk of mean reversion."
            action_call = "Avoid Fresh Buying / Wait for Correction"
        else:
            verdict = "AT FAIR PRICE"
            verdict_badge = "warning"
            verdict_desc = "Trading near calculated intrinsic fair value. Good for steady SIP or holding existing positions."
            action_call = "Hold / Systematic Accumulation (SIP)"

        return {
            "verdict": verdict,
            "verdict_badge": verdict_badge,
            "verdict_desc": verdict_desc,
            "action_call": action_call,
            "composite_score": composite_score,
            "fundamental_score": round(fundamental_score, 1),
            "technical_score": round(technical_score, 1),
            "current_price": round(current_price, 2),
            "fair_value": fair_value,
            "margin_of_safety_percent": margin_of_safety,
            "graham_number": graham,
            "dcf_intrinsic_value": dcf,
            "rsi": rsi,
            "dma_50": dma_50,
            "dma_200": dma_200,
            "high_52": high_52,
            "low_52": low_52,
            "pros": pros,
            "cons": cons,
            "valuation_status": (
                "Undervalued (Discount)" if margin_of_safety > 10
                else "Overvalued (Premium)" if margin_of_safety < -10
                else "Fairly Valued"
            )
        }
