import React, { useState } from 'react';
import {
  Clock,
  ChevronDown,
  ChevronUp,
  Flame,
  CheckCircle2,
  Compass,
  ShieldCheck,
} from 'lucide-react';
import type { ListingRadarData, ListingRadarPrediction } from '../types';
import { CompanyLogo } from './CompanyLogo';

interface ListingRadarCardProps {
  radarData: ListingRadarData | null;
  onSelectIPO?: (id: string) => void;
}

export const ListingRadarCard: React.FC<ListingRadarCardProps> = ({ radarData, onSelectIPO }) => {
  const [selectedIndex, setSelectedIndex] = useState<number>(0);
  const [activeStrategyTab, setActiveStrategyTab] = useState<'sell' | 'hold'>('sell');
  // Optional by default: Start collapsed as per minimal data-first principle
  const [isExpanded, setIsExpanded] = useState<boolean>(false);

  if (!radarData || !radarData.predictions || radarData.predictions.length === 0) {
    return null;
  }

  const prediction: ListingRadarPrediction = radarData.predictions[selectedIndex] || radarData.predictions[0];
  const isProfit = prediction.expected_gain_percent >= 0;

  const stageBadgeConfig = {
    pre_market_early: {
      label: '7:00 AM – 9:00 AM • Pre-Market',
      pill: 'bg-slate-800 text-slate-300',
    },
    pre_open_auction: {
      label: '9:00 AM – 9:45 AM • Call Auction Live',
      pill: 'bg-emerald-500/15 text-emerald-400 border border-emerald-500/30',
    },
    order_matching: {
      label: '9:45 AM – 10:00 AM • Matching Buffer',
      pill: 'bg-amber-500/15 text-amber-400 border border-amber-500/30',
    },
    trading_active: {
      label: '10:00 AM+ • Trading Active',
      pill: 'bg-slate-800 text-slate-300',
    },
  }[radarData.session_stage] || {
    label: 'Listing Day Radar',
    pill: 'bg-slate-800 text-slate-300',
  };

  return (
    <div className="bg-slate-900/40 border border-slate-800 rounded-2xl overflow-hidden text-left transition-all">
      {/* Compact Header Bar (Always visible, non-intrusive) */}
      <div
        onClick={() => setIsExpanded(!isExpanded)}
        className="p-3.5 sm:p-4 flex items-center justify-between gap-3 cursor-pointer hover:bg-slate-850/50 transition-colors"
      >
        <div className="flex items-center gap-2.5 min-w-0">
          <div className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse shrink-0" />
          <div className="min-w-0">
            <div className="flex items-center gap-2 flex-wrap">
              <span className="text-xs sm:text-sm font-semibold text-white truncate">
                Listing Day Radar: <strong className="text-emerald-400">{prediction.name}</strong>
              </span>
              <span className={`text-[10px] px-2 py-0.5 rounded font-medium ${stageBadgeConfig.pill}`}>
                {stageBadgeConfig.label}
              </span>
            </div>
            <p className="text-[11px] text-slate-400 truncate mt-0.5">
              Est. Open: ₹{prediction.predicted_open_price} ({isProfit ? '+' : ''}{prediction.expected_gain_percent.toFixed(0)}%) • Est. Profit: ₹{prediction.expected_profit_per_lot.toLocaleString('en-IN')}/lot
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2 shrink-0">
          <span className="text-xs text-slate-400 font-medium hidden sm:inline">
            {isExpanded ? 'Hide Strategy' : 'View Pre-Market Strategy'}
          </span>
          <div className="p-1 rounded-md text-slate-400 bg-slate-800">
            {isExpanded ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
          </div>
        </div>
      </div>

      {/* Expanded Content (Only shown when user clicks to view) */}
      {isExpanded && (
        <div className="p-4 sm:p-5 border-t border-slate-800 space-y-4 animate-in fade-in duration-150">
          {/* Multiple Candidates Tab (if > 1 IPO is listing today) */}
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
                  <span className="ml-1 text-emerald-400">+{p.expected_gain_percent.toFixed(0)}%</span>
                </button>
              ))}
            </div>
          )}

          {/* Clean 2-Column Data & Strategy Grid */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
            {/* Left: Price Discovery Numbers */}
            <div className="bg-slate-950/50 border border-slate-800 rounded-xl p-4 space-y-3">
              <div className="flex items-center justify-between pb-2 border-b border-slate-800/80">
                <span className="text-xs font-semibold text-slate-300">
                  Price Discovery Model
                </span>
                <span className="text-[11px] text-slate-500">Target 10:00 AM Open</span>
              </div>

              <div className="grid grid-cols-3 gap-2 text-center">
                <div className="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                  <span className="text-[10px] text-slate-400 block">Issue Price</span>
                  <span className="text-sm font-semibold text-white mt-0.5 block">₹{prediction.issue_price}</span>
                </div>
                <div className="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                  <span className="text-[10px] text-slate-400 block">Predicted Open</span>
                  <span className="text-sm font-bold text-white mt-0.5 block">₹{prediction.predicted_open_price}</span>
                  <span className="text-[9px] text-slate-500">₹{prediction.predicted_range.min} - ₹{prediction.predicted_range.max}</span>
                </div>
                <div className="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                  <span className="text-[10px] text-slate-400 block">Est. Profit / Lot</span>
                  <span className="text-sm font-bold text-emerald-400 mt-0.5 block">
                    +₹{prediction.expected_profit_per_lot.toLocaleString('en-IN')}
                  </span>
                </div>
              </div>

              <div className="text-xs text-slate-400 pt-1 flex items-center justify-between">
                <span className="flex items-center gap-1.5">
                  <Flame className="w-3.5 h-3.5 text-amber-400" />
                  <span>Bidding Demand:</span>
                </span>
                <span className="text-slate-200 font-medium">{prediction.bidding_pressure}</span>
              </div>
            </div>

            {/* Right: Exit Playbook (Sell vs Hold) */}
            <div className="bg-slate-950/50 border border-slate-800 rounded-xl p-4 flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between mb-2.5 pb-2 border-b border-slate-800/80">
                  <span className="text-xs font-semibold text-slate-300 flex items-center gap-1.5">
                    <Compass className="w-3.5 h-3.5 text-slate-400" />
                    <span>Retail Exit Playbook</span>
                  </span>

                  <div className="flex items-center bg-slate-900 p-0.5 rounded-lg border border-slate-800 text-[11px]">
                    <button
                      onClick={() => setActiveStrategyTab('sell')}
                      className={`px-2.5 py-0.5 rounded font-medium cursor-pointer ${
                        activeStrategyTab === 'sell'
                          ? 'bg-slate-700 text-white font-semibold'
                          : 'text-slate-400'
                      }`}
                    >
                      Sell (10 AM)
                    </button>
                    <button
                      onClick={() => setActiveStrategyTab('hold')}
                      className={`px-2.5 py-0.5 rounded font-medium cursor-pointer ${
                        activeStrategyTab === 'hold'
                          ? 'bg-slate-700 text-white font-semibold'
                          : 'text-slate-400'
                      }`}
                    >
                      Hold
                    </button>
                  </div>
                </div>

                {activeStrategyTab === 'sell' ? (
                  <div className="space-y-2 text-xs">
                    <span className="inline-block text-[11px] font-bold text-emerald-400">
                      {prediction.retail_sell_playbook.verdict}
                    </span>
                    <p className="text-slate-300 leading-relaxed">
                      {prediction.retail_sell_playbook.action_guide}
                    </p>
                    <p className="text-[11px] text-slate-400 pt-1 border-t border-slate-850">
                      {prediction.retail_sell_playbook.pre_open_order_tip}
                    </p>
                  </div>
                ) : (
                  <div className="space-y-2 text-xs">
                    <span className="inline-block text-[11px] font-bold text-slate-300">
                      Hold with Trailing Stop Loss
                    </span>
                    <p className="text-slate-300 leading-relaxed">
                      {prediction.long_term_hold_playbook.strategy}
                    </p>
                    <div className="flex items-center gap-2 pt-1 border-t border-slate-850 text-[11px]">
                      <span className="text-slate-400">Suggested Stop Loss:</span>
                      <strong className="text-rose-400">₹{prediction.long_term_hold_playbook.suggested_stop_loss}</strong>
                    </div>
                  </div>
                )}
              </div>

              <div className="pt-2 text-[10px] text-slate-500">
                Educational estimate based on pre-market GMP & QIB bids. Not financial advice.
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
