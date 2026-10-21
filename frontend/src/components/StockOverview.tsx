import React, { useState } from 'react';
import { Bookmark, BookmarkCheck, ExternalLink, Activity, BarChart2, Share2, Check } from 'lucide-react';
import type { StockAnalysisResponse } from '../types';
import { CompanyLogo } from './CompanyLogo';

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
  
  const [copied, setCopied] = useState<boolean>(false);

  // Calculate percentage within 52w range
  const rangeSpan = high52 - low52;
  const positionPercent = rangeSpan > 0 
    ? Math.min(Math.max(((stock.current_price - low52) / rangeSpan) * 100, 0), 100) 
    : 50;

  const handleShare = async () => {
    const verdict = stock.valuation?.verdict || 'ANALYZE';
    const mos = stock.valuation?.margin_of_safety_percent ?? 0;
    const fairVal = stock.valuation?.dcf_intrinsic_value ?? stock.valuation?.graham_number ?? stock.current_price;

    const shareText = `📊 *${stock.name} (${stock.display_symbol})* on Stocks Suggestions - Dhakrey:\n` +
      `• CMP: ₹${stock.current_price.toFixed(2)}\n` +
      `• Intrinsic Fair Value: ₹${fairVal.toFixed(2)}\n` +
      `• Verdict: *${verdict}* (Margin of Safety: ${mos > 0 ? '+' : ''}${mos.toFixed(1)}%)\n\n` +
      `Calculate DCF Intrinsic Value & Live IPOs on Stocks Suggestions - Dhakrey:`;
    
    const shareUrl = `https://main.d2x1z9kgh5o58m.amplifyapp.com/?stock=${encodeURIComponent(stock.symbol)}`;

    if (navigator.share) {
      try {
        await navigator.share({
          title: `${stock.name} - Stocks Suggestions - Dhakrey Valuation`,
          text: shareText,
          url: shareUrl,
        });
      } catch {
        // User cancelled share dialog
      }
    } else {
      try {
        await navigator.clipboard.writeText(`${shareText}\n${shareUrl}`);
        setCopied(true);
        setTimeout(() => setCopied(false), 2500);
      } catch {
        // Fallback
      }
    }
  };

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl sm:rounded-3xl p-4 sm:p-6 shadow-xl">
      <div className="flex flex-col md:flex-row md:items-start justify-between gap-4">
        {/* Company Title & Exchange Info */}
        <div className="flex items-start gap-3 sm:gap-4">
          <CompanyLogo
            name={stock.name}
            symbol={stock.symbol}
            size="lg"
            className="mt-1 rounded-2xl shadow-lg border-slate-700/80 shrink-0"
          />
          <div>
            <div className="flex items-center gap-2 flex-wrap">
              <h1 className="text-xl sm:text-2xl md:text-3xl font-extrabold text-white tracking-tight">
                {stock.name}
              </h1>
              <span className="px-2 py-0.5 rounded-lg text-[10px] sm:text-xs font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
                {stock.exchange}
              </span>
              <span className="font-mono text-[10px] sm:text-xs font-semibold text-slate-400 px-1.5 sm:px-2 py-0.5 rounded bg-slate-800 border border-slate-700">
                {stock.symbol}
              </span>
            </div>

            <div className="flex items-center gap-1.5 sm:gap-2 mt-2 text-[11px] sm:text-xs text-slate-400 flex-wrap">
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
        </div>

        {/* Live Price & Watchlist CTA */}
        <div className="flex items-end justify-between md:justify-end gap-4 sm:gap-6 pt-1 md:pt-0 border-t md:border-t-0 border-slate-800/60">
          <div className="text-left md:text-right">
            <div className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
              ₹{stock.current_price.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
            </div>
            <div className={`text-xs sm:text-sm font-semibold flex items-center gap-1.5 md:justify-end mt-0.5 ${isPositive ? 'text-emerald-400' : 'text-rose-400'}`}>
              <span>{isPositive ? '+' : ''}₹{stock.change.toFixed(2)}</span>
              <span>({isPositive ? '+' : ''}{stock.change_percent.toFixed(2)}%)</span>
            </div>
            <div className="text-[10px] sm:text-[11px] text-slate-500 mt-0.5">
              Prev Close: ₹{stock.previous_close.toFixed(2)}
            </div>
          </div>

          {/* Action CTAs: Share & Watchlist */}
          <div className="flex items-center gap-2 shrink-0">
            <button
              onClick={handleShare}
              className={`p-2.5 sm:p-3 rounded-2xl border transition-all flex items-center gap-1.5 sm:gap-2 text-xs font-semibold shrink-0 active:scale-95 ${
                copied
                  ? 'bg-emerald-500/20 text-emerald-400 border-emerald-500/50 shadow-lg shadow-emerald-500/10'
                  : 'bg-slate-800/80 text-slate-300 border-slate-700 hover:bg-slate-800 hover:text-white'
              }`}
              title="Share stock valuation analysis"
            >
              {copied ? (
                <>
                  <Check className="w-4 h-4 sm:w-5 sm:h-5 text-emerald-400" />
                  <span className="inline">Copied!</span>
                </>
              ) : (
                <>
                  <Share2 className="w-4 h-4 sm:w-5 sm:h-5 text-slate-400" />
                  <span className="hidden xs:inline sm:inline">Share</span>
                </>
              )}
            </button>

            <button
              onClick={onToggleWatchlist}
              className={`p-2.5 sm:p-3 rounded-2xl border transition-all flex items-center gap-1.5 sm:gap-2 text-xs font-semibold shrink-0 active:scale-95 ${
                isWatchlisted
                  ? 'bg-amber-500/20 text-amber-400 border-amber-500/50 shadow-lg shadow-amber-500/10'
                  : 'bg-slate-800/80 text-slate-300 border-slate-700 hover:bg-slate-800 hover:text-white'
              }`}
              title={isWatchlisted ? 'Remove from Watchlist' : 'Save to Watchlist'}
            >
              {isWatchlisted ? (
                <>
                  <BookmarkCheck className="w-4 h-4 sm:w-5 sm:h-5 text-amber-400" />
                  <span className="inline">Saved</span>
                </>
              ) : (
                <>
                  <Bookmark className="w-4 h-4 sm:w-5 sm:h-5 text-slate-400" />
                  <span className="inline">Watchlist</span>
                </>
              )}
            </button>
          </div>
        </div>
      </div>

      {/* 52-Week Range Bar */}
      <div className="mt-5 sm:mt-6 pt-4 sm:pt-5 border-t border-slate-800/80">
        <div className="flex justify-between items-center text-[10px] sm:text-xs font-medium text-slate-400 mb-1.5">
          <span>52W Low: <strong className="text-slate-200">₹{low52?.toFixed(2)}</strong></span>
          <span className="text-[10px] uppercase tracking-wider font-semibold text-slate-500 hidden sm:inline">52-Week Price Spectrum</span>
          <span>52W High: <strong className="text-slate-200">₹{high52?.toFixed(2)}</strong></span>
        </div>
        <div className="relative h-2 sm:h-2.5 bg-slate-950 rounded-full border border-slate-800 overflow-hidden">
          <div
            className="absolute top-0 bottom-0 left-0 bg-gradient-to-r from-emerald-500 via-teal-400 to-indigo-500 rounded-full"
            style={{ width: `${positionPercent}%` }}
          />
        </div>
        <div className="flex justify-between text-[10px] sm:text-[11px] text-slate-500 mt-1">
          <span>Floor</span>
          <span className="text-slate-400 font-medium">Current: {positionPercent.toFixed(0)}% of 52W</span>
          <span>Peak</span>
        </div>
      </div>
    </div>
  );
};
