import React from 'react';
import { Bookmark, BookmarkCheck, ExternalLink, Activity, BarChart2 } from 'lucide-react';
import type { StockAnalysisResponse } from '../types';

interface StockOverviewProps {
  stock: StockAnalysisResponse;
  isWatchlisted: boolean;
  onToggleWatchlist: () => void;
}

export const StockOverview: React.FC<StockOverviewProps> = ({
  stock,
  isWatchlisted,
  onToggleWatchlist,
}) => {
  const isPositive = stock.change >= 0;
  const low52 = stock.high_52 && stock.low_52 ? stock.low_52 : stock.current_price * 0.8;
  const high52 = stock.high_52 && stock.low_52 ? stock.high_52 : stock.current_price * 1.2;
  
  // Calculate percentage within 52w range
  const rangeSpan = high52 - low52;
  const positionPercent = rangeSpan > 0 
    ? Math.min(Math.max(((stock.current_price - low52) / rangeSpan) * 100, 0), 100) 
    : 50;

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-3xl p-6 shadow-xl">
      <div className="flex flex-col md:flex-row md:items-start justify-between gap-4">
        {/* Company Title & Exchange Info */}
        <div>
          <div className="flex items-center gap-2.5 flex-wrap">
            <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
              {stock.name}
            </h1>
            <span className="px-2.5 py-0.5 rounded-lg text-xs font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
              {stock.exchange}
            </span>
            <span className="font-mono text-xs font-semibold text-slate-400 px-2 py-0.5 rounded bg-slate-800 border border-slate-700">
              {stock.symbol}
            </span>
          </div>

          <div className="flex items-center gap-2 mt-2 text-xs text-slate-400 flex-wrap">
            <span className="px-2 py-0.5 rounded bg-slate-800/80 text-slate-300 border border-slate-700/60 font-medium">
              {stock.sector}
            </span>
            <span>•</span>
            <span className="text-slate-400">{stock.industry}</span>
            <span>•</span>
            <span className="text-slate-300 font-medium">
              M-Cap: <span className="text-white font-semibold">{stock.market_cap_formatted}</span>
            </span>
          </div>
        </div>

        {/* Live Price & Watchlist CTA */}
        <div className="flex items-end md:items-end justify-between md:justify-end gap-6">
          <div className="text-left md:text-right">
            <div className="text-3xl font-extrabold text-white tracking-tight">
              ₹{stock.current_price.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
            </div>
            <div className={`text-sm font-semibold flex items-center gap-1.5 md:justify-end mt-0.5 ${isPositive ? 'text-emerald-400' : 'text-rose-400'}`}>
              <span>{isPositive ? '+' : ''}₹{stock.change.toFixed(2)}</span>
              <span>({isPositive ? '+' : ''}{stock.change_percent.toFixed(2)}%)</span>
            </div>
            <div className="text-[11px] text-slate-500 mt-0.5">
              Prev Close: ₹{stock.previous_close.toFixed(2)}
            </div>
          </div>

          <button
            onClick={onToggleWatchlist}
            className={`p-3 rounded-2xl border transition-all flex items-center gap-2 text-xs font-semibold ${
              isWatchlisted
                ? 'bg-amber-500/20 text-amber-400 border-amber-500/50 shadow-lg shadow-amber-500/10'
                : 'bg-slate-800/80 text-slate-300 border-slate-700 hover:bg-slate-800 hover:text-white'
            }`}
            title={isWatchlisted ? 'Remove from Watchlist' : 'Save to Watchlist'}
          >
            {isWatchlisted ? (
              <>
                <BookmarkCheck className="w-5 h-5 text-amber-400" />
                <span className="hidden sm:inline">Saved</span>
              </>
            ) : (
              <>
                <Bookmark className="w-5 h-5 text-slate-400" />
                <span className="hidden sm:inline">Watchlist</span>
              </>
            )}
          </button>
        </div>
      </div>

      {/* 52-Week Range Bar */}
      <div className="mt-6 pt-5 border-t border-slate-800/80">
        <div className="flex justify-between items-center text-xs font-medium text-slate-400 mb-1.5">
          <span>52W Low: <strong className="text-slate-200">₹{low52?.toFixed(2)}</strong></span>
          <span className="text-[11px] uppercase tracking-wider font-semibold text-slate-500">52-Week Price Spectrum</span>
          <span>52W High: <strong className="text-slate-200">₹{high52?.toFixed(2)}</strong></span>
        </div>
        <div className="relative h-2.5 bg-slate-950 rounded-full border border-slate-800 overflow-hidden">
          <div
            className="absolute top-0 bottom-0 left-0 bg-gradient-to-r from-emerald-500 via-teal-400 to-indigo-500 rounded-full"
            style={{ width: `${positionPercent}%` }}
          />
        </div>
        <div className="flex justify-between text-[11px] text-slate-500 mt-1">
          <span>Oversold / Floor</span>
          <span className="text-slate-400 font-medium">Current: {positionPercent.toFixed(0)}% of 52W Range</span>
          <span>Momentum / Peak</span>
        </div>
      </div>
    </div>
  );
};
