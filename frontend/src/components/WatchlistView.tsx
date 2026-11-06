import React, { useState } from 'react';
import { Bookmark, Trash2, ArrowUpRight, Search, PlusCircle, Sparkles } from 'lucide-react';
import type { WatchlistEntry } from './WatchlistDrawer';
import { CompanyLogo } from './CompanyLogo';

interface WatchlistViewProps {
  watchlist: WatchlistEntry[];
  onSelectStock: (symbol: string) => void;
  onRemoveFromWatchlist: (symbol: string) => void;
}

const POPULAR_SUGGESTIONS = [
  { symbol: 'RELIANCE', name: 'Reliance Industries', sector: 'Energy & Retail' },
  { symbol: 'TCS', name: 'Tata Consultancy Services', sector: 'IT Services' },
  { symbol: 'HDFCBANK', name: 'HDFC Bank', sector: 'Banking & Finance' },
  { symbol: 'INFY', name: 'Infosys Ltd', sector: 'IT Services' },
  { symbol: 'TATAMOTORS', name: 'Tata Motors', sector: 'Automobiles' },
  { symbol: 'ITC', name: 'ITC Limited', sector: 'FMCG' },
];

export const WatchlistView: React.FC<WatchlistViewProps> = ({
  watchlist,
  onSelectStock,
  onRemoveFromWatchlist,
}) => {
  const [filterQuery, setFilterQuery] = useState('');

  const filteredItems = watchlist.filter((item) => {
    if (!filterQuery.trim()) return true;
    const q = filterQuery.toLowerCase();
    return (
      item.symbol.toLowerCase().includes(q) ||
      item.name.toLowerCase().includes(q)
    );
  });

  return (
    <div className="space-y-5 max-w-4xl mx-auto">
      {/* Top Header Card */}
      <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-sm">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-slate-800 border border-slate-700/80 flex items-center justify-center text-teal-400 shrink-0">
            <Bookmark className="w-5 h-5 fill-teal-400/20" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-lg sm:text-xl font-bold text-white tracking-tight">
                Watchlist
              </h1>
              <span className="text-xs bg-slate-800 text-slate-300 border border-slate-700 px-2 py-0.5 rounded-full font-semibold">
                {watchlist.length} {watchlist.length === 1 ? 'stock' : 'stocks'}
              </span>
            </div>
            <p className="text-xs text-slate-400 mt-0.5">
              Track real-time prices, DCF fair values & Graham targets
            </p>
          </div>
        </div>

        {/* Search within watchlist (visible if > 2 items) */}
        {watchlist.length > 2 && (
          <div className="relative min-w-[220px]">
            <Search className="w-3.5 h-3.5 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none" />
            <input
              type="text"
              value={filterQuery}
              onChange={(e) => setFilterQuery(e.target.value)}
              placeholder="Search watchlist..."
              className="w-full pl-8 pr-3 py-1.5 text-xs rounded-xl bg-slate-950 border border-slate-800 text-white placeholder-slate-500 focus:outline-none focus:border-slate-600 transition-colors"
            />
          </div>
        )}
      </div>

      {/* Watchlist Items */}
      {watchlist.length === 0 ? (
        /* Clean Empty State with Quick Suggestions */
        <div className="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-8 text-center space-y-4">
          <div className="w-14 h-14 rounded-2xl bg-slate-800/60 border border-slate-700/60 flex items-center justify-center mx-auto text-slate-500">
            <Bookmark className="w-7 h-7 stroke-1" />
          </div>
          <div>
            <h3 className="text-base font-bold text-white">Your Watchlist is Empty</h3>
            <p className="text-xs text-slate-400 max-w-sm mx-auto mt-1">
              Tap the bookmark icon on any stock details page to save and monitor it here.
            </p>
          </div>

          {/* Quick Suggestions to add */}
          <div className="pt-2">
            <p className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-2.5">
              Popular Stocks to Track:
            </p>
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-2 max-w-md mx-auto text-left">
              {POPULAR_SUGGESTIONS.map((sug) => (
                <button
                  key={sug.symbol}
                  onClick={() => onSelectStock(sug.symbol)}
                  className="p-2.5 rounded-xl bg-slate-950/80 hover:bg-slate-800/80 border border-slate-800 hover:border-slate-700 transition-all cursor-pointer group text-left"
                >
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-bold text-white group-hover:text-teal-300 transition-colors">
                      {sug.symbol}
                    </span>
                    <ArrowUpRight className="w-3 h-3 text-slate-500 group-hover:text-teal-400" />
                  </div>
                  <div className="text-[10px] text-slate-400 truncate mt-0.5">
                    {sug.name}
                  </div>
                </button>
              ))}
            </div>
          </div>
        </div>
      ) : filteredItems.length === 0 ? (
        <div className="p-8 text-center bg-slate-900/40 border border-slate-800/60 rounded-2xl text-xs text-slate-400">
          No stocks match "{filterQuery}".
        </div>
      ) : (
        /* Stock List Rows */
        <div className="bg-slate-900/80 border border-slate-800/80 rounded-2xl divide-y divide-slate-800/60 overflow-hidden shadow-sm">
          {filteredItems.map((item) => (
            <div
              key={item.symbol}
              onClick={() => onSelectStock(item.symbol)}
              className="p-3.5 sm:p-4 hover:bg-slate-800/40 active:bg-slate-800/60 transition-colors cursor-pointer flex items-center justify-between gap-3 group"
            >
              {/* Left: Logo & Company Info */}
              <div className="flex items-center gap-3 min-w-0">
                <CompanyLogo
                  symbol={item.symbol}
                  name={item.name}
                  size="md"
                  className="rounded-xl border border-slate-800 shrink-0"
                />
                <div className="min-w-0">
                  <div className="flex items-center gap-1.5 flex-wrap">
                    <span className="font-bold text-white text-sm group-hover:text-teal-300 transition-colors">
                      {item.symbol}
                    </span>
                    <span className="text-[10px] text-slate-400">
                      • {item.exchange}
                    </span>
                  </div>
                  <div className="text-xs text-slate-400 truncate mt-0.5 max-w-[200px] sm:max-w-xs">
                    {item.name}
                  </div>
                </div>
              </div>

              {/* Right: Price, Verdict & Delete */}
              <div className="flex items-center gap-3 shrink-0">
                <div className="text-right">
                  <div className="font-bold text-white text-sm tracking-tight">
                    ₹{item.current_price?.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                  </div>
                  <span
                    className={`text-[10px] font-bold px-2 py-0.5 rounded-md inline-block mt-0.5 ${
                      item.verdict === 'BEST BUY'
                        ? 'bg-teal-950/60 text-teal-300 border border-teal-800/50'
                        : item.verdict === 'CURRENTLY EXPENSIVE'
                        ? 'bg-rose-950/60 text-rose-300 border border-rose-800/50'
                        : 'bg-amber-950/60 text-amber-300 border border-amber-800/50'
                    }`}
                  >
                    {item.verdict}
                  </span>
                </div>

                {/* Remove from watchlist button */}
                <button
                  type="button"
                  onClick={(e) => {
                    e.stopPropagation();
                    onRemoveFromWatchlist(item.symbol);
                  }}
                  className="p-2 text-slate-500 hover:text-rose-400 hover:bg-rose-950/40 rounded-xl transition-colors cursor-pointer"
                  title="Remove from watchlist"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
