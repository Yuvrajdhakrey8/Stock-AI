import React, { useState } from 'react';
import {
  X,
  Share2,
  Check,
  ChevronDown,
  ChevronUp,
  ExternalLink,
  ShieldCheck,
  Info,
} from 'lucide-react';
import type { IPOData } from '../types';
import { CompanyLogo } from './CompanyLogo';
import { MetricInfoModal } from './MetricInfoModal';

interface IPODetailModalProps {
  ipo: IPOData | null;
  isOpen: boolean;
  onClose: () => void;
}

export const IPODetailModal: React.FC<IPODetailModalProps> = ({ ipo, isOpen, onClose }) => {
  const [copied, setCopied] = useState<boolean>(false);
  const [showInsights, setShowInsights] = useState<boolean>(false);
  const [selectedMetric, setSelectedMetric] = useState<string | null>(null);

  if (!isOpen || !ipo) return null;

  const isClosedOrListed = ipo.status === 'Listed' || ipo.status === 'Closed';
  const rec = ipo.recommendation_at_ipo;
  const listing = ipo.listing;
  const sub = ipo.subscription;

  const actualListingPrice = listing?.listing_price ?? ipo.gmp_estimated_listing ?? ipo.issue_price;
  const actualGainPercent = listing?.listing_gain_percent ?? ipo.gmp_closing_percent ?? 0;
  const actualProfitPerLot = listing?.profit_per_lot ?? Math.round((actualListingPrice - ipo.issue_price) * ipo.lot_size);

  const handleShare = async () => {
    const shareText = `📊 *${ipo.name}* IPO Details:\n` +
      `• Issue Price: ₹${ipo.issue_price}\n` +
      `• Lot Size: ${ipo.lot_size} shares (₹${ipo.min_investment.toLocaleString('en-IN')})\n` +
      `• GMP: ₹${ipo.gmp_closing_day} (+${ipo.gmp_closing_percent.toFixed(0)}%)\n\n` +
      `Track live Indian IPOs on Dhakrey Stocks:`;
    const shareUrl = `https://main.dtvi3uv6gm2u7.amplifyapp.com/?tab=ipo`;

    if (navigator.share) {
      try {
        await navigator.share({ title: `${ipo.name} IPO`, text: shareText, url: shareUrl });
      } catch {
        // Cancelled
      }
    } else {
      try {
        await navigator.clipboard.writeText(`${shareText}\n${shareUrl}`);
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
      } catch {
        // Fallback
      }
    }
  };

  const openRegistrar = () => {
    window.open('https://ipostatus.kfintech.com/', '_blank', 'noopener,noreferrer');
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 overflow-y-auto">
      {/* Backdrop */}
      <div className="fixed inset-0 bg-black/75 backdrop-blur-xs" onClick={onClose} />

      {/* Modal Dialog */}
      <div className="relative w-full max-w-2xl bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl z-10 max-h-[90vh] flex flex-col overflow-hidden text-left">
        {/* Header */}
        <div className="p-4 sm:p-5 bg-slate-950/80 border-b border-slate-800 flex items-start justify-between gap-3">
          <div className="flex items-start gap-3 min-w-0">
            <CompanyLogo
              name={ipo.name}
              symbol={ipo.symbol}
              size="lg"
              className="mt-0.5 rounded-xl border border-slate-800 shrink-0"
            />
            <div className="min-w-0">
              <div className="flex items-center gap-2 flex-wrap">
                <h2 className="text-base sm:text-lg font-bold text-white tracking-tight truncate">
                  {ipo.name}
                </h2>
                <span className="text-[11px] font-medium text-slate-400">
                  {ipo.ipo_type} • {ipo.sector}
                </span>
              </div>
              <div className="flex items-center gap-2 text-xs text-slate-400 mt-1">
                <span>Issue: {ipo.open_date} – {ipo.close_date}</span>
                {ipo.listing_date && <span>• Listing: {ipo.listing_date}</span>}
              </div>
            </div>
          </div>

          <div className="flex items-center gap-1 shrink-0">
            <button
              onClick={handleShare}
              className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors cursor-pointer"
              title="Share IPO"
            >
              {copied ? <Check className="w-4 h-4 text-emerald-400" /> : <Share2 className="w-4 h-4" />}
            </button>
            <button
              onClick={onClose}
              className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors cursor-pointer"
              title="Close"
            >
              <X className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Scrollable Content */}
        <div className="p-4 sm:p-6 overflow-y-auto space-y-5 text-xs sm:text-sm">
          {/* Key Financials (Groww 2-Column Key-Value List) */}
          <div className="bg-slate-950/50 border border-slate-800 rounded-xl p-4">
            <div className="flex items-center justify-between pb-2.5 border-b border-slate-800/80 mb-1">
              <span className="text-xs font-bold text-white uppercase tracking-wider">
                IPO Details
              </span>
              <span className="text-[11px] text-slate-400">Bidding Parameters</span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-x-8 divide-y sm:divide-y-0 divide-slate-800/60">
              {/* Left Column */}
              <div className="divide-y divide-slate-800/60">
                <div className="flex items-center justify-between py-2">
                  <span className="text-slate-400">Price Band</span>
                  <span className="font-medium text-white">{ipo.price_band}</span>
                </div>
                <div className="flex items-center justify-between py-2">
                  <span className="text-slate-400">Issue Price</span>
                  <span className="font-medium text-white">₹{ipo.issue_price}</span>
                </div>
                <div className="flex items-center justify-between py-2">
                  <span className="text-slate-400">Lot Size</span>
                  <span className="font-medium text-white">{ipo.lot_size} Shares</span>
                </div>
                <div className="flex items-center justify-between py-2">
                  <span className="text-slate-400">Min. Retail Investment</span>
                  <span className="font-medium text-white">₹{ipo.min_investment.toLocaleString('en-IN')}</span>
                </div>
              </div>

              {/* Right Column */}
              <div className="divide-y divide-slate-800/60">
                <div className="flex items-center justify-between py-2">
                  <span className="text-slate-400">Issue Size</span>
                  <span className="font-medium text-white">₹{ipo.issue_size_cr.toLocaleString('en-IN')} Cr</span>
                </div>
                <div className="flex items-center justify-between py-2">
                  <span className="text-slate-400">Fresh Issue</span>
                  <span className="font-medium text-white">₹{ipo.fresh_issue_cr} Cr</span>
                </div>
                <div className="flex items-center justify-between py-2">
                  <div className="flex items-center gap-1 text-slate-400">
                    <span>Grey Market (GMP)</span>
                    <button
                      onClick={() => setSelectedMetric('gmp')}
                      className="text-slate-600 hover:text-slate-400"
                    >
                      <Info className="w-3 h-3" />
                    </button>
                  </div>
                  <span className={`font-semibold ${ipo.gmp_closing_day >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                    {ipo.gmp_closing_day >= 0 ? '+' : ''}₹{ipo.gmp_closing_day} ({ipo.gmp_closing_percent.toFixed(0)}%)
                  </span>
                </div>
                <div className="flex items-center justify-between py-2">
                  <span className="text-slate-400">Registrar</span>
                  <span className="font-medium text-slate-300 truncate max-w-[150px]">
                    {ipo.registrar || 'KFin Technologies'}
                  </span>
                </div>
              </div>
            </div>
          </div>

          {/* Subscription Figures (Clean Flat Row) */}
          {sub && (
            <div className="bg-slate-950/50 border border-slate-800 rounded-xl p-4 space-y-2.5">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-1.5">
                  <span className="text-xs font-bold text-white uppercase tracking-wider">
                    Subscription Demand
                  </span>
                  <button
                    onClick={() => setSelectedMetric('subscription')}
                    className="text-slate-600 hover:text-slate-400"
                  >
                    <Info className="w-3 h-3" />
                  </button>
                </div>
                <span className="text-[11px] text-slate-400">{sub.applications_count || 'Category Breakdown'}</span>
              </div>

              <div className="grid grid-cols-4 gap-2 text-center">
                <div className="p-2 rounded-lg bg-slate-900 border border-slate-800">
                  <span className="text-[10px] text-slate-400 block">QIB</span>
                  <span className="text-xs sm:text-sm font-semibold text-white mt-0.5 block">
                    {sub.final_day?.qib ? `${sub.final_day.qib}x` : sub.day2?.qib ? `${sub.day2.qib}x` : 'Live'}
                  </span>
                </div>
                <div className="p-2 rounded-lg bg-slate-900 border border-slate-800">
                  <span className="text-[10px] text-slate-400 block">NII (HNI)</span>
                  <span className="text-xs sm:text-sm font-semibold text-white mt-0.5 block">
                    {sub.final_day?.nii ? `${sub.final_day.nii}x` : sub.day2?.nii ? `${sub.day2.nii}x` : 'Live'}
                  </span>
                </div>
                <div className="p-2 rounded-lg bg-slate-900 border border-slate-800">
                  <span className="text-[10px] text-slate-400 block">Retail</span>
                  <span className="text-xs sm:text-sm font-semibold text-white mt-0.5 block">
                    {sub.final_day?.retail ? `${sub.final_day.retail}x` : sub.day2?.retail ? `${sub.day2.retail}x` : 'Live'}
                  </span>
                </div>
                <div className="p-2 rounded-lg bg-slate-900 border border-slate-800">
                  <span className="text-[10px] text-slate-400 block">Total</span>
                  <span className="text-xs sm:text-sm font-bold text-emerald-400 mt-0.5 block">
                    {sub.final_day?.total ? `${sub.final_day.total}x` : sub.day2?.total ? `${sub.day2.total}x` : 'Live'}
                  </span>
                </div>
              </div>
            </div>
          )}

          {/* Debut Performance (if Listed) */}
          {isClosedOrListed && (
            <div className="bg-slate-950/50 border border-slate-800 rounded-xl p-4 flex items-center justify-between">
              <div>
                <span className="text-[10px] text-slate-400 uppercase font-semibold block">Listing Day Open</span>
                <span className="text-base font-bold text-white mt-0.5 block">₹{actualListingPrice.toFixed(1)}</span>
              </div>
              <div className="text-right">
                <span className="text-[10px] text-slate-400 uppercase font-semibold block">Listing Gain</span>
                <span className={`text-base font-bold block ${actualGainPercent >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                  {actualGainPercent >= 0 ? '+' : ''}{actualGainPercent.toFixed(1)}%
                </span>
              </div>
              <div className="text-right">
                <span className="text-[10px] text-slate-400 uppercase font-semibold block">Profit / 1 Lot</span>
                <span className="text-base font-bold text-white">₹{actualProfitPerLot.toLocaleString('en-IN')}</span>
              </div>
            </div>
          )}

          {/* Optional Insights & Recommendation (Collapsed by Default) */}
          {rec && (
            <div className="border border-slate-800 rounded-xl overflow-hidden">
              <button
                onClick={() => setShowInsights(!showInsights)}
                className="w-full p-3.5 flex items-center justify-between bg-slate-950/60 hover:bg-slate-850 transition-colors cursor-pointer text-left"
              >
                <div className="flex items-center gap-2">
                  <ShieldCheck className="w-4 h-4 text-slate-400" />
                  <span className="text-xs font-semibold text-white">
                    View Analyst Recommendation & Risk Analysis
                  </span>
                </div>
                <div className="flex items-center gap-2">
                  <span className="text-[11px] font-bold text-slate-300">
                    {rec.verdict}
                  </span>
                  {showInsights ? <ChevronUp className="w-3.5 h-3.5 text-slate-400" /> : <ChevronDown className="w-3.5 h-3.5 text-slate-400" />}
                </div>
              </button>

              {showInsights && (
                <div className="p-4 bg-slate-950/90 border-t border-slate-800 space-y-3 animate-in fade-in duration-150">
                  <p className="text-xs text-slate-300 leading-relaxed">{rec.reasons}</p>
                  {rec.strengths && rec.strengths.length > 0 && (
                    <div className="space-y-1">
                      <span className="text-[11px] font-semibold text-emerald-400">Strengths:</span>
                      <ul className="list-disc list-inside text-xs text-slate-400 space-y-0.5">
                        {rec.strengths.map((s, i) => <li key={i}>{s}</li>)}
                      </ul>
                    </div>
                  )}
                  {rec.risks && rec.risks.length > 0 && (
                    <div className="space-y-1">
                      <span className="text-[11px] font-semibold text-amber-400">Risks:</span>
                      <ul className="list-disc list-inside text-xs text-slate-400 space-y-0.5">
                        {rec.risks.map((r, i) => <li key={i}>{r}</li>)}
                      </ul>
                    </div>
                  )}
                </div>
              )}
            </div>
          )}
        </div>

        {/* Quiet Footer */}
        <div className="p-3.5 bg-slate-950 border-t border-slate-800 flex items-center justify-between text-xs">
          <button
            onClick={openRegistrar}
            className="text-slate-400 hover:text-emerald-400 transition-colors inline-flex items-center gap-1 cursor-pointer"
          >
            <span>Allotment portal (KFintech)</span>
            <ExternalLink className="w-3 h-3" />
          </button>
          <button
            onClick={onClose}
            className="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 font-medium transition-colors cursor-pointer"
          >
            Close
          </button>
        </div>
      </div>

      <MetricInfoModal
        metricKey={selectedMetric}
        onClose={() => setSelectedMetric(null)}
      />
    </div>
  );
};
