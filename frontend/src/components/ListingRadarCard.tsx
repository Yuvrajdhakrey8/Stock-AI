import React, { useState } from 'react';
import {
  ChevronDown,
  ChevronUp,
  Info,
  X,
  TrendingUp,
  TrendingDown,
  ArrowRight,
} from 'lucide-react';
import type { ListingRadarData, ListingRadarPrediction } from '../types';

interface ListingRadarCardProps {
  radarData: ListingRadarData | null;
  onSelectIPO?: (id: string) => void;
}

export const ListingRadarCard: React.FC<ListingRadarCardProps> = ({ radarData }) => {
  const [selectedIndex, setSelectedIndex] = useState<number>(0);
  const [isExpanded, setIsExpanded] = useState<boolean>(false);
  const [showBrokerGuide, setShowBrokerGuide] = useState<boolean>(false);

  if (!radarData || !radarData.predictions || radarData.predictions.length === 0) {
    return null;
  }

  const prediction: ListingRadarPrediction = radarData.predictions[selectedIndex] || radarData.predictions[0];
  const isProfit = prediction.expected_gain_percent >= 0;

  // Derive explicit action recommendation
  const actionTitle = prediction.action_title || (
    prediction.expected_gain_percent >= 25
      ? 'SELL (Book Profit in Pre-Open: 9:00 - 9:45 AM)'
      : prediction.expected_gain_percent >= 8
      ? 'PARTIAL SELL (Sell 50%, Keep Stop-Loss at Issue Price)'
      : 'EXIT / CAPITAL PROTECTION (Sell in Pre-Open)'
  );

  const actionSummary = prediction.action_summary || prediction.retail_sell_playbook.action_guide;

  return (
    <div className="bg-slate-900/40 border border-slate-800 rounded-2xl overflow-hidden text-left transition-all">
      {/* Compact Top Header Bar */}
      <div
        onClick={() => setIsExpanded(!isExpanded)}
        className="p-3.5 sm:p-4 flex items-center justify-between gap-3 cursor-pointer hover:bg-slate-850/50 transition-colors"
      >
        <div className="flex items-center gap-2.5 min-w-0">
          <span className="w-2 h-2 rounded-full bg-emerald-400/80 shrink-0" />
          <div className="min-w-0">
            <div className="flex items-center gap-2 flex-wrap">
              <span className="text-xs sm:text-sm font-semibold text-white truncate">
                Listing Radar: <span className="text-slate-100 font-bold">{prediction.name}</span>
              </span>
              <span className="text-[10px] px-2 py-0.5 rounded font-medium bg-slate-800 text-slate-300">
                {prediction.listing_date === 'Today' ? 'Listing Today' : `Listing on ${prediction.listing_date}`}
              </span>
            </div>
            <p className="text-[11px] text-slate-400 truncate mt-0.5">
              Est. Open: ₹{prediction.predicted_open_price} ({isProfit ? '+' : ''}{prediction.expected_gain_percent.toFixed(0)}%) • Est. Profit: ₹{prediction.expected_profit_per_lot.toLocaleString('en-IN')}/lot
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2 shrink-0">
          <span className="text-xs text-slate-400 font-medium hidden sm:inline">
            {isExpanded ? 'Hide Details' : 'View Action Plan'}
          </span>
          <div className="p-1 rounded-md text-slate-400 bg-slate-800">
            {isExpanded ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
          </div>
        </div>
      </div>

      {/* Expanded Strategy Card */}
      {isExpanded && (
        <div className="p-4 sm:p-5 border-t border-slate-800 space-y-4 animate-in fade-in duration-150">
          {/* Multiple Candidates Tab (only if >1 IPO is listing) */}
          {radarData.predictions.length > 1 && (
            <div className="flex items-center gap-2 overflow-x-auto scrollbar-none pb-1">
              {radarData.predictions.map((p, idx) => (
                <button
                  key={p.id}
                  onClick={(e) => {
                    e.stopPropagation();
                    setSelectedIndex(idx);
                  }}
                  className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all shrink-0 cursor-pointer ${
                    selectedIndex === idx
                      ? 'bg-slate-700 text-white font-semibold'
                      : 'bg-slate-800/60 hover:bg-slate-800 text-slate-400'
                  }`}
                >
                  <span>{p.name}</span>
                  <span className="ml-1 text-slate-300">+{p.expected_gain_percent.toFixed(0)}%</span>
                </button>
              ))}
            </div>
          )}

          {/* 1. Primary Action Box (Direct & Unambiguous: SELL vs HOLD) */}
          <div className="bg-slate-950/60 border border-slate-800 rounded-xl p-3.5 sm:p-4 space-y-2">
            <div className="flex items-center justify-between gap-2 flex-wrap">
              <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">
                Recommended Action
              </span>
              <button
                onClick={() => setShowBrokerGuide(true)}
                className="text-[11px] text-slate-400 hover:text-slate-200 inline-flex items-center gap-1 underline underline-offset-2 transition-colors cursor-pointer"
              >
                <Info className="w-3 h-3" />
                <span>How to place order in Zerodha/Groww?</span>
              </button>
            </div>

            <div className="flex items-center gap-2">
              <span className={`text-xs sm:text-sm font-bold px-2.5 py-1 rounded-lg ${
                prediction.expected_gain_percent >= 25
                  ? 'bg-emerald-500/15 text-emerald-300 border border-emerald-500/30'
                  : prediction.expected_gain_percent >= 8
                  ? 'bg-amber-500/15 text-amber-300 border border-amber-500/30'
                  : 'bg-rose-500/15 text-rose-300 border border-rose-500/30'
              }`}>
                {actionTitle}
              </span>
            </div>

            <p className="text-xs text-slate-300 leading-relaxed pt-1">
              {actionSummary}
            </p>
          </div>

          {/* 2. Numerical Breakdown (Subtle 3-Stat Row) */}
          <div className="grid grid-cols-3 gap-2 text-center">
            <div className="bg-slate-950/40 p-2.5 rounded-lg border border-slate-800/80">
              <span className="text-[10px] text-slate-400 block">Issue Price</span>
              <span className="text-sm font-semibold text-white mt-0.5 block">₹{prediction.issue_price}</span>
            </div>
            <div className="bg-slate-950/40 p-2.5 rounded-lg border border-slate-800/80">
              <span className="text-[10px] text-slate-400 block">Predicted Open</span>
              <span className="text-sm font-bold text-white mt-0.5 block">₹{prediction.predicted_open_price}</span>
              <span className="text-[9px] text-slate-500">Range: ₹{prediction.predicted_range.min} - ₹{prediction.predicted_range.max}</span>
            </div>
            <div className="bg-slate-950/40 p-2.5 rounded-lg border border-slate-800/80">
              <span className="text-[10px] text-slate-400 block">Est. Profit / Lot</span>
              <span className="text-sm font-bold text-emerald-300 mt-0.5 block">
                +₹{prediction.expected_profit_per_lot.toLocaleString('en-IN')}
              </span>
            </div>
          </div>
        </div>
      )}

      {/* Broker Placement Modal Popup (Clean on-demand popup instead of fixed clutter) */}
      {showBrokerGuide && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/70 backdrop-blur-sm animate-in fade-in duration-150">
          <div className="bg-slate-900 border border-slate-800 rounded-2xl max-w-md w-full p-5 space-y-4 shadow-2xl">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div className="flex items-center gap-2">
                <Info className="w-4 h-4 text-slate-300" />
                <h4 className="text-sm font-bold text-white">How to Place Pre-Open Sell Order</h4>
              </div>
              <button
                onClick={() => setShowBrokerGuide(false)}
                className="p-1 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors cursor-pointer"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <div className="space-y-3 text-xs text-slate-300 leading-relaxed">
              <p>
                IPO listing day begins with a special <strong>Call Auction Pre-Open Session (9:00 AM – 9:45 AM IST)</strong> before normal 10:00 AM trading starts.
              </p>

              <div className="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-1.5">
                <span className="text-[11px] font-semibold text-slate-200 block">Step-by-Step (Zerodha / Groww / AngelOne):</span>
                <ol className="list-decimal list-inside space-y-1 text-slate-400">
                  <li>Go to <strong>Portfolio / Orders</strong> $\rightarrow$ Select your allotted IPO stock.</li>
                  <li>Tap <strong>Sell</strong> between <strong>9:00 AM and 9:45 AM</strong>.</li>
                  <li>Select Order Type: <strong>Limit Order</strong> at Issue Price (or Market).</li>
                  <li>Submit. Your order will be matched at the discovered equilibrium opening price at 9:45 AM.</li>
                </ol>
              </div>

              <p className="text-[11px] text-slate-500">
                Note: Orders cannot be cancelled or modified between 9:45 AM and 10:00 AM (Order matching phase).
              </p>
            </div>

            <button
              onClick={() => setShowBrokerGuide(false)}
              className="w-full py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-semibold text-xs transition-colors cursor-pointer"
            >
              Got it
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
