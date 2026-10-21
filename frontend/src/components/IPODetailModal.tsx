import React, { useState } from 'react';
import {
  X,
  Calendar,
  Building2,
  DollarSign,
  Users,
  CheckCircle2,
  ExternalLink,
  Sparkles,
  Share2,
  Check,
  TrendingUp,
  AlertTriangle,
  ShieldCheck,
  Flame,
} from 'lucide-react';
import type { IPOData } from '../types';
import { CompanyLogo } from './CompanyLogo';

interface IPODetailModalProps {
  ipo: IPOData | null;
  isOpen: boolean;
  onClose: () => void;
}

export const IPODetailModal: React.FC<IPODetailModalProps> = ({ ipo, isOpen, onClose }) => {
  const [copied, setCopied] = useState<boolean>(false);
  if (!isOpen || !ipo) return null;

  const isListed = ipo.status === 'Listed';
  const rec = ipo.recommendation_at_ipo;
  const listing = ipo.listing;
  const missed = ipo.missed_opportunity_analysis;
  const sub = ipo.subscription;

  const handleShare = async () => {
    const gmpText = ipo.gmp_closing_day ? `₹${ipo.gmp_closing_day} (${ipo.gmp_closing_percent.toFixed(1)}%)` : 'Live';
    const shareText = `🚀 *${ipo.name} (${ipo.ipo_type} IPO)* on Stocks Suggestions - Dhakrey:\n` +
      `• Price Band: ${ipo.price_band}\n` +
      `• Closing GMP: ${gmpText}\n` +
      `• Est. Listing: ₹${ipo.gmp_estimated_listing}\n` +
      `• Recommendation: *${rec?.verdict || 'Track'}*\n\n` +
      `Check live IPO GMP & allotment status:`;
    const shareUrl = `https://main.d2x1z9kgh5o58m.amplifyapp.com/?tab=ipo`;

    if (navigator.share) {
      try {
        await navigator.share({
          title: `${ipo.name} - IPO Analysis`,
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

  const openKFintech = () => {
    window.open('https://ipostatus.kfintech.com/', '_blank', 'noopener,noreferrer');
  };

  const recBadge = {
    Apply: 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40',
    'Apply with Caution': 'bg-amber-500/20 text-amber-300 border-amber-500/40',
    Avoid: 'bg-rose-500/20 text-rose-300 border-rose-500/40',
  }[rec?.verdict || 'Apply with Caution'];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-2.5 sm:p-6 overflow-y-auto">
      {/* Backdrop */}
      <div className="fixed inset-0 bg-black/80 backdrop-blur-sm" onClick={onClose} />

      {/* Modal Dialog */}
      <div className="relative w-full max-w-3xl bg-slate-900 border border-slate-700/80 rounded-2xl sm:rounded-3xl shadow-2xl z-10 max-h-[92vh] flex flex-col overflow-hidden">
        {/* Header */}
        <div className="p-4 sm:p-5 bg-slate-950/90 border-b border-slate-800 flex items-start justify-between gap-3">
          <div className="flex items-start gap-3 min-w-0">
            <CompanyLogo
              name={ipo.name}
              symbol={ipo.symbol}
              size="lg"
              className="mt-0.5 rounded-2xl shadow-lg border-slate-700 shrink-0"
            />
            <div className="min-w-0">
              <div className="flex items-center gap-2 flex-wrap">
                <h2 className="text-lg sm:text-xl font-bold text-white tracking-tight truncate">
                  {ipo.name}
                </h2>
                <span className={`px-2 py-0.2 rounded-full text-[10px] sm:text-xs font-bold border ${
                  ipo.closes_today
                    ? 'bg-amber-500/20 text-amber-400 border-amber-500/50 animate-pulse'
                    : ipo.status === 'Open'
                    ? 'bg-emerald-500/20 text-emerald-400 border-emerald-500/50 animate-pulse'
                    : ipo.status === 'Upcoming'
                    ? 'bg-sky-500/20 text-sky-400 border-sky-500/50'
                    : ipo.status === 'Listed'
                    ? 'bg-indigo-500/20 text-indigo-400 border-indigo-500/50'
                    : 'bg-slate-800 text-slate-400 border-slate-700'
                }`}>
                  {ipo.closes_today ? 'CLOSES TODAY' : ipo.status}
                </span>
                {ipo.ipo_type === 'SME' && (
                  <span className="text-[10px] font-extrabold px-1.5 py-0.2 rounded bg-amber-500/10 text-amber-300 border border-amber-500/30 uppercase">
                    SME
                  </span>
                )}
                {ipo.symbol && (
                  <span className="font-mono text-[10px] text-slate-400 bg-slate-950 px-1.5 py-0.2 rounded border border-slate-800">
                    {ipo.symbol}
                  </span>
                )}
              </div>
              <div className="flex items-center gap-2 text-xs text-slate-400 mt-1 flex-wrap">
                <span className="truncate">{ipo.sector}</span>
                <span>•</span>
                <span className="flex items-center gap-1">
                  <Calendar className="w-3.5 h-3.5 text-slate-500 shrink-0" />
                  <span>Issue: <strong className="text-slate-200">{ipo.open_date}</strong> - <strong className="text-slate-200">{ipo.close_date}</strong></span>
                </span>
                {ipo.listing_date && (
                  <>
                    <span>•</span>
                    <span>Listing: <strong className="text-slate-200">{ipo.listing_date}</strong></span>
                  </>
                )}
              </div>
            </div>
          </div>

          <div className="flex items-center gap-1.5 shrink-0">
            <button
              onClick={handleShare}
              className={`p-2 rounded-xl transition-all flex items-center gap-1 text-xs font-semibold ${
                copied
                  ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/50'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
              title="Share IPO"
            >
              {copied ? <Check className="w-4 h-4 text-emerald-400" /> : <Share2 className="w-4 h-4" />}
            </button>
            <button
              onClick={onClose}
              className="p-2 text-slate-400 hover:text-white hover:bg-slate-800 rounded-xl transition-colors"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Scrollable Modal Content */}
        <div className="p-4 sm:p-6 overflow-y-auto space-y-4 text-slate-200">
          {/* 1. Official Allotment Check Banner */}
          <div className="bg-emerald-500/10 border border-emerald-500/30 rounded-2xl p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-md">
            <div>
              <div className="flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                <h4 className="font-bold text-white text-sm">Check IPO Allotment Status</h4>
              </div>
              <p className="text-xs text-slate-300 mt-0.5">
                Navigate directly to the official registrar allotment portal (KFintech) to verify your PAN status.
              </p>
            </div>
            <button
              onClick={openKFintech}
              className="px-4 py-2 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-xs rounded-xl flex items-center justify-center gap-1.5 shadow-md shadow-emerald-500/20 transition-all shrink-0 active:scale-95 cursor-pointer"
            >
              <span>Check Allotment Status</span>
              <ExternalLink className="w-3.5 h-3.5" />
            </button>
          </div>

          {/* 2. Key Metrics Snapshot (Clean 4-Card Grid) */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
            <div className="bg-slate-950/70 p-3.5 rounded-2xl border border-slate-800">
              <span className="text-[10px] text-slate-400 block font-medium uppercase tracking-wider">Price Band</span>
              <span className="text-base font-bold text-white mt-0.5 block">{ipo.price_band}</span>
              <span className="text-[10px] text-slate-500 mt-0.5 block">Issue: ₹{ipo.issue_price}</span>
            </div>

            <div className="bg-slate-950/70 p-3.5 rounded-2xl border border-slate-800">
              <span className="text-[10px] text-slate-400 block font-medium uppercase tracking-wider">Lot Size & Min Inv</span>
              <span className="text-base font-bold text-emerald-400 mt-0.5 block">{ipo.lot_size} Shares</span>
              <span className="text-[10px] text-slate-400 mt-0.5 block">₹{ipo.min_investment.toLocaleString('en-IN')}</span>
            </div>

            <div className="bg-slate-950/70 p-3.5 rounded-2xl border border-slate-800">
              <span className="text-[10px] text-slate-400 block font-medium uppercase tracking-wider">Issue Size</span>
              <span className="text-base font-bold text-white mt-0.5 block">₹{ipo.issue_size_cr.toLocaleString('en-IN')} Cr</span>
              <span className="text-[10px] text-slate-500 mt-0.5 block">Fresh: ₹{ipo.fresh_issue_cr} Cr</span>
            </div>

            <div className="bg-slate-950/70 p-3.5 rounded-2xl border border-slate-800">
              <span className="text-[10px] text-slate-400 block font-medium uppercase tracking-wider">
                {isListed ? 'Listing Date' : 'Bidding Closes'}
              </span>
              <span className="text-base font-bold text-white mt-0.5 block">
                {isListed ? (ipo.listing_date || 'Listed') : (ipo.close_date || 'Live')}
              </span>
              <span className="text-[10px] text-slate-500 mt-0.5 block">
                {ipo.closes_today ? '⚡ Closes Today!' : 'Standard Bidding'}
              </span>
            </div>
          </div>

          {/* 3. Expected GMP or Actual Listing Debut Pop */}
          {listing ? (
            <div className="bg-slate-950/90 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-3">
              <div className="flex items-center justify-between gap-2 border-b border-slate-800/80 pb-3">
                <div className="flex items-center gap-2">
                  <TrendingUp className="w-4 h-4 text-emerald-400" />
                  <span className="font-bold text-white text-sm">Listing Debut Performance</span>
                </div>
                <span className={`px-2.5 py-0.5 rounded-full font-bold text-xs ${
                  listing.is_profitable
                    ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30'
                    : 'bg-rose-500/20 text-rose-400 border border-rose-500/30'
                }`}>
                  {listing.listing_gain_percent >= 0 ? '+' : ''}{listing.listing_gain_percent.toFixed(1)}% Return
                </span>
              </div>

              <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 text-xs">
                <div className="bg-slate-900/80 p-3 rounded-xl border border-slate-800/80">
                  <span className="text-[10px] text-slate-400 block">Listing Open Price</span>
                  <span className="text-sm font-bold text-white mt-0.5 block">₹{listing.listing_price.toFixed(2)}</span>
                  <span className="text-[10px] text-slate-500">Issue: ₹{ipo.issue_price}</span>
                </div>
                <div className="bg-slate-900/80 p-3 rounded-xl border border-slate-800/80">
                  <span className="text-[10px] text-slate-400 block">Gain / Loss Per Share</span>
                  <span className={`text-sm font-bold mt-0.5 block ${listing.listing_gain_rs >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                    {listing.listing_gain_rs >= 0 ? '+' : ''}₹{listing.listing_gain_rs.toFixed(2)}
                  </span>
                  <span className="text-[10px] text-slate-500">{listing.listing_gain_percent.toFixed(1)}%</span>
                </div>
                <div className="bg-slate-900/80 p-3 rounded-xl border border-slate-800/80 col-span-2 sm:col-span-1">
                  <span className="text-[10px] text-slate-400 block">Retail 1-Lot Net Profit</span>
                  <span className={`text-sm font-bold mt-0.5 block ${listing.profit_per_lot >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                    {listing.profit_per_lot >= 0 ? '+' : ''}₹{listing.profit_per_lot.toLocaleString('en-IN')}
                  </span>
                  <span className="text-[10px] text-slate-500">{ipo.lot_size} shares/lot</span>
                </div>
              </div>

              {listing.gmp_accuracy && (
                <p className="text-xs text-slate-400 bg-slate-900/50 p-2.5 rounded-xl border border-slate-800/60">
                  <strong className="text-slate-300">GMP Check: </strong>
                  {listing.gmp_accuracy.notes}
                </p>
              )}
            </div>
          ) : (
            <div className="bg-slate-950/90 border border-slate-800 rounded-2xl p-4 sm:p-5 flex items-center justify-between gap-4">
              <div>
                <span className="text-[10px] text-slate-400 font-medium uppercase tracking-wider block">Grey Market Premium (GMP)</span>
                <div className="flex items-baseline gap-2 mt-0.5">
                  <span className="text-xl font-extrabold text-emerald-400">
                    {ipo.gmp_closing_day >= 0 ? '+' : ''}₹{ipo.gmp_closing_day}
                  </span>
                  <span className="text-sm font-bold text-emerald-300">
                    ({ipo.gmp_closing_percent >= 0 ? '+' : ''}{ipo.gmp_closing_percent.toFixed(1)}%)
                  </span>
                </div>
                <p className="text-xs text-slate-400 mt-1">
                  Est. Listing Price: <strong className="text-white">₹{ipo.gmp_estimated_listing}</strong> • Trend: <strong className="text-slate-200">{ipo.gmp_trend}</strong>
                </p>
              </div>

              <div className="text-right">
                <span className="text-[10px] text-slate-400 block">Est. 1-Lot Gain</span>
                <span className="text-base font-bold text-emerald-400">
                  ₹{Math.round(ipo.gmp_closing_day * ipo.lot_size).toLocaleString('en-IN')}
                </span>
              </div>
            </div>
          )}

          {/* 4. AI Recommendation & Key Drivers */}
          {rec && (
            <div className="bg-slate-950/90 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-3">
              <div className="flex items-center justify-between gap-2 border-b border-slate-800/80 pb-3">
                <div className="flex items-center gap-2">
                  <Sparkles className="w-4 h-4 text-emerald-400" />
                  <span className="font-bold text-white text-sm">AI Suggestion & Verdict</span>
                </div>
                <span className={`px-3 py-1 rounded-full text-xs font-bold border ${recBadge}`}>
                  {rec.verdict}
                </span>
              </div>

              <p className="text-xs text-slate-300 leading-relaxed font-medium">
                {rec.reasons}
              </p>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1 text-xs">
                {rec.strengths && rec.strengths.length > 0 && (
                  <div className="bg-slate-900/60 p-3 rounded-xl border border-slate-800/80">
                    <span className="text-emerald-400 font-bold block mb-1">Key Strengths</span>
                    <ul className="space-y-1 text-slate-300">
                      {rec.strengths.slice(0, 2).map((s, idx) => (
                        <li key={idx} className="flex items-start gap-1.5">
                          <span className="text-emerald-400 shrink-0">•</span>
                          <span>{s}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {rec.risks && rec.risks.length > 0 && (
                  <div className="bg-slate-900/60 p-3 rounded-xl border border-slate-800/80">
                    <span className="text-amber-400 font-bold block mb-1">Key Risks</span>
                    <ul className="space-y-1 text-slate-300">
                      {rec.risks.slice(0, 2).map((r, idx) => (
                        <li key={idx} className="flex items-start gap-1.5">
                          <span className="text-amber-400 shrink-0">•</span>
                          <span>{r}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            </div>
          )}

          {/* 5. Subscription Multiples Summary */}
          <div className="bg-slate-950/90 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-3">
            <div className="flex items-center justify-between">
              <h4 className="text-sm font-bold text-white flex items-center gap-2">
                <Users className="w-4 h-4 text-emerald-400" />
                <span>Subscription Demand Summary</span>
              </h4>
              {sub.applications_count && (
                <span className="text-slate-400 text-xs font-semibold">
                  {sub.applications_count}
                </span>
              )}
            </div>

            <div className="grid grid-cols-4 gap-2 text-center text-xs">
              <div className="bg-slate-900/80 p-2.5 rounded-xl border border-slate-800/80">
                <span className="text-[10px] text-slate-400 block">QIB</span>
                <span className="font-bold text-white text-sm mt-0.5 block">
                  {sub.final_day?.qib ? `${sub.final_day.qib}x` : sub.day2?.qib ? `${sub.day2.qib}x` : 'Live'}
                </span>
              </div>
              <div className="bg-slate-900/80 p-2.5 rounded-xl border border-slate-800/80">
                <span className="text-[10px] text-slate-400 block">NII / HNI</span>
                <span className="font-bold text-white text-sm mt-0.5 block">
                  {sub.final_day?.nii ? `${sub.final_day.nii}x` : sub.day2?.nii ? `${sub.day2.nii}x` : 'Live'}
                </span>
              </div>
              <div className="bg-slate-900/80 p-2.5 rounded-xl border border-slate-800/80">
                <span className="text-[10px] text-slate-400 block">Retail (RII)</span>
                <span className="font-bold text-white text-sm mt-0.5 block">
                  {sub.final_day?.retail ? `${sub.final_day.retail}x` : sub.day2?.retail ? `${sub.day2.retail}x` : 'Live'}
                </span>
              </div>
              <div className="bg-emerald-500/10 p-2.5 rounded-xl border border-emerald-500/30">
                <span className="text-[10px] text-emerald-400 block font-semibold">Total</span>
                <span className="font-extrabold text-emerald-300 text-sm mt-0.5 block">
                  {sub.final_day?.total ? `${sub.final_day.total}x` : sub.day2?.total ? `${sub.day2.total}x` : 'Live'}
                </span>
              </div>
            </div>
          </div>
        </div>

        {/* Simplified Footer */}
        <div className="p-4 bg-slate-950 border-t border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="text-xs text-slate-500">
            Registrar: <strong className="text-slate-300">{ipo.registrar || 'KFin Technologies Ltd'}</strong>
          </div>
          <div className="flex items-center gap-2 self-end sm:self-auto">
            <button
              onClick={openKFintech}
              className="px-4 py-2 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-xs inline-flex items-center gap-1.5 shadow-md shadow-emerald-500/20 transition-all cursor-pointer"
            >
              <span>Check Allotment (KFintech)</span>
              <ExternalLink className="w-3.5 h-3.5" />
            </button>
            <button
              onClick={onClose}
              className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold text-xs transition-colors cursor-pointer"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
