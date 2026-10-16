import React, { useState, useEffect } from 'react';
import { Navbar } from './components/Navbar';
import { SearchHeader } from './components/SearchHeader';
import { ValuationMeter } from './components/ValuationMeter';
import { StockOverview } from './components/StockOverview';
import { FundamentalGrid } from './components/FundamentalGrid';
import { TechnicalChart } from './components/TechnicalChart';
import { ScreenerView } from './components/ScreenerView';
import { IPODashboard } from './components/IPODashboard';
import { WatchlistDrawer } from './components/WatchlistDrawer';
import type { WatchlistEntry } from './components/WatchlistDrawer';
import type { StockAnalysisResponse, MarketIndex } from './types';
import { Loader2, AlertCircle, RefreshCw } from 'lucide-react';

export function App() {
  const [currentSymbol, setCurrentSymbol] = useState<string>('RELIANCE.NS');
  const [stock, setStock] = useState<StockAnalysisResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<'analyzer' | 'screener' | 'ipo'>('analyzer');
  const [indices, setIndices] = useState<MarketIndex[]>([]);
  const [isWatchlistOpen, setIsWatchlistOpen] = useState<boolean>(false);

  // Watchlist persisted in localStorage
  const [watchlist, setWatchlist] = useState<WatchlistEntry[]>(() => {
    try {
      const saved = localStorage.getItem('dhakreystock_watchlist') || localStorage.getItem('bharatstock_watchlist');
      return saved ? JSON.parse(saved) : [];
    } catch {
      return [];
    }
  });

  useEffect(() => {
    try {
      localStorage.setItem('dhakreystock_watchlist', JSON.stringify(watchlist));
    } catch (e) {
      console.error('Failed to save watchlist to localStorage', e);
    }
  }, [watchlist]);

  // Fetch benchmark indices
  useEffect(() => {
    const fetchIndices = async () => {
      try {
        const res = await fetch('/api/indices');
        if (res.ok) {
          const data = await res.json();
          setIndices(data.indices || []);
        }
      } catch (err) {
        console.error('Failed to load indices:', err);
      }
    };
    fetchIndices();
  }, []);

  // Fetch stock data whenever currentSymbol changes
  useEffect(() => {
    fetchStockAnalysis(currentSymbol);
  }, [currentSymbol]);

  const fetchStockAnalysis = async (symbol: string) => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(`/api/stock/${encodeURIComponent(symbol)}`);
      if (!res.ok) {
        const errData = await res.json().catch(() => ({ detail: 'Failed to fetch stock analysis.' }));
        throw new Error(errData.detail || `Unable to load data for ${symbol}`);
      }
      const data: StockAnalysisResponse = await res.json();
      setStock(data);
    } catch (err: any) {
      setError(err.message || 'Error connecting to stock market data service.');
    } finally {
      setLoading(false);
    }
  };

  const handleSelectStock = (symbol: string) => {
    setCurrentSymbol(symbol);
    setActiveTab('analyzer');
  };

  const isCurrentWatchlisted = Boolean(
    stock && watchlist.some((item) => item.symbol === stock.symbol)
  );

  const handleToggleWatchlist = () => {
    if (!stock) return;
    if (isCurrentWatchlisted) {
      setWatchlist((prev) => prev.filter((item) => item.symbol !== stock.symbol));
    } else {
      const newEntry: WatchlistEntry = {
        symbol: stock.symbol,
        name: stock.name,
        exchange: stock.exchange,
        current_price: stock.current_price,
        verdict: stock.valuation.verdict,
      };
      setWatchlist((prev) => [newEntry, ...prev]);
    }
  };

  const handleRemoveFromWatchlist = (symbol: string) => {
    setWatchlist((prev) => prev.filter((item) => item.symbol !== symbol));
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col selection:bg-emerald-500 selection:text-slate-950">
      {/* Top Navigation */}
      <Navbar
        indices={indices}
        watchlistCount={watchlist.length}
        onOpenWatchlist={() => setIsWatchlistOpen(true)}
        activeTab={activeTab}
        setActiveTab={setActiveTab}
      />

      {/* Main Content Area */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 space-y-6">
        {activeTab === 'screener' ? (
          <ScreenerView onSelectStock={handleSelectStock} />
        ) : activeTab === 'ipo' ? (
          <IPODashboard />
        ) : (
          <>
            {/* Search Bar & Fast Ticker Chips */}
            <SearchHeader
              onSelectStock={handleSelectStock}
              currentSymbol={currentSymbol}
            />

            {/* Loading State */}
            {loading && (
              <div className="py-24 text-center space-y-4">
                <div className="relative w-16 h-16 mx-auto">
                  <div className="w-16 h-16 rounded-full border-4 border-slate-800 border-t-emerald-400 animate-spin" />
                  <Loader2 className="w-6 h-6 text-emerald-400 absolute inset-0 m-auto animate-pulse" />
                </div>
                <div>
                  <h3 className="text-base font-semibold text-white">
                    Evaluating {currentSymbol}...
                  </h3>
                  <p className="text-xs text-slate-400 mt-1">
                    Running DCF intrinsic cash flow, Graham multiples, RSI-14, and moving average cross algorithms
                  </p>
                </div>
              </div>
            )}

            {/* Error State */}
            {!loading && error && (
              <div className="bg-rose-950/40 border border-rose-800/80 rounded-3xl p-8 text-center space-y-3">
                <AlertCircle className="w-10 h-10 text-rose-400 mx-auto" />
                <h3 className="text-base font-bold text-white">Stock Analysis Unavailable</h3>
                <p className="text-xs text-rose-300 max-w-md mx-auto">{error}</p>
                <div className="pt-2">
                  <button
                    onClick={() => fetchStockAnalysis(currentSymbol)}
                    className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold inline-flex items-center gap-1.5 transition-colors"
                  >
                    <RefreshCw className="w-3.5 h-3.5" />
                    <span>Try Again</span>
                  </button>
                </div>
              </div>
            )}

            {/* Loaded Stock Content */}
            {!loading && !error && stock && (
              <div className="space-y-6 animate-in fade-in duration-300">
                {/* 1. Quantitative Valuation Verdict Gauge */}
                <ValuationMeter
                  valuation={stock.valuation}
                  currency={stock.currency}
                />

                {/* 2. Stock Overview: Price, Change, 52W Range */}
                <StockOverview
                  stock={stock}
                  isWatchlisted={isCurrentWatchlisted}
                  onToggleWatchlist={handleToggleWatchlist}
                />

                {/* 3. Price History & Technical Moving Averages Chart */}
                <TechnicalChart
                  chartData={stock.chart}
                  valuation={stock.valuation}
                  currentPrice={stock.current_price}
                />

                {/* 4. Fundamental Scorecards: DCF, Graham, P/E, PEG, ROE */}
                <FundamentalGrid stock={stock} />
              </div>
            )}
          </>
        )}
      </main>

      {/* Watchlist Side Drawer */}
      <WatchlistDrawer
        isOpen={isWatchlistOpen}
        onClose={() => setIsWatchlistOpen(false)}
        watchlist={watchlist}
        onSelectStock={handleSelectStock}
        onRemoveFromWatchlist={handleRemoveFromWatchlist}
      />

      {/* Footer */}
      <footer className="border-t border-slate-800/80 py-6 text-center text-xs text-slate-500">
        <p>
          DhakreyStock AI • Quantitative Stock & IPO Valuation Engine (NSE & BSE)
        </p>
        <p className="text-[11px] text-slate-600 mt-1">
          Designed for long-term fundamental, swing, and IPO analysis. Financial data powered by yfinance & public registries.
        </p>
      </footer>
    </div>
  );
}

export default App;
