import React, { useState } from 'react';
import { ShieldCheck, AlertTriangle, Info, ArrowUpRight, ArrowDownRight, CheckCircle2 } from 'lucide-react';
import type { ValuationData } from '../types';
import { MetricInfoModal } from './MetricInfoModal';

interface ValuationMeterProps {
  valuation: ValuationData;
  currency?: string;
}

export const ValuationMeter: React.FC<ValuationMeterProps> = ({ valuation, currency = 'INR' }) => {
  const [selectedMetric, setSelectedMetric] = useState<string | null>(null);
  const {
    verdict,
    verdict_desc,
    action_call,
    composite_score,
    fundamental_score,
    technical_score,
    fair_value,
    margin_of_safety_percent,
    pros,
    cons,
  } = valuation;

  const scorePercent = Math.min(Math.max(composite_score, 5), 95);
  const isDiscount = margin_of_safety_percent > 0;

  const badgeTheme = {
    'BEST BUY': {
      pill: 'bg-teal-950/40 text-teal-300 border border-teal-800/40',
      label: 'Undervalued (Best Buy)',
      icon: ShieldCheck,
    },
    'AT FAIR PRICE': {
      pill: 'bg-amber-950/40 text-amber-300 border border-amber-800/40',
      label: 'At Fair Price',
      icon: Info,
    },
    'CURRENTLY EXPENSIVE': {
      pill: 'bg-rose-950/40 text-rose-300 border border-rose-800/40',
      label: 'Stretched (Expensive)',
      icon: AlertTriangle,
    },
  }[verdict] || {
    pill: 'bg-slate-800 text-slate-300 border border-slate-700',
    label: verdict,
    icon: Info,
  };

  const IconComp = badgeTheme.icon;

  return (
    <div className="bg-slate-900/50 border border-slate-800 rounded-2xl p-4 sm:p-6 space-y-5">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800/80 pb-4">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <span className="text-xs uppercase tracking-wider font-semibold text-slate-400">
              Quantitative Valuation
            </span>
            <button
              onClick={() => setSelectedMetric('dcf_intrinsic_value')}
              className="text-slate-500 hover:text-slate-300 transition-colors cursor-pointer"
              title="Learn about intrinsic valuation"
            >
              <Info className="w-3.5 h-3.5" />
            </button>
          </div>
          <div className="flex items-center gap-2.5 flex-wrap">
            <span className={`px-2.5 py-1 rounded-lg text-xs font-bold flex items-center gap-1.5 ${badgeTheme.pill}`}>
              <IconComp className="w-3.5 h-3.5 shrink-0" />
              <span>{badgeTheme.label}</span>
            </span>
            <span className="text-xs font-medium text-slate-300">
              {action_call}
            </span>
          </div>
          <p className="text-xs text-slate-400 mt-2 leading-relaxed max-w-xl">
            {verdict_desc}
          </p>
        </div>

        {/* Intrinsic Fair Value & Margin */}
        <div className="flex items-center gap-5 bg-slate-950/70 p-3 sm:p-3.5 rounded-xl border border-slate-800 self-start sm:self-auto">
          <div>
            <div className="flex items-center gap-1 text-[11px] text-slate-400">
              <span>Fair Value</span>
              <button
                onClick={() => setSelectedMetric('dcf_intrinsic_value')}
                className="text-slate-500 hover:text-slate-300 cursor-pointer"
              >
                <Info className="w-3 h-3" />
              </button>
            </div>
            <div className="text-base sm:text-lg font-bold text-white mt-0.5">
              ₹{fair_value.toLocaleString('en-IN', { maximumFractionDigits: 1 })}
            </div>
          </div>
          <div className="w-[1px] h-8 bg-slate-800" />
          <div>
            <div className="flex items-center gap-1 text-[11px] text-slate-400">
              <span>Margin of Safety</span>
              <button
                onClick={() => setSelectedMetric('margin_of_safety')}
                className="text-slate-500 hover:text-slate-300 cursor-pointer"
              >
                <Info className="w-3 h-3" />
              </button>
            </div>
            <div className={`text-base sm:text-lg font-bold flex items-center gap-0.5 mt-0.5 ${
              isDiscount ? 'text-teal-300' : 'text-rose-300'
            }`}>
              {isDiscount ? <ArrowUpRight className="w-4 h-4 shrink-0" /> : <ArrowDownRight className="w-4 h-4 shrink-0" />}
              <span>{Math.abs(margin_of_safety_percent).toFixed(1)}%</span>
            </div>
          </div>
        </div>
      </div>

      {/* Valuation Range Slider */}
      <div className="space-y-2">
        <div className="flex justify-between items-center text-[11px] font-medium text-slate-400">
          <span>Stretched</span>
          <span>At Fair Price</span>
          <span>Undervalued</span>
        </div>

        <div className="relative h-2 bg-slate-800 rounded-full overflow-hidden">
          <div className="w-full h-full bg-gradient-to-r from-rose-500/80 via-amber-400/80 to-emerald-500/80" />
          <div
            className="absolute top-0 bottom-0 w-2.5 bg-white rounded-full shadow-md -translate-x-1/2"
            style={{ left: `${scorePercent}%` }}
          />
        </div>

        <div className="grid grid-cols-3 gap-2 pt-2 text-center text-xs">
          <div className="bg-slate-950/50 p-2 rounded-lg border border-slate-800/80">
            <span className="text-[10px] text-slate-400 block">Overall Score</span>
            <span className="text-sm font-bold text-white mt-0.5 block">{composite_score}/100</span>
          </div>
          <div className="bg-slate-950/50 p-2 rounded-lg border border-slate-800/80">
            <span className="text-[10px] text-slate-400 block">Fundamental (60%)</span>
            <span className="text-sm font-bold text-slate-200 mt-0.5 block">{fundamental_score}/100</span>
          </div>
          <div className="bg-slate-950/50 p-2 rounded-lg border border-slate-800/80">
            <span className="text-[10px] text-slate-400 block">Technical (40%)</span>
            <span className="text-sm font-bold text-slate-200 mt-0.5 block">{technical_score}/100</span>
          </div>
        </div>
      </div>

      {/* Pros & Cons - Clean & Uncluttered */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 pt-3 border-t border-slate-800/80 text-xs">
        <div className="space-y-2">
          <div className="flex items-center gap-1.5 font-semibold text-slate-300">
            <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
            <span>Key Catalysts</span>
          </div>
          {pros.length > 0 ? (
            <ul className="space-y-1.5 text-slate-400">
              {pros.map((p, idx) => (
                <li key={idx} className="flex items-start gap-2">
                  <span className="text-emerald-400 font-bold">•</span>
                  <span>{p}</span>
                </li>
              ))}
            </ul>
          ) : (
            <p className="text-slate-500 italic">No specific catalysts noted.</p>
          )}
        </div>

        <div className="space-y-2">
          <div className="flex items-center gap-1.5 font-semibold text-slate-300">
            <AlertTriangle className="w-4 h-4 text-amber-400 shrink-0" />
            <span>Points to Watch</span>
          </div>
          {cons.length > 0 ? (
            <ul className="space-y-1.5 text-slate-400">
              {cons.map((c, idx) => (
                <li key={idx} className="flex items-start gap-2">
                  <span className="text-amber-400 font-bold">•</span>
                  <span>{c}</span>
                </li>
              ))}
            </ul>
          ) : (
            <p className="text-slate-500 italic">No specific risk flags noted.</p>
          )}
        </div>
      </div>

      <MetricInfoModal
        metricKey={selectedMetric}
        onClose={() => setSelectedMetric(null)}
      />
    </div>
  );
};
