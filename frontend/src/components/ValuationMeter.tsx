import React from 'react';
import { ShieldCheck, AlertTriangle, XCircle, TrendingUp, CheckCircle2, Info, ArrowUpRight, ArrowDownRight } from 'lucide-react';
import type { ValuationData } from '../types';

interface ValuationMeterProps {
  valuation: ValuationData;
  currency?: string;
}

export const ValuationMeter: React.FC<ValuationMeterProps> = ({ valuation, currency = 'INR' }) => {
  const {
    verdict,
    verdict_badge,
    verdict_desc,
    action_call,
    composite_score,
    fundamental_score,
    technical_score,
    current_price,
    fair_value,
    margin_of_safety_percent,
    pros,
    cons,
  } = valuation;

  // Determine needle / indicator position (0% = Most Expensive, 50% = Fair, 100% = Best Buy)
  // We map composite_score (0-100) or margin of safety to a percentage
  const scorePercent = Math.min(Math.max(composite_score, 5), 95);

  const isBestBuy = verdict === 'BEST BUY';
  const isFairPrice = verdict === 'AT FAIR PRICE';
  const isExpensive = verdict === 'CURRENTLY EXPENSIVE';

  const badgeConfig = {
    'BEST BUY': {
      bg: 'bg-emerald-500/10 border-emerald-500/40 text-emerald-400',
      pill: 'bg-emerald-500 text-slate-950 font-bold',
      icon: ShieldCheck,
      ring: 'ring-emerald-500/20 shadow-emerald-500/10',
    },
    'AT FAIR PRICE': {
      bg: 'bg-amber-500/10 border-amber-500/40 text-amber-400',
      pill: 'bg-amber-500 text-slate-950 font-bold',
      icon: Info,
      ring: 'ring-amber-500/20 shadow-amber-500/10',
    },
    'CURRENTLY EXPENSIVE': {
      bg: 'bg-rose-500/10 border-rose-500/40 text-rose-400',
      pill: 'bg-rose-500 text-white font-bold',
      icon: AlertTriangle,
      ring: 'ring-rose-500/20 shadow-rose-500/10',
    },
  }[verdict] || {
    bg: 'bg-slate-800 border-slate-700 text-slate-300',
    pill: 'bg-slate-700 text-white',
    icon: Info,
    ring: '',
  };

  const IconComponent = badgeConfig.icon;
  const isDiscount = margin_of_safety_percent > 0;

  return (
    <div className={`p-4 sm:p-6 rounded-2xl sm:rounded-3xl border bg-slate-900/95 shadow-xl relative overflow-hidden ${badgeConfig.bg} ${badgeConfig.ring}`}>
      {/* Background glow effect */}
      <div
        className={`absolute -top-24 -right-24 w-72 h-72 rounded-full blur-3xl opacity-20 pointer-events-none ${
          isBestBuy ? 'bg-emerald-500' : isFairPrice ? 'bg-amber-500' : 'bg-rose-500'
        }`}
      />

      {/* Top Header Row */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800/80 pb-4 sm:pb-5">
        <div>
          <div className="flex items-center gap-2 mb-1.5 flex-wrap">
            <span className="text-[11px] sm:text-xs uppercase tracking-wider font-semibold text-slate-400">
              Quantitative Investment Verdict
            </span>
            <span className="text-[9px] sm:text-[10px] bg-slate-800 text-slate-300 px-2 py-0.5 rounded-full border border-slate-700">
              Hybrid Model
            </span>
          </div>
          <div className="flex items-center gap-2.5 sm:gap-3 flex-wrap">
            <div className={`px-3 sm:px-4 py-1.5 rounded-xl text-sm sm:text-base tracking-wide flex items-center gap-2 shadow-md ${badgeConfig.pill}`}>
              <IconComponent className="w-4 h-4 sm:w-5 sm:h-5 shrink-0" />
              <span>{verdict}</span>
            </div>
            <span className="text-xs sm:text-sm font-semibold text-slate-200">
              {action_call}
            </span>
          </div>
          <p className="text-xs text-slate-400 mt-2 max-w-xl leading-relaxed">
            {verdict_desc}
          </p>
        </div>

        {/* Target Intrinsic Value vs Current Price Box */}
        <div className="grid grid-cols-2 gap-3 sm:flex sm:items-center sm:gap-4 bg-slate-950/70 p-3 sm:p-3.5 rounded-2xl border border-slate-800/80">
          <div>
            <div className="text-[10px] sm:text-[11px] text-slate-400 uppercase font-medium">Estimated Fair Value</div>
            <div className="text-lg sm:text-xl font-bold text-slate-100">
              ₹{fair_value.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
            </div>
            <div className="text-[9px] sm:text-[10px] text-slate-500 mt-0.5 truncate">DCF & Graham benchmark</div>
          </div>
          <div className="hidden sm:block h-10 w-[1px] bg-slate-800" />
          <div>
            <div className="text-[10px] sm:text-[11px] text-slate-400 uppercase font-medium">Margin of Safety</div>
            <div className={`text-lg sm:text-xl font-bold flex items-center gap-0.5 ${isDiscount ? 'text-emerald-400' : 'text-rose-400'}`}>
              {isDiscount ? <ArrowUpRight className="w-4 h-4 sm:w-5 sm:h-5 shrink-0" /> : <ArrowDownRight className="w-4 h-4 sm:w-5 sm:h-5 shrink-0" />}
              <span>{Math.abs(margin_of_safety_percent).toFixed(1)}%</span>
            </div>
            <div className="text-[9px] sm:text-[10px] font-medium text-slate-400 mt-0.5 truncate">
              {isDiscount ? 'Undervalued Discount' : 'Valuation Premium'}
            </div>
          </div>
        </div>
      </div>

      {/* Visual Gauge Bar */}
      <div className="my-5 sm:my-6">
        <div className="flex justify-between items-center text-[10px] sm:text-xs font-semibold mb-2">
          <span className="text-rose-400 flex items-center gap-1">
            <span className="w-1.5 h-1.5 sm:w-2 sm:h-2 rounded-full bg-rose-500" /> EXPENSIVE
          </span>
          <span className="text-amber-400 flex items-center gap-1">
            <span className="w-1.5 h-1.5 sm:w-2 sm:h-2 rounded-full bg-amber-500" /> AT FAIR PRICE
          </span>
          <span className="text-emerald-400 flex items-center gap-1">
            <span className="w-1.5 h-1.5 sm:w-2 sm:h-2 rounded-full bg-emerald-500" /> BEST BUY
          </span>
        </div>

        {/* 3-Color Gradient Track with Needle Pointer */}
        <div className="relative h-3.5 sm:h-4 bg-slate-950 rounded-full p-0.5 border border-slate-800 shadow-inner">
          <div className="w-full h-full rounded-full bg-gradient-to-r from-rose-500 via-amber-400 to-emerald-500 opacity-80" />
          
          {/* Needle / Marker */}
          <div
            className="absolute top-1/2 -translate-y-1/2 -translate-x-1/2 transition-all duration-700 ease-out flex flex-col items-center"
            style={{ left: `${scorePercent}%` }}
          >
            <div className="w-4 h-4 sm:w-5 sm:h-5 rounded-full bg-white border-2 border-slate-900 shadow-lg ring-2 ring-emerald-400/80 animate-pulse" />
          </div>
        </div>

        {/* Score Indicators */}
        <div className="grid grid-cols-3 gap-2 mt-3.5 sm:mt-4 text-center">
          <div className="bg-slate-950/60 p-2 sm:p-2.5 rounded-xl border border-slate-800/80">
            <div className="text-[10px] sm:text-[11px] text-slate-400 truncate">Overall Score</div>
            <div className="text-base sm:text-lg font-bold text-white mt-0.5">
              {composite_score}<span className="text-[10px] sm:text-xs text-slate-400 font-normal">/100</span>
            </div>
          </div>
          <div className="bg-slate-950/60 p-2 sm:p-2.5 rounded-xl border border-slate-800/80">
            <div className="text-[10px] sm:text-[11px] text-slate-400 truncate">Fundamental (60%)</div>
            <div className="text-base sm:text-lg font-bold text-emerald-400 mt-0.5">
              {fundamental_score}<span className="text-[10px] sm:text-xs text-slate-400 font-normal">/100</span>
            </div>
          </div>
          <div className="bg-slate-950/60 p-2 sm:p-2.5 rounded-xl border border-slate-800/80">
            <div className="text-[10px] sm:text-[11px] text-slate-400 truncate">Technical (40%)</div>
            <div className="text-base sm:text-lg font-bold text-teal-400 mt-0.5">
              {technical_score}<span className="text-[10px] sm:text-xs text-slate-400 font-normal">/100</span>
            </div>
          </div>
        </div>
      </div>

      {/* Decision Rationale: Pros & Cons */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-5 pt-4 border-t border-slate-800/80 text-xs">
        {/* Supporting Reasons (Pros) */}
        <div className="bg-slate-950/50 p-4 rounded-2xl border border-emerald-900/30">
          <div className="flex items-center gap-1.5 font-bold text-emerald-400 uppercase tracking-wider mb-2.5">
            <CheckCircle2 className="w-4 h-4" />
            <span>Investment Highlights & Catalysts</span>
          </div>
          {pros.length > 0 ? (
            <ul className="space-y-1.5">
              {pros.map((pro, idx) => (
                <li key={idx} className="flex items-start gap-2 text-slate-300">
                  <span className="text-emerald-400 font-bold">•</span>
                  <span>{pro}</span>
                </li>
              ))}
            </ul>
          ) : (
            <p className="text-slate-500 italic">No major value catalysts identified.</p>
          )}
        </div>

        {/* Cautionary Factors (Cons) */}
        <div className="bg-slate-950/50 p-4 rounded-2xl border border-rose-900/30">
          <div className="flex items-center gap-1.5 font-bold text-rose-400 uppercase tracking-wider mb-2.5">
            <AlertTriangle className="w-4 h-4" />
            <span>Valuation & Technical Caution Points</span>
          </div>
          {cons.length > 0 ? (
            <ul className="space-y-1.5">
              {cons.map((con, idx) => (
                <li key={idx} className="flex items-start gap-2 text-slate-300">
                  <span className="text-rose-400 font-bold">•</span>
                  <span>{con}</span>
                </li>
              ))}
            </ul>
          ) : (
            <p className="text-slate-500 italic">No red flags detected in current evaluation.</p>
          )}
        </div>
      </div>
    </div>
  );
};
