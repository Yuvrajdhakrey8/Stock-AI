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
import { DownloadAppModal } from './components/DownloadAppModal';
import { adService } from './services/adService';
import type { WatchlistEntry } from './components/WatchlistDrawer';
import type { StockAnalysisResponse, MarketIndex } from './types';
import { Loader2, AlertCircle, RefreshCw, WifiOff, ArrowLeft } from 'lucide-react';
import { API_BASE_URL } from './config';
import { mobileService } from './services/mobileService';
import { Capacitor } from '@capacitor/core';

// Helper to read initial state from URL parameters or localStorage
const getInitialNavState = (): { activeTab: 'analyzer' | 'screener' | 'ipo'; currentSymbol: string } => {
  try {
    const params = new URLSearchParams(window.location.search);
    const urlTab = params.get('tab') as 'analyzer' | 'screener' | 'ipo' | null;
    const urlStock = params.get('stock');

    const validTabs: ('analyzer' | 'screener' | 'ipo')[] = ['analyzer', 'screener', 'ipo'];
    const savedTab = localStorage.getItem('dhakreystock_active_tab') as 'analyzer' | 'screener' | 'ipo' | null;
    const savedStock = localStorage.getItem('dhakreystock_current_symbol');

    const activeTab: 'analyzer' | 'screener' | 'ipo' = (urlTab && validTabs.includes(urlTab))
      ? urlTab
      : (savedTab && validTabs.includes(savedTab))
      ? savedTab
      : 'screener'; // Default to Screener for discovery & suggestions

    const currentSymbol = urlStock && urlStock.trim()
      ? urlStock.trim().toUpperCase()
      : savedStock && savedStock.trim()
      ? savedStock.trim().toUpperCase()
      : 'RELIANCE.NS';

    return { activeTab, currentSymbol };
  } catch {
    return { activeTab: 'screener', currentSymbol: 'RELIANCE.NS' };
  }
};

export function App() {
  const [navState] = useState(getInitialNavState);
  const [currentSymbol, setCurrentSymbol] = useState<string>(navState.currentSymbol);
  const [stock, setStock] = useState<StockAnalysisResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<'analyzer' | 'screener' | 'ipo'>(navState.activeTab);
  const [previousTab, setPreviousTab] = useState<'screener' | 'ipo' | null>(null);
  const [indices, setIndices] = useState<MarketIndex[]>([]);
  const [isWatchlistOpen, setIsWatchlistOpen] = useState<boolean>(false);
  const [isDownloadModalOpen, setIsDownloadModalOpen] = useState<boolean>(false);
  const [isOffline, setIsOffline] = useState<boolean>(() => typeof navigator !== 'undefined' && !navigator.onLine);

  // Initialize Native Mobile features (AdMob, Status Bar, Back Button)
  useEffect(() => {
    adService.initialize();
    mobileService.initialize();
  }, []);

  // Hardware Back Button integration for Android
  useEffect(() => {
    const unregister = mobileService.registerBackHandler(() => {
      if (isWatchlistOpen) {
        setIsWatchlistOpen(false);
        return true;
      }
      if (isDownloadModalOpen) {
        setIsDownloadModalOpen(false);
        return true;
      }
      if (activeTab === 'analyzer' && previousTab) {
        setActiveTab(previousTab);
        setPreviousTab(null);
        return true;
      }
      if (activeTab !== 'screener') {
        setActiveTab('screener');
        setPreviousTab(null);
        return true;
      }
      return false; // Let native app exit
    });

    return unregister;
  }, [isWatchlistOpen, isDownloadModalOpen, activeTab, previousTab]);

  const fetchIndices = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/indices`);
      if (res.ok) {
        const data = await res.json();
        setIndices(data.indices || []);
      }
    } catch (err) {
      console.error('Failed to load indices:', err);
    }
  };

  // Online / Offline network listeners
  useEffect(() => {
    const handleOnline = () => {
      setIsOffline(false);
      fetchIndices();
      if (currentSymbol) {
        fetchStockAnalysis(currentSymbol);
      }
    };
    const handleOffline = () => setIsOffline(true);

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);
    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, [currentSymbol]);

  // Synchronize state with localStorage and URL query parameters
  useEffect(() => {
    try {
      localStorage.setItem('dhakreystock_current_symbol', currentSymbol);
      localStorage.setItem('dhakreystock_active_tab', activeTab);

      const url = new URL(window.location.href);
      url.searchParams.set('tab', activeTab);
      if (activeTab === 'analyzer' && currentSymbol) {
        url.searchParams.set('stock', currentSymbol);
      } else {
        url.searchParams.delete('stock');
      }
      window.history.replaceState(null, '', url.toString());
    } catch (e) {
      console.error('Failed to persist navigation state', e);
    }
  }, [currentSymbol, activeTab]);

  // Handle browser back and forward button navigation
  useEffect(() => {
    const handlePopState = () => {
      const params = new URLSearchParams(window.location.search);
      const tab = params.get('tab') as 'analyzer' | 'screener' | 'ipo' | null;
      const stockParam = params.get('stock');
      if (tab && ['analyzer', 'screener', 'ipo'].includes(tab)) {
        setActiveTab(tab);
      }
      if (stockParam) {
        setCurrentSymbol(stockParam.toUpperCase());
      }
    };
    window.addEventListener('popstate', handlePopState);
    return () => window.removeEventListener('popstate', handlePopState);
  }, []);

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
      const res = await fetch(`${API_BASE_URL}/api/stock/${encodeURIComponent(symbol)}`);
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
    if (activeTab === 'screener' || activeTab === 'ipo') {
      setPreviousTab(activeTab);
    }
    setCurrentSymbol(symbol);
    setActiveTab('analyzer');
    try {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } catch {
      // Fallback
    }
  };

  const handleGoBack = () => {
    if (previousTab) {
      setActiveTab(previousTab);
      setPreviousTab(null);
    } else {
      setActiveTab('screener');
      setPreviousTab(null);
    }
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
        onOpenDownloadApp={Capacitor.isNativePlatform() ? undefined : () => setIsDownloadModalOpen(true)}
        activeTab={activeTab}
        setActiveTab={setActiveTab}
      />

      {/* Offline Alert Banner */}
      {isOffline && (
        <div className="bg-amber-500/95 text-slate-950 px-4 py-2 text-xs font-bold flex items-center justify-center gap-2 shadow-lg">
          <WifiOff className="w-4 h-4 shrink-0" />
          <span>No Internet Connection • Retrying live market data when connection restores...</span>
        </div>
      )}

      {/* Main Content Area */}
      <main className={`flex-1 max-w-7xl w-full mx-auto px-3 sm:px-6 lg:px-8 py-4 sm:py-6 space-y-4 sm:space-y-6 ${
        Capacitor.isNativePlatform() ? 'pb-admob-buffer' : ''
      }`}>
        {/* Screener View - Kept mounted to preserve filter state and exact scroll position */}
        <div className={activeTab === 'screener' ? 'block' : 'hidden'}>
          <ScreenerView onSelectStock={handleSelectStock} />
        </div>

        {/* IPO Dashboard - Kept mounted to preserve scroll position */}
        <div className={activeTab === 'ipo' ? 'block' : 'hidden'}>
          <IPODashboard />
        </div>

        {/* Stock Analyzer View */}
        <div className={activeTab === 'analyzer' ? 'block space-y-4 sm:space-y-6' : 'hidden'}>
          {/* Prominent Back to Screener / IPO button */}
          {previousTab && (
            <div className="flex items-center justify-between pb-1 animate-in fade-in duration-200">
              <button
                onClick={handleGoBack}
                className="inline-flex items-center gap-2 px-3.5 py-2 rounded-xl bg-slate-900 border border-slate-700/90 text-slate-200 hover:text-white hover:bg-slate-800 text-xs sm:text-sm font-semibold transition-all shadow-md active:scale-95 group"
              >
                <ArrowLeft className="w-4 h-4 text-emerald-400 group-hover:-translate-x-1 transition-transform" />
                <span>Back to {previousTab === 'screener' ? 'Screener' : 'IPO Research'}</span>
              </button>
              <span className="text-[11px] text-slate-400 hidden xs:inline">
                Viewing analysis for <span className="text-white font-bold">{currentSymbol}</span>
              </span>
            </div>
          )}

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
        </div>
      </main>

      {/* Watchlist Side Drawer */}
      <WatchlistDrawer
        isOpen={isWatchlistOpen}
        onClose={() => setIsWatchlistOpen(false)}
        watchlist={watchlist}
        onSelectStock={handleSelectStock}
        onRemoveFromWatchlist={handleRemoveFromWatchlist}
      />

      {/* Download App Modal & Smart Banner (only for browser visitors) */}
      {!Capacitor.isNativePlatform() && (
        <DownloadAppModal
          forceOpen={isDownloadModalOpen}
          onClose={() => setIsDownloadModalOpen(false)}
        />
      )}

      {/* Footer */}
      <footer className={`border-t border-slate-800/80 py-6 text-center text-xs text-slate-500 ${
        Capacitor.isNativePlatform() ? 'pb-admob-buffer' : ''
      }`}>
        <p>
          Stocks Suggestions - Dhakrey • Quantitative Stock & IPO Valuation Engine (NSE & BSE)
        </p>
        <p className="text-[11px] text-slate-600 mt-1">
          Designed for educational, fundamental, and IPO analysis. Financial data powered by yfinance & public registries.
        </p>
        <div className="mt-3 flex items-center justify-center gap-4 text-[11px] text-slate-500">
          <a
            href="/privacy-policy.html"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-emerald-400 transition-colors underline"
          >
            Privacy Policy
          </a>
          {!Capacitor.isNativePlatform() && (
            <>
              <span>•</span>
              <button
                onClick={() => setIsDownloadModalOpen(true)}
                className="hover:text-emerald-400 transition-colors"
              >
                Download Mobile App
              </button>
            </>
          )}
        </div>
      </footer>
    </div>
  );
}

export default App;
