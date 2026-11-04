import React, { useState } from 'react';
import {
  ArrowLeft,
  Bookmark,
  BookmarkCheck,
  Share2,
  Check,
  ChevronDown,
  ChevronUp,
  Sparkles,
  ShieldCheck,
  TrendingUp,
  TrendingDown,
  Info,
} from 'lucide-react';
import type { StockAnalysisResponse } from '../types';
import { CompanyLogo } from './CompanyLogo';
import { TechnicalChart } from './TechnicalChart';
import { FundamentalGrid } from './FundamentalGrid';
import { ValuationMeter } from './ValuationMeter';

interface StockDetailViewProps {
  stock: StockAnalysisResponse;
  onBack: () => void;
  isWatchlisted: boolean;
  onToggleWatchlist: () => void;
}

export const StockDetailView: React.FC<StockDetailViewProps> = ({
  stock,
  onBack,
  isWatchlisted,
  onToggleWatchlist,
}) => {
  const [copied, setCopied] = useState<boolean>(false);
  const [showValuationInsights, setShowValuationInsights] = useState<boolean>(false);

  const isPos = stock.change >= 0;
  const valuation = stock.valuation;
  const mos = valuation.margin_of_safety_percent;
  const isMoSPos = mos > 0;
  const low52 = stock.low_52 ?? stock.current_price * 0.8;
  const high52 = stock.high_52 ?? stock.current_price * 1.2;
  const rangeSpan = high52 - low52;
  const positionPercent = rangeSpan > 0
    ? Math.min(Math.max(((stock.current_price - low52) / rangeSpan) * 100, 0), 100)
    : 50;

  const handleShare = async () => {
    const verdict = valuation.verdict;
    const fairVal = valuation.dcf_intrinsic_value ?? valuation.graham_number ?? stock.current_price;
    const shareText = `📊 *${stock.name} (${stock.display_symbol})* on Dhakrey Stocks:\n` +
      `• CMP: ₹${stock.current_price.toFixed(2)}\n` +
      `• Fair Value: ₹${fairVal.toFixed(2)}\n` +
      `• Verdict: ${verdict} (${mos > 0 ? '+' : ''}${mos.toFixed(1)}%)\n\n` +
      `Explore DCF Fair Value & Live IPOs:`;
    const shareUrl = `https://main.dtvi3uv6gm2u7.amplifyapp.com/?stock=${encodeURIComponent(stock.symbol)}`;

    if (navigator.share) {
      try {
        await navigator.share({
          title: `${stock.name} - Valuation`,
          text: shareText,
          url: shareUrl,
        });
      } catch {
        // User cancelled share
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
    <div className="space-y-4 sm:space-y-5 animate-in fade-in duration-200">
      {/* Top Navigation Row: Back to Explore & Quick Actions */}
      <div className="flex items-center justify-between gap-3 flex-wrap">
        <button
          onClick={onBack}
          className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 hover:bg-slate-800 text-slate-300 hover:text-white text-xs font-semibold transition-all cursor-pointer"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>Back</span>
        </button>

        <div className="flex items-center gap-2">
          {/* Share */}
          <button
            onClick={handleShare}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 hover:bg-slate-800 text-slate-300 hover:text-white text-xs font-medium transition-colors cursor-pointer"
            title="Share analysis"
          >
            {copied ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Share2 className="w-3.5 h-3.5" />}
            <span>{copied ? 'Copied' : 'Share'}</span>
          </button>

          {/* Watchlist */}
          <button
            onClick={onToggleWatchlist}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl border text-xs font-medium transition-all cursor-pointer ${
              isWatchlisted
                ? 'bg-amber-500/15 border-amber-500/40 text-amber-300'
                : 'bg-slate-900 border-slate-800 text-slate-300 hover:bg-slate-800 hover:text-white'
            }`}
          >
            {isWatchlisted ? (
              <BookmarkCheck className="w-3.5 h-3.5 text-amber-400" />
            ) : (
              <Bookmark className="w-3.5 h-3.5" />
            )}
            <span>{isWatchlisted ? 'Watchlisted' : 'Watchlist'}</span>
          </button>
        </div>
      </div>

      {/* Primary Stock Header: Clean, Typography-Driven (Groww Reference) */}
      <div className="bg-slate-900/40 border border-slate-800 rounded-2xl p-4 sm:p-5">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          {/* Left: Logo & Company Name */}
          <div className="flex items-start gap-3">
            <CompanyLogo
              name={stock.name}
              symbol={stock.symbol}
              size="lg"
              className="rounded-xl border border-slate-800 shrink-0"
            />
            <div className="min-w-0">
              <div className="flex items-center gap-2 flex-wrap">
                <h1 className="text-lg sm:text-2xl font-bold text-white tracking-tight">
                  {stock.name}
                </h1>
                <span className="text-[11px] font-medium text-slate-400">
                  {stock.exchange} • {stock.display_symbol}
                </span>
              </div>
              <div className="text-xs text-slate-400 mt-0.5">
                <span>{stock.sector}</span>
              </div>
            </div>
          </div>

          {/* Right: Live Price & 1D Change */}
          <div className="text-left md:text-right pt-2 md:pt-0 border-t md:border-t-0 border-slate-800/60">
            <div className="text-2xl sm:text-3xl font-bold text-white tracking-tight">
              ₹{stock.current_price.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
            </div>
            <div className={`text-xs sm:text-sm font-semibold flex items-center gap-1.5 md:justify-end mt-0.5 ${
              isPos ? 'text-emerald-400' : 'text-rose-400'
            }`}>
              <span>{isPos ? '+' : ''}₹{stock.change.toFixed(2)}</span>
              <span>({isPos ? '+' : ''}{stock.change_percent.toFixed(2)}%)</span>
              <span className="text-slate-500 text-[11px] font-normal">• 1D</span>
            </div>
          </div>
        </div>

        {/* Section 1 Valuation Verdict: Direct & Clean */}
        <div className="mt-3.5 pt-3 border-t border-slate-800/80 flex items-center justify-between gap-3 flex-wrap">
          <div className="flex items-center gap-2">
            <span className="text-xs text-slate-400 font-medium">Valuation Verdict:</span>
            <span className={`text-xs font-bold px-2.5 py-0.5 rounded-md ${
              valuation.verdict === 'BEST BUY'
                ? 'bg-[#f0fdf4] text-[#047857] border border-[#d1fae5]'
                : valuation.verdict === 'CURRENTLY EXPENSIVE'
                ? 'bg-[#fff1f3] text-[#be123c] border border-[#fecdd3]'
                : 'bg-[#fff8eb] text-[#b45309] border border-[#fef3c7]'
            }`}>
              {valuation.verdict}
            </span>
          </div>

          <div className="text-xs text-slate-300">
            Fair Value: <strong className="text-white">₹{valuation.fair_value.toFixed(1)}</strong>
            <span className="ml-1 text-slate-400">({isMoSPos ? '+' : ''}{mos.toFixed(1)}% Margin)</span>
          </div>
        </div>

        {/* 52-Week Range Slider (Subtle & Quiet) */}
        <div className="mt-4 pt-3.5 border-t border-slate-800/80">
          <div className="flex items-center justify-between text-[11px] text-slate-400 mb-1.5">
            <span>52W Low: <strong className="text-slate-200 font-medium">₹{low52.toFixed(1)}</strong></span>
            <span className="text-slate-500 font-medium">52-Week Range</span>
            <span>52W High: <strong className="text-slate-200 font-medium">₹{high52.toFixed(1)}</strong></span>
          </div>
          <div className="relative w-full h-1.5 rounded-full bg-slate-800 overflow-hidden">
            <div
              className="absolute top-0 bottom-0 left-0 bg-slate-400 rounded-full"
              style={{ width: `${positionPercent}%` }}
            />
          </div>
        </div>
      </div>

      {/* 1. Primary Focus: Interactive Price & Technical Chart */}
      <TechnicalChart
        chartData={stock.chart}
        valuation={stock.valuation}
        currentPrice={stock.current_price}
      />

      {/* 2. Secondary Focus: Clean Fundamentals (Direct Groww Reference) */}
      <FundamentalGrid stock={stock} />

      {/* 3. OPTIONAL Valuation Insights & Recommendations (Collapsed by Default) */}
      <div className="bg-slate-900/40 border border-slate-800 rounded-2xl overflow-hidden transition-all">
        <button
          onClick={() => setShowValuationInsights(!showValuationInsights)}
          className="w-full p-4 sm:p-5 flex items-center justify-between gap-3 text-left hover:bg-slate-850/50 transition-colors cursor-pointer"
        >
          <div className="flex items-center gap-2.5 min-w-0">
            <ShieldCheck className="w-4 h-4 text-slate-400 shrink-0" />
            <div className="min-w-0">
              <span className="text-xs sm:text-sm font-semibold text-white block truncate">
                Valuation Analysis & DCF Insights
              </span>
              <span className="text-[11px] text-slate-400 block truncate">
                Intrinsic value estimate: ₹{valuation.fair_value.toFixed(1)} ({isMoSPos ? '+' : ''}{mos.toFixed(1)}% margin)
              </span>
            </div>
          </div>

          <div className="flex items-center gap-2.5 shrink-0">
            <span className={`text-[11px] font-bold px-2 py-0.5 rounded-md ${
              valuation.verdict === 'BEST BUY'
                ? 'bg-[#f0fdf4] text-[#047857] border border-[#d1fae5]'
                : valuation.verdict === 'CURRENTLY EXPENSIVE'
                ? 'bg-[#fff1f3] text-[#be123c] border border-[#fecdd3]'
                : 'bg-[#fff8eb] text-[#b45309] border border-[#fef3c7]'
            }`}>
              {valuation.verdict}
            </span>
            <div className="p-1 rounded-md text-slate-400 hover:text-white bg-slate-800">
              {showValuationInsights ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
            </div>
          </div>
        </button>

        {/* Expanded View of Valuation Meter */}
        {showValuationInsights && (
          <div className="p-4 sm:p-6 border-t border-slate-800 animate-in fade-in duration-200">
            <ValuationMeter
              valuation={stock.valuation}
              currency={stock.currency}
            />
          </div>
        )}
      </div>
    </div>
  );
};
