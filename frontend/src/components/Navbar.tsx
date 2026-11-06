import React from 'react';
import { TrendingUp, Bookmark, Search, ShieldCheck, Smartphone } from 'lucide-react';
import type { MarketIndex } from '../types';

interface NavbarProps {
  indices: MarketIndex[];
  watchlistCount: number;
  openIpoCount?: number;
  onOpenWatchlist: () => void;
  onOpenDownloadApp?: () => void;
  activeTab: 'explore' | 'analyzer' | 'screener' | 'ipo';
  setActiveTab: (tab: 'explore' | 'screener' | 'ipo') => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  indices,
  watchlistCount,
  openIpoCount = 0,
  onOpenWatchlist,
  onOpenDownloadApp,
  activeTab,
  setActiveTab,
}) => {
  return (
    <header className="border-b border-slate-800 bg-slate-900/95 backdrop-blur sticky top-0 z-50 pt-safe">
      {/* Indices Ticker Bar */}
      {indices.length > 0 && (
        <div className="bg-slate-950/90 border-b border-slate-800/60 px-3 sm:px-4 py-1.5 text-[11px] sm:text-xs flex items-center gap-4 sm:gap-6 overflow-x-auto whitespace-nowrap scrollbar-none">
          <span className="text-slate-400 font-semibold flex items-center gap-1.5 shrink-0">
            <span className="inline-block w-2 h-2 rounded-full bg-teal-400" />
            LIVE MARKETS
          </span>
          {indices.map((idx) => {
            const isPos = idx.change >= 0;
            return (
              <div key={idx.symbol} className="flex items-center gap-1.5 shrink-0">
                <span className="font-medium text-slate-300">{idx.name}</span>
                <span className="font-semibold text-slate-100">
                  ₹{idx.price.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                </span>
                <span className={`text-[10px] sm:text-[11px] font-medium ${isPos ? 'text-teal-400' : 'text-rose-400'}`}>
                  {isPos ? '+' : ''}{idx.change_percent.toFixed(2)}%
                </span>
              </div>
            );
          })}
        </div>
      )}

      {/* Main Header Container */}
      <div className="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
        <div className="h-14 sm:h-16 flex items-center justify-between gap-3">
          {/* Brand */}
          <div
            className="flex items-center gap-2.5 sm:gap-3 cursor-pointer select-none"
            onClick={() => setActiveTab('explore')}
          >
            <img
              src="/logo.png"
              alt="Stockly"
              className="w-8 h-8 sm:w-10 sm:h-10 rounded-xl object-contain shrink-0 border border-slate-800 shadow-sm"
            />
            <div className="min-w-0">
              <div className="flex items-center gap-1.5 sm:gap-2">
                <span className="text-base sm:text-lg font-bold tracking-tight text-white truncate">
                  Stockly
                </span>
                <span className="text-[9px] sm:text-[10px] bg-slate-800 text-slate-300 border border-slate-700/60 px-1.5 sm:px-2 py-0.2 rounded-full font-medium uppercase tracking-wider shrink-0">
                  NSE & BSE
                </span>
              </div>
              <p className="text-[10px] sm:text-xs text-slate-400 hidden sm:block truncate">
                Stock Valuation & Live IPO Tracker
              </p>
            </div>
          </div>

          {/* Desktop Navigation Tabs: Cool, Calm Slate Navigation (Groww Style) */}
          <div className="hidden md:flex items-center gap-1 bg-slate-950 p-1 rounded-xl border border-slate-800">
            <button
              onClick={() => setActiveTab('explore')}
              className={`px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all cursor-pointer ${
                activeTab === 'explore' || activeTab === 'analyzer'
                  ? 'bg-slate-800 text-white font-semibold shadow-sm border border-slate-700/80'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              Explore
            </button>
            <button
              onClick={() => setActiveTab('screener')}
              className={`px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all cursor-pointer ${
                activeTab === 'screener'
                  ? 'bg-slate-800 text-white font-semibold shadow-sm border border-slate-700/80'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              Market Screener
            </button>
            <button
              onClick={() => setActiveTab('ipo')}
              className={`px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 cursor-pointer ${
                activeTab === 'ipo'
                  ? 'bg-slate-800 text-white font-semibold shadow-sm border border-slate-700/80'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              <span>IPO Research</span>
              {openIpoCount > 0 && (
                <span className={`text-[10px] px-1.5 py-0.2 rounded-full font-medium ${
                  activeTab === 'ipo' ? 'bg-slate-700 text-slate-200' : 'bg-slate-850 text-slate-400 border border-slate-750'
                }`}>
                  {openIpoCount} Open
                </span>
              )}
            </button>
          </div>

          {/* Action Buttons: Get App & Watchlist */}
          <div className="flex items-center gap-2">
            {onOpenDownloadApp && (
              <button
                onClick={onOpenDownloadApp}
                className="flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 sm:py-2 rounded-xl border border-slate-700/80 bg-slate-850 hover:bg-slate-800 text-slate-200 text-xs font-medium transition-colors shadow-sm shrink-0 cursor-pointer"
                title="Download Android Mobile App"
              >
                <Smartphone className="w-3.5 h-3.5 text-slate-300 shrink-0" />
                <span className="hidden sm:inline">Get App</span>
              </button>
            )}

            <button
              onClick={onOpenWatchlist}
              className="flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 sm:py-2 rounded-xl border border-slate-700/80 bg-slate-850 hover:bg-slate-800 text-slate-200 text-xs font-medium transition-colors shrink-0 cursor-pointer"
              title="Open Watchlist"
            >
              <Bookmark className="w-3.5 h-3.5 sm:w-4 sm:h-4 text-slate-300" />
              <span className="hidden xs:inline sm:inline">Watchlist</span>
              {watchlistCount > 0 && (
                <span className="w-4 h-4 rounded-full bg-slate-700 text-white text-[10px] font-bold flex items-center justify-center">
                  {watchlistCount}
                </span>
              )}
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};
