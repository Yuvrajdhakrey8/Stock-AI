# DhakreyStock AI — Indian Stock & IPO Market Valuation & Advisory App (NSE & BSE)

A full-stack, free-tier financial analysis application specifically designed for the **Indian Stock Market (NSE & BSE)**. The platform analyzes any listed stock and delivers an immediate quantitative verdict:
- 🟢 **BEST BUY (Strong Buy / Value Opportunity)**
- 🟡 **AT FAIR PRICE (Systematic Accumulation / SIP)**
- 🔴 **CURRENTLY EXPENSIVE (Valuation Stretched / Avoid Fresh Buying)**

---

## Key Features

1. **Complete NSE & BSE Coverage**:
   - Instant search and autocomplete for thousands of Indian equities (e.g. `Reliance`, `TCS`, `Tata Motors`, `HDFC Bank`, `Infosys`, `Zomato`, `ITC`, `SBI`, etc.).
   - Analyzes any active stock by ticker (`SYMBOL.NS` or `SYMBOL.BO`).

2. **Hybrid Valuation Engine (100% Free)**:
   - **Fundamental Intrinsic Valuation (60%)**:
     - **Discounted Cash Flow (DCF)** 5-year free cash flow model adjusted for Indian long-term GDP growth.
     - **Benjamin Graham Number** ($\sqrt{22.5 \times \text{EPS} \times \text{Book Value}}$).
     - **Valuation Multiples**: P/E vs sector/market median, PEG ratio, Price-to-Book vs ROE.
     - **Financial Solvency**: Debt-to-Equity leverage checks and Return on Equity (ROE).
   - **Technical Timing (40%)**:
     - **RSI (14-period)** to identify oversold accumulation zones vs overbought peaks.
     - **50 DMA & 200 DMA** institutional support levels and Golden/Death cross detection.
     - **52-Week Price Spectrum** showing current price discount relative to 52W High and Low.

3. **Visual Valuation Gauge**:
   - 3-segment visual meter showing exact positioning between **EXPENSIVE**, **AT FAIR PRICE**, and **BEST BUY**.
   - Calculated Intrinsic Fair Value vs Current Market Price and Margin of Safety %.
   - Plain-English investment highlights and risk warnings.

4. **Interactive Multi-Timeframe Charts**:
   - Area price chart with toggleable 50 DMA, 200 DMA, and intrinsic fair value reference lines.
   - Timeframe toggles (1M, 3M, 6M, 1Y).

5. **Multi-Index Screener**:
   - Explore and rank stocks across **Nifty 50 Bluechips**, **Nifty Next 50**, **Midcap Growth**, **IT**, **Banking**, and **Automobiles**.
   - Filter by verdict (e.g. show only "Best Buy" stocks).

6. **Local Watchlist**:
   - Save your favorite Indian stocks to a persistent local watchlist with live valuation badges.

7. **IPO Research & Advisory Tab (NEW)**:
   - **Full Listing & History**: Filters for Upcoming, Open, Closed, and Listed IPOs (Mainboard & SME).
   - **Closing-Day GMP**: Verified grey market premium on the IPO closing date with estimated listing price.
   - **Subscription Progression**: Day 1, Day 2, and Final Day demand trends across QIB, NII/HNI, and Retail categories.
   - **Listing Gains & 1-Lot Profit**: Issue price vs actual listing price, percentage gain, and net profit per retail lot (₹).
   - **GMP Reliability Check**: Evaluates whether closing GMP was accurate or over/under-predicted.
   - **Missed Opportunity Retrospective**: Actionable analysis of whether skipping a past IPO was a good decision or missed opportunity.
   - **Application Recommendation**: Actionable **Apply**, **Avoid**, or **Apply with Caution** guidance with listing gain vs long-term investment breakdown.
   - **Side-by-Side Comparison**: Select and compare multiple IPOs across all metrics in real time.

---

## Quick Start Guide

### Option 1: One-Click Launcher (Windows)
Double-click `start_app.bat` or run:
```powershell
.\run.ps1
```

### Option 2: Manual Start

#### 1. Backend (FastAPI)
```powershell
cd backend
.\venv\Scripts\python.exe main.py
```
Backend runs at: `http://127.0.0.1:8000` (Interactive Swagger docs: `http://127.0.0.1:8000/docs`)

#### 2. Frontend (React + Vite)
```powershell
cd frontend
npm run dev
```
Frontend runs at: `http://localhost:5173`

---

## Project Structure

```
Stock_App/
├── backend/
│   ├── main.py                  # FastAPI REST endpoints
│   ├── requirements.txt         # Python dependencies
│   ├── services/
│   │   ├── valuation_engine.py  # Hybrid DCF, Graham, RSI, DMA scoring model
│   │   ├── stock_service.py     # yfinance market data fetcher & cache
│   │   └── ticker_catalog.py    # NSE & BSE search registry & index catalog
│   └── tests/
│       ├── test_valuation.py    # Valuation engine unit tests
│       └── test_api.py          # FastAPI endpoint integration tests
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.tsx           # Header with live market index ticker
│   │   │   ├── SearchHeader.tsx     # Smart autocomplete search for NSE/BSE
│   │   │   ├── ValuationMeter.tsx   # 3-Zone verdict gauge & margin of safety
│   │   │   ├── StockOverview.tsx    # Live quotes & 52W range slider
│   │   │   ├── FundamentalGrid.tsx  # DCF, Graham, P/E, PEG, ROE cards
│   │   │   ├── TechnicalChart.tsx   # Price chart with 50/200 DMA & RSI
│   │   │   ├── ScreenerView.tsx     # Multi-index stock screener
│   │   │   └── WatchlistDrawer.tsx  # Persistent saved stocks
│   │   ├── types.ts                 # TypeScript interfaces
│   │   ├── App.tsx                  # Main layout & router
│   │   └── main.tsx
│   ├── vite.config.ts
│   └── package.json
├── start_app.bat                # Windows 1-click batch launcher
├── run.ps1                      # Windows PowerShell launcher
└── README.md
```

---

## Verification & Testing

To run the automated backend test suite:
```powershell
$env:PYTHONPATH="backend"
.\backend\venv\Scripts\pytest.exe backend\tests -v
```
All tests verify Graham number, DCF calculations, RSI edge cases, verdict classifications, and API routes.

---

## 📱 Mobile App (Android APK & Google Play Store)

DhakreyStock AI is packaged as a high-performance native Android app powered by Capacitor:
- **Direct Sideload APK**: Downloadable directly from [GitHub Releases](https://github.com/Yuvrajdhakrey8/Stock-AI/releases/tag/mobile-latest) (`DhakreyStock-AI.apk`).
- **Google Play Store Bundle**: Official production-ready Android App Bundle (`DhakreyStock-AI.aab`).
- **Google AdMob Monetization**: Integrated with banner and interstitial ads for passive revenue.
- **Privacy Policy Compliance**: Public legal disclosure hosted at `/privacy-policy.html`.
- **Viral 1-Click Sharing**: Share live DCF valuations, margin of safety, and IPO GMP analysis directly via WhatsApp and social apps.
- **Automated CI/CD**: Cloud compilation via GitHub Actions (`.github/workflows/build-apk.yml`) on every push to `main`.
