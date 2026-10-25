import React, { useState, useEffect } from 'react';
import { Navbar } from './components/Navbar';
import { SearchHeader } from './components/SearchHeader';
import { ExploreView } from './components/ExploreView';
import { SectorDetailView } from './components/SectorDetailView';
import { StockDetailView } from './components/StockDetailView';
import { ScreenerView } from './components/ScreenerView';
import { IPODashboard } from './components/IPODashboard';
import { WatchlistDrawer } from './components/WatchlistDrawer';
import { DownloadAppModal } from './components/DownloadAppModal';
import { adService } from './services/adService';
import type { WatchlistEntry } from './components/WatchlistDrawer';
import type { StockAnalysisResponse, MarketIndex } from './types';
import { Loader2, AlertCircle, RefreshCw, WifiOff } from 'lucide-react';
import { API_BASE_URL } from './config';
import { mobileService } from './services/mobileService';
import { Capacitor } from '@capacitor/core';

// Helper to read initial state from URL parameters or localStorage
// Defaults to Explore tab with NO stock selected by default
const getInitialNavState = (): { activeTab: 'explore' | 'screener' | 'ipo'; currentSymbol: string | null } => {
  try {
    const params = new URLSearchParams(window.location.search);
    const urlTab = params.get('tab') as 'explore' | 'screener' | 'ipo' | null;
    const urlStock = params.get('stock');

    const validTabs: ('explore' | 'screener' | 'ipo')[] = ['explore', 'screener', 'ipo'];
    const savedTab = localStorage.getItem('dhakreystock_active_tab') as 'explore' | 'screener' | 'ipo' | null;

    // Do NOT select a stock by default unless explicitly specified in URL (?stock=...)
    const currentSymbol = urlStock && urlStock.trim() ? urlStock.trim().toUpperCase() : null;

    const activeTab: 'explore' | 'screener' | 'ipo' = (urlTab && validTabs.includes(urlTab))
      ? urlTab
      : (savedTab && validTabs.includes(savedTab))
      ? savedTab
      : 'explore'; // The 1st tab is Explore!

    return { activeTab, currentSymbol };
  } catch {
    return { activeTab: 'explore', currentSymbol: null };
  }
};

export function App() {
  const [navState] = useState(getInitialNavState);
  const [currentSymbol, setCurrentSymbol] = useState<string | null>(navState.currentSymbol);
  const [selectedSector, setSelectedSector] = useState<string | null>(null);
  const [stock, setStock] = useState<StockAnalysisResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<'explore' | 'screener' | 'ipo'>(navState.activeTab);
  const [previousTab, setPreviousTab] = useState<'explore' | 'screener' | 'ipo' | null>(null);
  const [indices, setIndices] = useState<MarketIndex[]>([]);
  const [isWatchlistOpen, setIsWatchlistOpen] = useState<boolean>(false);
  const [isDownloadModalOpen, setIsDownloadModalOpen] = useState<boolean>(false);
  const [isOffline, setIsOffline] = useState<boolean>(() => typeof navigator !== 'undefined' && !navigator.onLine);
  const [openIpoCount, setOpenIpoCount] = useState<number>(0);

  // Fetch live Open IPO count for header badge
  useEffect(() => {
    fetch(`${API_BASE_URL}/api/ipo/summary?type=all`)
      .then((res) => (res.ok ? res.json() : null))
      .then((data) => {
        if (data && typeof data.open_count === 'number') {
          setOpenIpoCount(data.open_count);
        }
      })
      .catch(() => {});
  }, []);

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
      // If viewing a stock, back button returns to Sector / Explore
      if (currentSymbol) {
        handleBackFromStock();
        return true;
      }
      // If viewing a sector, back button returns to Explore home
      if (selectedSector) {
        setSelectedSector(null);
        return true;
      }
      if (activeTab !== 'explore') {
        setActiveTab('explore');
        setPreviousTab(null);
        return true;
      }
      return false; // Let native app exit
    });

    return unregister;
  }, [isWatchlistOpen, isDownloadModalOpen, activeTab, previousTab, currentSymbol, selectedSector]);

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
      if (currentSymbol) {
        localStorage.setItem('dhakreystock_current_symbol', currentSymbol);
      } else {
        localStorage.removeItem('dhakreystock_current_symbol');
      }
      localStorage.setItem('dhakreystock_active_tab', activeTab);

      const url = new URL(window.location.href);
      url.searchParams.set('tab', activeTab);
      if (currentSymbol) {
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
      const tab = params.get('tab') as 'explore' | 'screener' | 'ipo' | null;
      const stockParam = params.get('stock');
      if (tab && ['explore', 'screener', 'ipo'].includes(tab)) {
        setActiveTab(tab);
      }
      if (stockParam) {
        setCurrentSymbol(stockParam.toUpperCase());
      } else {
        setCurrentSymbol(null);
        setStock(null);
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

  // Fetch stock data only when currentSymbol is explicitly selected
  useEffect(() => {
    if (currentSymbol) {
      fetchStockAnalysis(currentSymbol);
    } else {
      setStock(null);
      setLoading(false);
      setError(null);
    }
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
    } else {
      setPreviousTab('explore');
    }
    setCurrentSymbol(symbol);
    setActiveTab('explore');
    try {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } catch {
      // Fallback
    }
  };

  const handleBackFromStock = () => {
    setCurrentSymbol(null);
    setStock(null);
    try {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } catch {
      // Fallback
    }
  };

  const handleBackToExplore = () => {
    if (previousTab && previousTab !== 'explore') {
      setActiveTab(previousTab);
      setPreviousTab(null);
    } else {
      setActiveTab('explore');
      setPreviousTab(null);
    }
    setCurrentSymbol(null);
    setSelectedSector(null);
    setStock(null);
    try {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } catch {
      // Fallback
    }
  };

  const handleTabChange = (tab: 'explore' | 'screener' | 'ipo') => {
    if (tab === 'explore') {
      // Return directly to Explore home
      setCurrentSymbol(null);
      setSelectedSector(null);
      setStock(null);
      setPreviousTab(null);
    }
    setActiveTab(tab);
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
        openIpoCount={openIpoCount}
        onOpenWatchlist={() => setIsWatchlistOpen(true)}
        onOpenDownloadApp={Capacitor.isNativePlatform() ? undefined : () => setIsDownloadModalOpen(true)}
        activeTab={activeTab}
        setActiveTab={handleTabChange}
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
        {/* Explore View (The 1st Tab - Default State: No stock selected by default) */}
        <div className={activeTab === 'explore' ? 'block' : 'hidden'}>
          {currentSymbol ? (
            /* Stock Detail View (When a stock is explicitly selected) */
            <div className="space-y-4 sm:space-y-6">
              {/* Search Bar for Quick Stock Lookup */}
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
                      Running DCF intrinsic cash flow, Graham multiples, RSI-14, and valuation algorithms
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
                  <div className="pt-2 flex items-center justify-center gap-2">
                    <button
                      onClick={() => fetchStockAnalysis(currentSymbol)}
                      className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold inline-flex items-center gap-1.5 transition-colors cursor-pointer"
                    >
                      <RefreshCw className="w-3.5 h-3.5" />
                      <span>Try Again</span>
                    </button>
                    <button
                      onClick={handleBackFromStock}
                      className="px-4 py-2 rounded-xl bg-slate-900 border border-slate-700 hover:bg-slate-800 text-slate-300 text-xs font-semibold transition-colors cursor-pointer"
                    >
                      Back
                    </button>
                  </div>
                </div>
              )}

              {/* Loaded Simplified Stock Content */}
              {!loading && !error && stock && (
                <StockDetailView
                  stock={stock}
                  onBack={handleBackFromStock}
                  isWatchlisted={isCurrentWatchlisted}
                  onToggleWatchlist={handleToggleWatchlist}
                />
              )}
            </div>
          ) : selectedSector ? (
            /* Sector Deep-Dive Page (When a sector is clicked from Explore) */
            <div className="space-y-5">
              <SectorDetailView
                sectorName={selectedSector}
                onBack={() => setSelectedSector(null)}
                onSelectStock={handleSelectStock}
              />
            </div>
          ) : (
            /* Explore Home Dashboard: Most Traded Stocks, Top Movers, Sectors Trending */
            <div className="space-y-6">
              {/* Search Bar at Top */}
              <SearchHeader onSelectStock={handleSelectStock} />

              {/* Groww Explore Layout */}
              <ExploreView
                onSelectStock={handleSelectStock}
                onExploreSector={(sectorName) => {
                  setSelectedSector(sectorName);
                  window.scrollTo({ top: 0, behavior: 'smooth' });
                }}
              />
            </div>
          )}
        </div>

        {/* Screener View - Kept mounted to preserve filter state and exact scroll position */}
        <div className={activeTab === 'screener' ? 'block' : 'hidden'}>
          <ScreenerView onSelectStock={handleSelectStock} />
        </div>

        {/* IPO Dashboard - Kept mounted to preserve scroll position */}
        <div className={activeTab === 'ipo' ? 'block' : 'hidden'}>
          <IPODashboard />
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
