import React from 'react';
import { TrendingUp, Bookmark, Search, ShieldCheck, Smartphone } from 'lucide-react';
import type { MarketIndex } from '../types';

interface NavbarProps {
  indices: MarketIndex[];
  watchlistCount: number;
  openIpoCount?: number;
  onOpenWatchlist: () => void;
  onOpenDownloadApp?: () => void;
  activeTab: 'analyzer' | 'screener' | 'ipo';
  setActiveTab: (tab: 'analyzer' | 'screener' | 'ipo') => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  indices,
  watchlistCount,
  openIpoCount = 1,
  onOpenWatchlist,
  onOpenDownloadApp,
  activeTab,
  setActiveTab,
}) => {
  return (
    <header className="border-b border-slate-800 bg-slate-900/95 backdrop-blur sticky top-0 z-50">
      {/* Indices Ticker Bar */}
      {indices.length > 0 && (
        <div className="bg-slate-950/90 border-b border-slate-800/60 px-3 sm:px-4 py-1.5 text-[11px] sm:text-xs flex items-center gap-4 sm:gap-6 overflow-x-auto whitespace-nowrap scrollbar-none">
          <span className="text-slate-400 font-semibold flex items-center gap-1.5 shrink-0">
            <span className="inline-block w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
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
                <span className={`text-[10px] sm:text-[11px] font-medium ${isPos ? 'text-emerald-400' : 'text-rose-400'}`}>
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
            onClick={() => setActiveTab('analyzer')}
          >
            <div className="w-8 h-8 sm:w-10 sm:h-10 rounded-xl bg-gradient-to-tr from-emerald-500 via-teal-500 to-indigo-600 flex items-center justify-center shadow-lg shadow-emerald-500/20 shrink-0">
              <TrendingUp className="w-4 h-4 sm:w-6 sm:h-6 text-white" />
            </div>
            <div className="min-w-0">
              <div className="flex items-center gap-1.5 sm:gap-2">
                <span className="text-base sm:text-lg font-bold tracking-tight text-white truncate">
                  Dhakrey<span className="text-emerald-400">Stock</span> AI
                </span>
                <span className="text-[9px] sm:text-[10px] bg-emerald-950 text-emerald-400 border border-emerald-800/80 px-1.5 sm:px-2 py-0.2 rounded-full font-semibold uppercase tracking-wider shrink-0">
                  NSE & BSE
                </span>
              </div>
              <p className="text-[10px] sm:text-xs text-slate-400 hidden sm:block truncate">
                Hybrid Valuation & Buy / Sell Decision Engine
              </p>
            </div>
          </div>

          {/* Desktop Navigation Tabs */}
          <div className="hidden md:flex items-center gap-2 bg-slate-800/80 p-1 rounded-xl border border-slate-700/60">
            <button
              onClick={() => setActiveTab('analyzer')}
              className={`px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all ${
                activeTab === 'analyzer'
                  ? 'bg-emerald-500 text-slate-950 shadow-sm font-semibold'
                  : 'text-slate-300 hover:text-white'
              }`}
            >
              Stock Analyzer
            </button>
            <button
              onClick={() => setActiveTab('screener')}
              className={`px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all ${
                activeTab === 'screener'
                  ? 'bg-emerald-500 text-slate-950 shadow-sm font-semibold'
                  : 'text-slate-300 hover:text-white'
              }`}
            >
              Market Screener
            </button>
            <button
              onClick={() => setActiveTab('ipo')}
              className={`px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 ${
                activeTab === 'ipo'
                  ? 'bg-emerald-500 text-slate-950 shadow-sm font-semibold'
                  : 'text-slate-300 hover:text-white'
              }`}
            >
              <span>IPO Research</span>
              {openIpoCount > 0 && (
                <span className={`text-[10px] px-1.5 py-0.2 rounded-full font-bold ${
                  activeTab === 'ipo' ? 'bg-slate-950 text-emerald-400' : 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40'
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
                className="relative group flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 sm:py-2 rounded-xl bg-gradient-to-r from-emerald-500/25 via-teal-500/20 to-indigo-500/25 hover:from-emerald-500/35 hover:to-indigo-500/35 border border-emerald-500/50 hover:border-emerald-400 text-emerald-300 hover:text-white text-xs font-semibold transition-all duration-300 hover:scale-105 active:scale-95 shadow-sm shadow-emerald-500/10 shrink-0"
                title="Download Android Mobile App"
              >
                {/* Subtle beacon pulse on top right corner */}
                <span className="absolute -top-1 -right-1 flex h-2 w-2 pointer-events-none">
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                  <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                </span>

                <Smartphone className="w-3.5 h-3.5 text-emerald-400 shrink-0 group-hover:-rotate-12 transition-transform duration-300" />
                <span className="hidden sm:inline">Get App</span>
              </button>
            )}

            <button
              onClick={onOpenWatchlist}
              className="flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 sm:py-2 rounded-xl border border-slate-700/80 bg-slate-800/60 hover:bg-slate-800 text-slate-200 text-xs font-medium transition-colors shrink-0"
              title="Open Watchlist"
            >
              <Bookmark className="w-3.5 h-3.5 sm:w-4 sm:h-4 text-amber-400" />
              <span className="hidden xs:inline sm:inline">Watchlist</span>
              {watchlistCount > 0 && (
                <span className="w-4 h-4 rounded-full bg-emerald-500 text-slate-950 text-[10px] font-bold flex items-center justify-center">
                  {watchlistCount}
                </span>
              )}
            </button>
          </div>
        </div>

        {/* Mobile Navigation Tabs (segmented full-width bar for thumb-friendly navigation) */}
        <div className="md:hidden pb-2.5 pt-0.5">
          <div className="bg-slate-950/90 p-1 rounded-xl flex items-center border border-slate-800 w-full text-xs">
            <button
              onClick={() => setActiveTab('analyzer')}
              className={`flex-1 py-2 text-center rounded-lg font-medium transition-all min-h-[38px] flex items-center justify-center ${
                activeTab === 'analyzer'
                  ? 'bg-emerald-500 text-slate-950 shadow-sm font-bold'
                  : 'text-slate-300 hover:text-white'
              }`}
            >
              Analyzer
            </button>
            <button
              onClick={() => setActiveTab('screener')}
              className={`flex-1 py-2 text-center rounded-lg font-medium transition-all min-h-[38px] flex items-center justify-center ${
                activeTab === 'screener'
                  ? 'bg-emerald-500 text-slate-950 shadow-sm font-bold'
                  : 'text-slate-300 hover:text-white'
              }`}
            >
              Screener
            </button>
            <button
              onClick={() => setActiveTab('ipo')}
              className={`flex-1 py-2 text-center rounded-lg font-medium transition-all min-h-[38px] flex items-center justify-center gap-1 ${
                activeTab === 'ipo'
                  ? 'bg-emerald-500 text-slate-950 shadow-sm font-bold'
                  : 'text-slate-300 hover:text-white'
              }`}
            >
              <span>IPO</span>
              {openIpoCount > 0 && (
                <span className={`text-[9px] px-1 py-0.2 rounded font-bold ${
                  activeTab === 'ipo' ? 'bg-slate-950 text-emerald-400' : 'bg-emerald-500/20 text-emerald-400'
                }`}>
                  {openIpoCount}
                </span>
              )}
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};
