import React, { useState, useEffect } from 'react';
import {
  Zap,
  Clock,
  TrendingUp,
  AlertCircle,
  ShieldCheck,
  CheckCircle2,
  ChevronRight,
  Flame,
  ArrowRight,
  Compass,
  Sparkles,
  Info,
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
  const [isExpanded, setIsExpanded] = useState<boolean>(true);

  if (!radarData || !radarData.predictions || radarData.predictions.length === 0) {
    return null;
  }

  const prediction: ListingRadarPrediction = radarData.predictions[selectedIndex] || radarData.predictions[0];
  const isProfit = prediction.expected_gain_percent >= 0;

  const stageBadgeConfig = {
    pre_market_early: {
      bg: 'bg-indigo-500/15 border-indigo-500/40 text-indigo-300',
      label: '7:00 AM – 9:00 AM • Pre-Market Assessment',
      pulse: 'bg-indigo-400',
    },
    pre_open_auction: {
      bg: 'bg-emerald-500/20 border-emerald-500/50 text-emerald-300',
      label: '9:00 AM – 9:45 AM • NSE Call Auction Live',
      pulse: 'bg-emerald-400',
    },
    order_matching: {
      bg: 'bg-amber-500/20 border-amber-500/50 text-amber-300',
      label: '9:45 AM – 10:00 AM • Price Matching Buffer',
      pulse: 'bg-amber-400',
    },
    trading_active: {
      bg: 'bg-teal-500/20 border-teal-500/50 text-teal-300',
      label: '10:00 AM+ • Market Open & Live Trading',
      pulse: 'bg-teal-400',
    },
  }[radarData.session_stage] || {
    bg: 'bg-slate-800 border-slate-700 text-slate-300',
    label: 'Listing Day Pre-Market',
    pulse: 'bg-emerald-400',
  };

  return (
    <div className="relative rounded-3xl border border-emerald-500/30 bg-gradient-to-b from-slate-900/98 via-slate-900/95 to-slate-950 p-4 sm:p-6 shadow-2xl overflow-hidden animate-in fade-in duration-300">
      {/* Background Accent Glows */}
      <div className="absolute top-0 right-0 -mr-20 -mt-20 w-64 h-64 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-64 h-64 bg-teal-500/10 rounded-full blur-3xl pointer-events-none" />

      {/* Top Banner Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3.5">
        <div className="flex items-center gap-2.5 flex-wrap">
          <div className="flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/15 border border-emerald-500/40 text-emerald-400 text-xs font-black uppercase tracking-wider shadow-sm">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            <span>Listing Day Radar</span>
          </div>

          <div className={`px-2.5 py-0.5 rounded-full border text-[11px] font-semibold flex items-center gap-1.5 ${stageBadgeConfig.bg}`}>
            <Clock className="w-3 h-3 shrink-0" />
            <span>{stageBadgeConfig.label}</span>
          </div>
        </div>

        <button
          onClick={() => setIsExpanded(!isExpanded)}
          className="text-xs font-semibold text-slate-400 hover:text-slate-200 transition-colors self-end sm:self-auto cursor-pointer"
        >
          {isExpanded ? 'Collapse' : 'Expand Prediction'}
        </button>
      </div>

      {isExpanded && (
        <div className="mt-4 space-y-4">
          {/* Multiple Candidates Tab (if > 1 IPO is listing today) */}
          {radarData.predictions.length > 1 && (
            <div className="flex items-center gap-2 overflow-x-auto scrollbar-none pb-1">
              <span className="text-[11px] font-bold text-slate-400 shrink-0 uppercase tracking-wider">
                Listing Today:
              </span>
              {radarData.predictions.map((p, idx) => (
                <button
                  key={p.id}
                  onClick={() => setSelectedIndex(idx)}
                  className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all shrink-0 cursor-pointer flex items-center gap-1.5 ${
                    selectedIndex === idx
                      ? 'bg-emerald-500 text-slate-950 shadow-md font-extrabold'
                      : 'bg-slate-800/80 hover:bg-slate-800 text-slate-300'
                  }`}
                >
                  <span>{p.name}</span>
                  <span className={`text-[10px] font-bold ${selectedIndex === idx ? 'text-slate-950' : 'text-emerald-400'}`}>
                    +{p.expected_gain_percent.toFixed(0)}%
                  </span>
                </button>
              ))}
            </div>
          )}

          {/* Main Price Discovery Hero Box */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-4 items-stretch">
            {/* Left 7 Columns: Price Discovery & Profit Metrics */}
            <div className="lg:col-span-7 bg-slate-950/70 border border-slate-800/80 rounded-2xl p-4 sm:p-5 flex flex-col justify-between space-y-4">
              <div className="flex items-start justify-between gap-3">
                <div className="flex items-center gap-3 min-w-0">
                  <CompanyLogo name={prediction.name} symbol={prediction.symbol} size="lg" className="shrink-0 rounded-2xl border-slate-700" />
                  <div className="min-w-0">
                    <div className="flex items-center gap-1.5 flex-wrap">
                      <h3 className="text-base sm:text-lg font-extrabold text-white truncate">
                        {prediction.name}
                      </h3>
                      <span className="text-[10px] bg-slate-800 text-slate-300 px-2 py-0.5 rounded-full font-bold uppercase tracking-wider">
                        {prediction.ipo_type}
                      </span>
                    </div>
                    <p className="text-xs text-slate-400 mt-0.5">
                      Issue Price: <strong className="text-white">₹{prediction.issue_price}</strong> • Lot: <strong className="text-white">{prediction.lot_size} shares</strong>
                    </p>
                  </div>
                </div>

                {onSelectIPO && (
                  <button
                    onClick={() => onSelectIPO(prediction.id)}
                    className="p-2 rounded-xl bg-slate-800/80 hover:bg-slate-800 text-slate-300 hover:text-white transition-colors cursor-pointer shrink-0"
                    title="View Full IPO Details"
                  >
                    <ChevronRight className="w-4 h-4" />
                  </button>
                )}
              </div>

              {/* Price Prediction Range Grid */}
              <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 pt-2 border-t border-slate-800/80">
                <div className="bg-slate-900/90 p-3 rounded-xl border border-slate-800">
                  <span className="text-[10px] text-slate-400 font-bold block uppercase tracking-wider">
                    Predicted Open
                  </span>
                  <div className="text-lg sm:text-xl font-extrabold text-white mt-0.5">
                    ₹{prediction.predicted_open_price}
                  </div>
                  <span className="text-[10px] text-slate-400 block truncate">
                    Range: ₹{prediction.predicted_range.min} - ₹{prediction.predicted_range.max}
                  </span>
                </div>

                <div className="bg-slate-900/90 p-3 rounded-xl border border-slate-800">
                  <span className="text-[10px] text-slate-400 font-bold block uppercase tracking-wider">
                    Expected Listing Gain
                  </span>
                  <div className={`text-lg sm:text-xl font-black mt-0.5 ${isProfit ? 'text-emerald-400' : 'text-rose-400'}`}>
                    {isProfit ? '+' : ''}{prediction.expected_gain_percent.toFixed(1)}%
                  </div>
                  <span className="text-[10px] text-slate-400 block truncate">
                    GMP: ₹{prediction.closing_gmp_rs} (+{prediction.closing_gmp_pct.toFixed(0)}%)
                  </span>
                </div>

                <div className="col-span-2 sm:col-span-1 bg-emerald-500/10 p-3 rounded-xl border border-emerald-500/30">
                  <span className="text-[10px] text-emerald-400 font-bold block uppercase tracking-wider">
                    Est. Profit / 1 Lot
                  </span>
                  <div className="text-lg sm:text-xl font-black text-emerald-300 mt-0.5">
                    {isProfit ? '+' : ''}₹{prediction.expected_profit_per_lot.toLocaleString('en-IN')}
                  </div>
                  <span className="text-[10px] text-emerald-400/80 block truncate">
                    On ₹{(prediction.issue_price * prediction.lot_size).toLocaleString('en-IN')} investment
                  </span>
                </div>
              </div>

              {/* Order Book / Bidding Pressure Gauge */}
              <div className="space-y-1.5 pt-1">
                <div className="flex items-center justify-between text-xs font-semibold">
                  <span className="text-slate-400 flex items-center gap-1.5">
                    <Flame className="w-3.5 h-3.5 text-amber-400" />
                    <span>Pre-Open Bidding Demand:</span>
                  </span>
                  <span className="text-white font-bold">{prediction.bidding_pressure}</span>
                </div>
                <div className="w-full bg-slate-900 h-2.5 rounded-full overflow-hidden border border-slate-800">
                  <div
                    className={`h-full transition-all duration-500 ${
                      prediction.pressure_score >= 75
                        ? 'bg-gradient-to-r from-emerald-500 to-teal-400'
                        : prediction.pressure_score >= 50
                        ? 'bg-gradient-to-r from-amber-500 to-emerald-400'
                        : 'bg-rose-500'
                    }`}
                    style={{ width: `${prediction.pressure_score}%` }}
                  />
                </div>
              </div>
            </div>

            {/* Right 5 Columns: Retail Decision Playbook (Sell vs Hold) */}
            <div className="lg:col-span-5 bg-slate-950/90 border border-slate-800/80 rounded-2xl p-4 sm:p-5 flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between mb-3">
                  <span className="text-xs font-extrabold uppercase tracking-wider text-slate-300 flex items-center gap-1.5">
                    <Compass className="w-4 h-4 text-emerald-400" />
                    <span>Allotment Exit Playbook</span>
                  </span>

                  {/* Strategy Tabs */}
                  <div className="flex items-center bg-slate-900 p-0.5 rounded-xl border border-slate-800 text-[11px] font-bold">
                    <button
                      onClick={() => setActiveStrategyTab('sell')}
                      className={`px-2.5 py-1 rounded-lg transition-all cursor-pointer ${
                        activeStrategyTab === 'sell'
                          ? 'bg-emerald-500 text-slate-950 font-black shadow-sm'
                          : 'text-slate-400 hover:text-white'
                      }`}
                    >
                      Sell Strategy
                    </button>
                    <button
                      onClick={() => setActiveStrategyTab('hold')}
                      className={`px-2.5 py-1 rounded-lg transition-all cursor-pointer ${
                        activeStrategyTab === 'hold'
                          ? 'bg-emerald-500 text-slate-950 font-black shadow-sm'
                          : 'text-slate-400 hover:text-white'
                      }`}
                    >
                      Hold Strategy
                    </button>
                  </div>
                </div>

                {activeStrategyTab === 'sell' ? (
                  <div className="space-y-2.5 text-xs">
                    <div className="flex items-center gap-2">
                      <span className="px-2.5 py-0.5 rounded-full text-xs font-black uppercase tracking-wider bg-emerald-500 text-slate-950">
                        {prediction.retail_sell_playbook.verdict}
                      </span>
                    </div>

                    <p className="text-slate-200 text-xs leading-relaxed">
                      {prediction.retail_sell_playbook.action_guide}
                    </p>

                    <div className="bg-slate-900/90 border border-slate-800 p-2.5 rounded-xl space-y-1 text-[11px] text-slate-300">
                      <div className="flex items-center gap-1 text-emerald-400 font-bold">
                        <CheckCircle2 className="w-3.5 h-3.5 shrink-0" />
                        <span>Pre-Open Execution Tip:</span>
                      </div>
                      <p className="text-slate-400 leading-normal">
                        {prediction.retail_sell_playbook.pre_open_order_tip}
                      </p>
                    </div>
                  </div>
                ) : (
                  <div className="space-y-2.5 text-xs">
                    <div className="flex items-center gap-2">
                      <span className="px-2.5 py-0.5 rounded-full text-xs font-black uppercase tracking-wider bg-indigo-500 text-white">
                        Long-Term Holding Strategy
                      </span>
                    </div>

                    <p className="text-slate-200 text-xs leading-relaxed">
                      {prediction.long_term_hold_playbook.strategy}
                    </p>

                    <div className="bg-slate-900/90 border border-slate-800 p-2.5 rounded-xl text-[11px] space-y-1">
                      <span className="text-slate-400 font-semibold block">Suggested Trailing Stop Loss:</span>
                      <div className="text-base font-black text-rose-400">
                        ₹{prediction.long_term_hold_playbook.suggested_stop_loss}
                      </div>
                      <p className="text-slate-500 text-[10px]">
                        Protects capital if stock drops after opening pop.
                      </p>
                    </div>
                  </div>
                )}
              </div>

              {/* Mandatory SEBI Disclaimer notice */}
              <div className="mt-3 pt-2.5 border-t border-slate-800/80 flex items-center justify-between text-[10px] text-slate-500">
                <span className="flex items-center gap-1">
                  <ShieldCheck className="w-3.5 h-3.5 text-slate-400" />
                  <span>Educational model based on pre-market GMP & QIB bids.</span>
                </span>
                <span className="text-slate-400 font-semibold">10:00 AM Open</span>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
