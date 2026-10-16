import React from 'react';
import { TrendingUp, Bookmark, Search, ShieldCheck } from 'lucide-react';
import type { MarketIndex } from '../types';

interface NavbarProps {
  indices: MarketIndex[];
  watchlistCount: number;
  openIpoCount?: number;
  onOpenWatchlist: () => void;
  activeTab: 'analyzer' | 'screener' | 'ipo';
  setActiveTab: (tab: 'analyzer' | 'screener' | 'ipo') => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  indices,
  watchlistCount,
  openIpoCount = 1,
  onOpenWatchlist,
  activeTab,
  setActiveTab,
}) => {
  return (
    <header className="border-b border-slate-800 bg-slate-900/90 backdrop-blur sticky top-0 z-50">
      {/* Indices Ticker Bar */}
      {indices.length > 0 && (
        <div className="bg-slate-950/80 border-b border-slate-800/60 px-4 py-1.5 text-xs flex items-center gap-6 overflow-x-auto whitespace-nowrap scrollbar-none">
          <span className="text-slate-400 font-semibold flex items-center gap-1">
            <span className="inline-block w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            LIVE MARKETS
          </span>
          {indices.map((idx) => {
            const isPos = idx.change >= 0;
            return (
              <div key={idx.symbol} className="flex items-center gap-2">
                <span className="font-medium text-slate-300">{idx.name}</span>
                <span className="font-semibold text-slate-100">
                  ₹{idx.price.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                </span>
                <span className={`text-[11px] font-medium ${isPos ? 'text-emerald-400' : 'text-rose-400'}`}>
                  {isPos ? '+' : ''}{idx.change_percent.toFixed(2)}%
                </span>
              </div>
            );
          })}
        </div>
      )}

      {/* Main Header */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        {/* Brand */}
        <div className="flex items-center gap-3 cursor-pointer" onClick={() => setActiveTab('analyzer')}>
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-500 via-teal-500 to-indigo-600 flex items-center justify-center shadow-lg shadow-emerald-500/20">
            <TrendingUp className="w-6 h-6 text-white" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="text-lg font-bold tracking-tight text-white">
                Dhakrey<span className="text-emerald-400">Stock</span> AI
              </span>
              <span className="text-[10px] bg-emerald-950 text-emerald-400 border border-emerald-800/80 px-2 py-0.5 rounded-full font-semibold uppercase tracking-wider">
                NSE & BSE
              </span>
            </div>
            <p className="text-xs text-slate-400">Hybrid Valuation & Buy / Sell Decision Engine</p>
          </div>
        </div>

        {/* Navigation Tabs & Actions */}
        <div className="flex items-center gap-3">
          <div className="bg-slate-800/80 p-1 rounded-xl flex items-center border border-slate-700/60">
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

          <button
            onClick={onOpenWatchlist}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-slate-700/80 bg-slate-800/60 hover:bg-slate-800 text-slate-200 text-xs font-medium transition-colors"
          >
            <Bookmark className="w-3.5 h-3.5 text-amber-400" />
            <span>Watchlist</span>
            {watchlistCount > 0 && (
              <span className="w-4 h-4 rounded-full bg-emerald-500 text-slate-950 text-[10px] font-bold flex items-center justify-center ml-0.5">
                {watchlistCount}
              </span>
            )}
          </button>
        </div>
      </div>
    </header>
  );
};
