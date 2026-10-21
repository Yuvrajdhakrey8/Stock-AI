import React, { useState } from 'react';
import {
  ArrowLeft,
  Bookmark,
  BookmarkCheck,
  Share2,
  Check,
  Sparkles,
  TrendingUp,
  TrendingDown,
  ShieldCheck,
  AlertTriangle,
  BarChart2,
  Layers,
  FileText,
  Activity,
} from 'lucide-react';
import type { StockAnalysisResponse } from '../types';
import { CompanyLogo } from './CompanyLogo';
import { ValuationMeter } from './ValuationMeter';
import { TechnicalChart } from './TechnicalChart';
import { FundamentalGrid } from './FundamentalGrid';

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
  const [activeSubTab, setActiveSubTab] = useState<'verdict' | 'chart' | 'fundamentals'>('verdict');
  const [copied, setCopied] = useState<boolean>(false);

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
    const shareText = `📊 *${stock.name} (${stock.display_symbol})* on Stocks Suggestions - Dhakrey:\n` +
      `• CMP: ₹${stock.current_price.toFixed(2)}\n` +
      `• Intrinsic Fair Value: ₹${fairVal.toFixed(2)}\n` +
      `• Verdict: *${verdict}* (Margin of Safety: ${mos > 0 ? '+' : ''}${mos.toFixed(1)}%)\n\n` +
      `Calculate DCF Intrinsic Value & Live IPOs on Stocks Suggestions - Dhakrey:`;
    const shareUrl = `https://main.d2x1z9kgh5o58m.amplifyapp.com/?stock=${encodeURIComponent(stock.symbol)}`;

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
    <div className="space-y-5 animate-in fade-in duration-300">
      {/* Top Navigation Row: Back to Explore & Quick Actions */}
      <div className="flex items-center justify-between gap-3 flex-wrap">
        <button
          onClick={onBack}
          className="inline-flex items-center gap-2 px-3.5 py-2 rounded-xl bg-slate-900 border border-slate-700/80 hover:bg-slate-800 text-slate-200 hover:text-white text-xs sm:text-sm font-semibold transition-all shadow-md active:scale-95 group cursor-pointer"
        >
          <ArrowLeft className="w-4 h-4 text-emerald-400 group-hover:-translate-x-1 transition-transform" />
          <span>Back to Explore</span>
        </button>

        <div className="flex items-center gap-2">
          {/* Share */}
          <button
            onClick={handleShare}
            className="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-slate-900 border border-slate-800 hover:bg-slate-800 text-slate-300 hover:text-white text-xs font-semibold transition-colors shadow-sm cursor-pointer"
            title="Share analysis"
          >
            {copied ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Share2 className="w-3.5 h-3.5" />}
            <span>{copied ? 'Copied' : 'Share'}</span>
          </button>

          {/* Watchlist */}
          <button
            onClick={onToggleWatchlist}
            className={`flex items-center gap-1.5 px-3 py-2 rounded-xl border text-xs font-semibold transition-all cursor-pointer ${
              isWatchlisted
                ? 'bg-amber-500/20 border-amber-500/50 text-amber-300'
                : 'bg-slate-900 border-slate-800 text-slate-300 hover:bg-slate-800 hover:text-white'
            }`}
          >
            {isWatchlisted ? (
              <BookmarkCheck className="w-3.5 h-3.5 text-amber-400" />
            ) : (
              <Bookmark className="w-3.5 h-3.5" />
            )}
            <span>{isWatchlisted ? 'Watchlisted' : 'Add Watchlist'}</span>
          </button>
        </div>
      </div>

      {/* Stock Main Header Card (Clean & Simple) */}
      <div className="bg-slate-900/95 border border-slate-800 rounded-2xl sm:rounded-3xl p-4 sm:p-5 shadow-xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          {/* Left: Logo & Company Name */}
          <div className="flex items-start gap-3.5">
            <CompanyLogo
              name={stock.name}
              symbol={stock.symbol}
              size="lg"
              className="mt-0.5 rounded-2xl shadow-lg border-slate-700/80 shrink-0"
            />
            <div className="min-w-0">
              <div className="flex items-center gap-2 flex-wrap">
                <h1 className="text-lg sm:text-2xl font-extrabold text-white tracking-tight">
                  {stock.name}
                </h1>
                <span className="px-2 py-0.2 rounded-lg text-[10px] sm:text-xs font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
                  {stock.exchange}
                </span>
                <span className="font-mono text-[10px] sm:text-xs text-slate-400 px-1.5 py-0.2 rounded bg-slate-800 border border-slate-700">
                  {stock.display_symbol}
                </span>
              </div>
              <div className="flex items-center gap-2 text-xs text-slate-400 mt-1">
                <span>{stock.sector}</span>
                <span>•</span>
                <span>M-Cap: <strong className="text-slate-200">{stock.market_cap_formatted}</strong></span>
              </div>
            </div>
          </div>

          {/* Right: Live Price & 1D Change */}
          <div className="text-left md:text-right pt-2 md:pt-0 border-t md:border-t-0 border-slate-800/80">
            <div className="text-2xl sm:text-3xl font-extrabold text-white">
              ₹{stock.current_price.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
            </div>
            <div className={`text-xs sm:text-sm font-bold flex items-center gap-1.5 md:justify-end mt-0.5 ${
              isPos ? 'text-emerald-400' : 'text-rose-400'
            }`}>
              <span>{isPos ? '+' : ''}₹{stock.change.toFixed(2)}</span>
              <span>({isPos ? '+' : ''}{stock.change_percent.toFixed(2)}%)</span>
            </div>
          </div>
        </div>

        {/* 52-Week Range Bar */}
        <div className="mt-4 pt-3 border-t border-slate-800/80">
          <div className="flex items-center justify-between text-[11px] text-slate-400 mb-1.5">
            <span>52W Low: <strong className="text-slate-200">₹{low52.toFixed(2)}</strong></span>
            <span className="text-slate-500">52-Week Range</span>
            <span>52W High: <strong className="text-slate-200">₹{high52.toFixed(2)}</strong></span>
          </div>
          <div className="relative w-full h-2 rounded-full bg-slate-800 overflow-hidden">
            <div
              className="absolute top-0 bottom-0 left-0 bg-gradient-to-r from-emerald-500 to-teal-400 rounded-full"
              style={{ width: `${positionPercent}%` }}
            />
          </div>
        </div>
      </div>

      {/* Simplified AI Suggestion & Verdict Banner */}
      <div className={`rounded-2xl sm:rounded-3xl p-4 sm:p-5 border shadow-xl ${
        valuation.verdict === 'BEST BUY'
          ? 'bg-emerald-950/30 border-emerald-500/40'
          : valuation.verdict === 'CURRENTLY EXPENSIVE'
          ? 'bg-rose-950/30 border-rose-500/40'
          : 'bg-amber-950/30 border-amber-500/40'
      }`}>
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="flex items-center gap-3">
            <div className={`w-10 h-10 rounded-2xl flex items-center justify-center shrink-0 ${
              valuation.verdict === 'BEST BUY'
                ? 'bg-emerald-500 text-slate-950 shadow-md shadow-emerald-500/30'
                : valuation.verdict === 'CURRENTLY EXPENSIVE'
                ? 'bg-rose-500 text-white shadow-md shadow-rose-500/30'
                : 'bg-amber-500 text-slate-950 shadow-md shadow-amber-500/30'
            }`}>
              <Sparkles className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-xs font-bold uppercase tracking-wider text-slate-400">
                  AI Valuation Suggestion
                </span>
                <span className={`px-2 py-0.5 rounded-full text-xs font-black uppercase ${
                  valuation.verdict === 'BEST BUY'
                    ? 'bg-emerald-500 text-slate-950'
                    : valuation.verdict === 'CURRENTLY EXPENSIVE'
                    ? 'bg-rose-500 text-white'
                    : 'bg-amber-500 text-slate-950'
                }`}>
                  {valuation.verdict}
                </span>
              </div>
              <p className="text-sm font-semibold text-white mt-0.5">
                {valuation.action_call}
              </p>
            </div>
          </div>

          {/* Target Fair Value & Margin */}
          <div className="flex items-center gap-4 self-end sm:self-auto text-right">
            <div>
              <span className="text-[10px] text-slate-400 block uppercase font-bold">Intrinsic Value</span>
              <span className="text-sm sm:text-base font-extrabold text-white">
                ₹{valuation.fair_value.toLocaleString('en-IN', { maximumFractionDigits: 0 })}
              </span>
            </div>
            <div className="pl-3 border-l border-slate-800">
              <span className="text-[10px] text-slate-400 block uppercase font-bold">Margin of Safety</span>
              <span className={`text-sm sm:text-base font-black ${isMoSPos ? 'text-emerald-400' : 'text-rose-400'}`}>
                {isMoSPos ? '+' : ''}{mos.toFixed(1)}%
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* Clean Analytical Sub-Tabs (Prevents overwhelming data bombardment) */}
      <div className="flex items-center gap-2 bg-slate-900/95 p-1 rounded-2xl border border-slate-800 overflow-x-auto scrollbar-none text-xs">
        <button
          onClick={() => setActiveSubTab('verdict')}
          className={`flex-1 py-2.5 px-3 rounded-xl font-bold transition-all text-center flex items-center justify-center gap-1.5 cursor-pointer shrink-0 ${
            activeSubTab === 'verdict'
              ? 'bg-emerald-500 text-slate-950 shadow-md font-extrabold'
              : 'text-slate-300 hover:text-white'
          }`}
        >
          <Sparkles className="w-3.5 h-3.5" />
          <span>Overview & AI Verdict</span>
        </button>

        <button
          onClick={() => setActiveSubTab('chart')}
          className={`flex-1 py-2.5 px-3 rounded-xl font-bold transition-all text-center flex items-center justify-center gap-1.5 cursor-pointer shrink-0 ${
            activeSubTab === 'chart'
              ? 'bg-emerald-500 text-slate-950 shadow-md font-extrabold'
              : 'text-slate-300 hover:text-white'
          }`}
        >
          <BarChart2 className="w-3.5 h-3.5" />
          <span>Price Chart & Technicals</span>
        </button>

        <button
          onClick={() => setActiveSubTab('fundamentals')}
          className={`flex-1 py-2.5 px-3 rounded-xl font-bold transition-all text-center flex items-center justify-center gap-1.5 cursor-pointer shrink-0 ${
            activeSubTab === 'fundamentals'
              ? 'bg-emerald-500 text-slate-950 shadow-md font-extrabold'
              : 'text-slate-300 hover:text-white'
          }`}
        >
          <FileText className="w-3.5 h-3.5" />
          <span>Financials & DCF Model</span>
        </button>
      </div>

      {/* Sub-Tab 1: Simple Overview & AI Verdict */}
      {activeSubTab === 'verdict' && (
        <div className="space-y-5 animate-in fade-in duration-200">
          <ValuationMeter
            valuation={stock.valuation}
            currency={stock.currency}
          />
        </div>
      )}

      {/* Sub-Tab 2: Technical Chart */}
      {activeSubTab === 'chart' && (
        <div className="space-y-5 animate-in fade-in duration-200">
          <TechnicalChart
            chartData={stock.chart}
            valuation={stock.valuation}
            currentPrice={stock.current_price}
          />
        </div>
      )}

      {/* Sub-Tab 3: Fundamental Grid */}
      {activeSubTab === 'fundamentals' && (
        <div className="space-y-5 animate-in fade-in duration-200">
          <FundamentalGrid stock={stock} />
        </div>
      )}
    </div>
  );
};
