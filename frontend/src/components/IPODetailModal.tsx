import React, { useState } from 'react';
import {
  X,
  TrendingUp,
  ShieldCheck,
  AlertTriangle,
  Calendar,
  Building2,
  DollarSign,
  Users,
  CheckCircle2,
  Flame,
  ArrowUpRight,
  ArrowDownRight,
  HelpCircle,
  Sparkles,
  Zap,
  Share2,
  Check,
} from 'lucide-react';
import type { IPOData } from '../types';

interface IPODetailModalProps {
  ipo: IPOData | null;
  isOpen: boolean;
  onClose: () => void;
}

export const IPODetailModal: React.FC<IPODetailModalProps> = ({ ipo, isOpen, onClose }) => {
  const [familyAccounts, setFamilyAccounts] = useState<number>(3);
  const [copied, setCopied] = useState<boolean>(false);
  if (!isOpen || !ipo) return null;

  const isListed = ipo.status === 'Listed';
  const rec = ipo.recommendation_at_ipo;
  const listing = ipo.listing;
  const missed = ipo.missed_opportunity_analysis;
  const sub = ipo.subscription;

  const handleShare = async () => {
    const gmpText = ipo.gmp_closing_day ? `₹${ipo.gmp_closing_day} (${ipo.gmp_closing_percent.toFixed(1)}%)` : 'Live';
    const shareText = `🚀 *${ipo.name} (${ipo.ipo_type} IPO)* on DhakreyStock AI:\n` +
      `• Price Band: ${ipo.price_band}\n` +
      `• Closing GMP: ${gmpText}\n` +
      `• Est. Listing: ₹${ipo.gmp_estimated_listing}\n` +
      `• Recommendation: *${rec?.verdict || 'Track'}*\n\n` +
      `Check live IPO GMP, subscriptions & retail allotment strategies:`;
    const shareUrl = `https://main.d2x1z9kgh5o58m.amplifyapp.com/?tab=ipo`;

    if (navigator.share) {
      try {
        await navigator.share({
          title: `${ipo.name} - IPO Analysis`,
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

  const recBadge = {
    Apply: 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40',
    'Apply with Caution': 'bg-amber-500/20 text-amber-300 border-amber-500/40',
    Avoid: 'bg-rose-500/20 text-rose-300 border-rose-500/40',
  }[rec?.verdict || 'Apply with Caution'];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-2.5 sm:p-6 overflow-y-auto">
      {/* Backdrop */}
      <div className="fixed inset-0 bg-black/75 backdrop-blur-sm" onClick={onClose} />

      {/* Modal Dialog */}
      <div className="relative w-full max-w-4xl bg-slate-900 border border-slate-700/80 rounded-2xl sm:rounded-3xl shadow-2xl z-10 max-h-[92vh] flex flex-col overflow-hidden">
        {/* Header */}
        <div className="p-4 sm:p-6 bg-slate-950/80 border-b border-slate-800 flex items-start justify-between gap-3 sm:gap-4">
          <div className="min-w-0">
            <div className="flex items-center gap-1.5 sm:gap-2.5 flex-wrap">
              <h2 className="text-lg sm:text-2xl font-bold text-white tracking-tight truncate">
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
              <span className="text-[10px] sm:text-xs font-semibold px-2 py-0.2 rounded bg-slate-800 text-slate-300 border border-slate-700">
                {ipo.ipo_type} IPO
              </span>
              {ipo.symbol && (
                <span className="font-mono text-[10px] sm:text-xs text-slate-400 bg-slate-950 px-1.5 py-0.2 rounded border border-slate-800">
                  {ipo.symbol}
                </span>
              )}
            </div>
            <div className="flex items-center gap-2 sm:gap-3 text-[11px] sm:text-xs text-slate-400 mt-1 flex-wrap">
              <span className="truncate">{ipo.sector}</span>
              <span>•</span>
              <span className="flex items-center gap-1">
                <Calendar className="w-3.5 h-3.5 text-slate-500 shrink-0" />
                Issue: <strong className="text-slate-200">{ipo.open_date}</strong> - <strong className="text-slate-200">{ipo.close_date}</strong>
              </span>
              {ipo.listing_date && (
                <>
                  <span>•</span>
                  <span>Listing: <strong className="text-slate-200">{ipo.listing_date}</strong></span>
                </>
              )}
            </div>
          </div>

          <div className="flex items-center gap-1.5 shrink-0">
            <button
              onClick={handleShare}
              className={`p-1.5 sm:p-2 rounded-xl transition-all flex items-center gap-1 text-xs font-semibold ${
                copied
                  ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/50'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
              title="Share live IPO analysis"
            >
              {copied ? (
                <>
                  <Check className="w-4 h-4 text-emerald-400" />
                  <span className="text-[11px] text-emerald-400">Copied</span>
                </>
              ) : (
                <>
                  <Share2 className="w-4 h-4 text-slate-400" />
                  <span className="hidden xs:inline text-[11px]">Share</span>
                </>
              )}
            </button>

            <button
              onClick={onClose}
              className="p-1.5 sm:p-2 text-slate-400 hover:text-white rounded-xl hover:bg-slate-800 transition-colors"
              title="Close"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Scrollable Content */}
        <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-4 sm:space-y-6 text-xs text-slate-300">
          {/* Key Issue Specs Banner */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5 sm:gap-3 bg-slate-950/60 p-3 sm:p-4 rounded-xl sm:rounded-2xl border border-slate-800">
            <div>
              <div className="text-slate-500">Price Band</div>
              <div className="text-base font-bold text-white mt-0.5">{ipo.price_band}</div>
              <div className="text-[11px] text-slate-400 mt-0.5">Cut-off: ₹{ipo.issue_price}</div>
            </div>
            <div>
              <div className="text-slate-500">Lot Size & Min Bid</div>
              <div className="text-base font-bold text-white mt-0.5">{ipo.lot_size} Shares</div>
              <div className="text-[11px] text-slate-400 mt-0.5">₹{ipo.min_investment.toLocaleString('en-IN')} (1 Lot)</div>
            </div>
            <div>
              <div className="text-slate-500">Total Issue Size</div>
              <div className="text-base font-bold text-white mt-0.5">₹{ipo.issue_size_cr.toLocaleString('en-IN')} Cr</div>
              <div className="text-[11px] text-slate-400 mt-0.5">
                Fresh: ₹{ipo.fresh_issue_cr ?? 0} Cr | OFS: ₹{ipo.ofs_cr ?? 0} Cr
              </div>
            </div>
            <div>
              <div className="text-slate-500">Closing-Day GMP</div>
              <div className={`text-base font-bold mt-0.5 ${ipo.gmp_closing_day >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                {ipo.gmp_closing_day >= 0 ? '+' : ''}₹{ipo.gmp_closing_day} ({ipo.gmp_closing_percent.toFixed(1)}%)
              </div>
              <div className="text-[11px] text-slate-400 mt-0.5">Est. List: ₹{ipo.gmp_estimated_listing}</div>
            </div>
          </div>

          {/* 1. Recommendation Box */}
          {rec && (
            <div className="bg-slate-950/90 p-5 rounded-2xl border border-slate-800 space-y-3">
              <div className="flex items-center justify-between flex-wrap gap-2">
                <div className="flex items-center gap-2">
                  <span className="text-xs uppercase font-bold tracking-wider text-slate-400">
                    Application Recommendation:
                  </span>
                  <span className={`px-3 py-1 rounded-xl text-xs font-bold border ${recBadge}`}>
                    {rec.verdict}
                  </span>
                </div>
                <div className="flex items-center gap-3 text-xs">
                  <span>
                    Listing Gain Potential: <strong className="text-white">{rec.listing_gain_prospect}</strong>
                  </span>
                  <span>•</span>
                  <span>
                    Long-Term Profile: <strong className="text-emerald-400">{rec.long_term_potential}</strong>
                  </span>
                </div>
              </div>

              <p className="text-slate-300 leading-relaxed pt-2 border-t border-slate-800/80">
                {rec.reasons}
              </p>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
                <div className="bg-slate-900/80 p-3 rounded-xl border border-emerald-950">
                  <div className="font-bold text-emerald-400 flex items-center gap-1.5 mb-1.5">
                    <CheckCircle2 className="w-4 h-4" />
                    <span>Key Strengths & Growth Catalysts</span>
                  </div>
                  <ul className="space-y-1">
                    {rec.strengths.map((str, i) => (
                      <li key={i} className="flex items-start gap-1.5 text-slate-300">
                        <span className="text-emerald-400 font-bold">•</span>
                        <span>{str}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                <div className="bg-slate-900/80 p-3 rounded-xl border border-rose-950">
                  <div className="font-bold text-rose-400 flex items-center gap-1.5 mb-1.5">
                    <AlertTriangle className="w-4 h-4" />
                    <span>Risk Factors & Downside Alerts</span>
                  </div>
                  <ul className="space-y-1">
                    {rec.risks.map((r, i) => (
                      <li key={i} className="flex items-start gap-1.5 text-slate-300">
                        <span className="text-rose-400 font-bold">•</span>
                        <span>{r}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </div>
          )}

          {/* 2. Listing Gains and Losses (if listed) */}
          {isListed && listing && (
            <div className="bg-slate-950/80 p-5 rounded-2xl border border-slate-800 space-y-4">
              <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                <h3 className="text-sm font-bold text-white flex items-center gap-2">
                  <TrendingUp className="w-4 h-4 text-emerald-400" />
                  <span>Actual Listing Day Outcome</span>
                </h3>
                <span className={`px-2.5 py-0.5 rounded-full font-bold text-xs ${
                  listing.is_profitable
                    ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40'
                    : 'bg-rose-500/20 text-rose-400 border border-rose-500/40'
                }`}>
                  {listing.is_profitable ? 'Profitable Listing Day' : 'Discount / Loss Listing'}
                </span>
              </div>

              <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
                <div className="bg-slate-900 p-3 rounded-xl border border-slate-800">
                  <div className="text-slate-500">Issue Price</div>
                  <div className="text-base font-bold text-white mt-0.5">₹{ipo.issue_price}</div>
                </div>
                <div className="bg-slate-900 p-3 rounded-xl border border-slate-800">
                  <div className="text-slate-500">Actual Listing Price</div>
                  <div className="text-base font-bold text-white mt-0.5">₹{listing.listing_price}</div>
                </div>
                <div className="bg-slate-900 p-3 rounded-xl border border-slate-800">
                  <div className="text-slate-500">Listing Gain / Loss</div>
                  <div className={`text-base font-bold mt-0.5 ${listing.listing_gain_rs >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                    {listing.listing_gain_rs >= 0 ? '+' : ''}₹{listing.listing_gain_rs} ({listing.listing_gain_percent.toFixed(2)}%)
                  </div>
                </div>
                <div className="bg-slate-900 p-3 rounded-xl border border-slate-800">
                  <div className="text-slate-500">Retail Profit (1 Lot)</div>
                  <div className={`text-base font-bold mt-0.5 ${listing.profit_per_lot >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                    {listing.profit_per_lot >= 0 ? '+' : ''}₹{listing.profit_per_lot.toLocaleString('en-IN')}
                  </div>
                </div>
              </div>

              {/* GMP Reliability Evaluation */}
              {listing.gmp_accuracy && (
                <div className="p-3.5 rounded-xl bg-slate-900 border border-slate-800 text-xs">
                  <div className="font-semibold text-slate-200 flex items-center justify-between">
                    <span>Grey Market (GMP) Reliability Check:</span>
                    <span className="text-emerald-400 font-bold">{listing.gmp_accuracy.reliability}</span>
                  </div>
                  <p className="text-slate-400 mt-1 leading-relaxed">{listing.gmp_accuracy.notes}</p>
                </div>
              )}
            </div>
          )}

          {/* 3. Missed Opportunity Analysis */}
          {missed && (
            <div className={`p-5 rounded-2xl border ${
              missed.is_missed_opp
                ? 'bg-amber-950/20 border-amber-800/60'
                : 'bg-emerald-950/20 border-emerald-800/60'
            }`}>
              <div className="flex items-center justify-between gap-2 mb-2">
                <span className="text-xs font-bold uppercase tracking-wider text-slate-400">
                  Decision Review & Retrospective
                </span>
                <span className={`px-2.5 py-0.5 rounded-full font-bold text-xs ${
                  missed.is_missed_opp
                    ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40'
                    : 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40'
                }`}>
                  {missed.verdict}
                </span>
              </div>
              <p className="text-slate-300 leading-relaxed">{missed.explanation}</p>
              {missed.retail_profit_lost > 0 && (
                <div className="mt-2 text-[11px] text-amber-400 font-medium">
                  Opportunity Cost: ₹{missed.retail_profit_lost.toLocaleString('en-IN')} per retail lot
                </div>
              )}
            </div>
          )}

          {/* 4. Day-by-Day Subscription Demand Progression */}
          <div className="bg-slate-950/80 p-5 rounded-2xl border border-slate-800 space-y-3">
            <div className="flex items-center justify-between">
              <h3 className="text-sm font-bold text-white flex items-center gap-2">
                <Users className="w-4 h-4 text-emerald-400" />
                <span>Subscription Demand Progression (Bidding Multiples)</span>
              </h3>
              {sub.applications_count && (
                <span className="text-slate-400 font-medium text-[11px]">
                  {sub.applications_count}
                </span>
              )}
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs">
                <thead className="text-[10px] uppercase text-slate-500 border-b border-slate-800">
                  <tr>
                    <th className="py-2 px-3">Bidding Stage</th>
                    <th className="py-2 px-3">QIB (Institutions)</th>
                    <th className="py-2 px-3">NII / HNI</th>
                    <th className="py-2 px-3">Retail (RII)</th>
                    <th className="py-2 px-3 font-bold text-slate-200">Total Bidding</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800/60">
                  {sub.day1 && (
                    <tr>
                      <td className="py-2 px-3 text-slate-400 font-medium">Day 1 Demand</td>
                      <td className="py-2 px-3">{sub.day1.qib}x</td>
                      <td className="py-2 px-3">{sub.day1.nii}x</td>
                      <td className="py-2 px-3">{sub.day1.retail}x</td>
                      <td className="py-2 px-3 font-bold text-slate-300">{sub.day1.total}x</td>
                    </tr>
                  )}
                  {sub.day2 && (
                    <tr>
                      <td className="py-2 px-3 text-slate-400 font-medium">Day 2 Momentum</td>
                      <td className="py-2 px-3">{sub.day2.qib}x</td>
                      <td className="py-2 px-3">{sub.day2.nii}x</td>
                      <td className="py-2 px-3">{sub.day2.retail}x</td>
                      <td className="py-2 px-3 font-bold text-slate-300">{sub.day2.total}x</td>
                    </tr>
                  )}
                  {sub.final_day ? (
                    <tr className="bg-slate-900/60 font-semibold">
                      <td className="py-2.5 px-3 text-emerald-400">Final Closing Day</td>
                      <td className="py-2.5 px-3 text-emerald-400">{sub.final_day.qib}x</td>
                      <td className="py-2.5 px-3 text-emerald-400">{sub.final_day.nii}x</td>
                      <td className="py-2.5 px-3 text-emerald-400">{sub.final_day.retail}x</td>
                      <td className="py-2.5 px-3 text-emerald-300 font-extrabold text-sm">{sub.final_day.total}x</td>
                    </tr>
                  ) : (
                    <tr>
                      <td colSpan={5} className="py-3 px-3 text-center text-slate-500 italic">
                        Final subscription numbers will be published on closing day.
                      </td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          </div>

          {/* 5. Company Financials & Valuation Multiples */}
          {rec?.financials && (
            <div className="bg-slate-950/80 p-5 rounded-2xl border border-slate-800 space-y-3">
              <h3 className="text-sm font-bold text-white">Audited Financial Ratios at IPO Price</h3>
              <div className="grid grid-cols-2 sm:grid-cols-5 gap-3">
                <div className="bg-slate-900 p-2.5 rounded-xl border border-slate-800 text-center">
                  <div className="text-slate-500 text-[10px]">P/E Ratio</div>
                  <div className="text-sm font-bold text-white mt-0.5">
                    {rec.financials.pe_ratio ? `${rec.financials.pe_ratio}x` : 'Loss-Making'}
                  </div>
                </div>
                <div className="bg-slate-900 p-2.5 rounded-xl border border-slate-800 text-center">
                  <div className="text-slate-500 text-[10px]">Peer Median P/E</div>
                  <div className="text-sm font-bold text-slate-300 mt-0.5">
                    {rec.financials.peer_pe ? `${rec.financials.peer_pe}x` : '-'}
                  </div>
                </div>
                <div className="bg-slate-900 p-2.5 rounded-xl border border-slate-800 text-center">
                  <div className="text-slate-500 text-[10px]">Revenue Growth (YoY)</div>
                  <div className="text-sm font-bold text-emerald-400 mt-0.5">
                    +{rec.financials.revenue_growth_yoy}%
                  </div>
                </div>
                <div className="bg-slate-900 p-2.5 rounded-xl border border-slate-800 text-center">
                  <div className="text-slate-500 text-[10px]">PAT Margin</div>
                  <div className="text-sm font-bold text-white mt-0.5">
                    {rec.financials.pat_margin}%
                  </div>
                </div>
                <div className="bg-slate-900 p-2.5 rounded-xl border border-slate-800 text-center">
                  <div className="text-slate-500 text-[10px]">Debt to Equity</div>
                  <div className="text-sm font-bold text-white mt-0.5">
                    {rec.financials.debt_to_equity ?? '-'}
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* 6. IPO Allotment Strategy & Probability Maximizer */}
          <div className="bg-gradient-to-br from-indigo-950/40 via-slate-950/90 to-slate-900/90 p-5 rounded-2xl border border-indigo-500/30 space-y-4">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div>
                <h3 className="text-sm font-bold text-white flex items-center gap-2">
                  <Sparkles className="w-4 h-4 text-indigo-400" />
                  <span>IPO Allotment Probability & Maximizer Strategy</span>
                </h3>
                <p className="text-[11px] text-slate-400 mt-0.5">
                  SEBI rules state retail allotment is done by computerized lottery. Maximize your odds mathematically.
                </p>
              </div>

              {/* Family Accounts Selector */}
              <div className="flex items-center gap-1.5 bg-slate-900 border border-indigo-500/30 px-2.5 py-1.5 rounded-xl self-start sm:self-auto">
                <span className="text-[10px] text-slate-400 font-medium">Family PANs:</span>
                {[1, 2, 3, 4, 5].map((num) => (
                  <button
                    key={num}
                    onClick={() => setFamilyAccounts(num)}
                    className={`w-6 h-6 rounded-lg text-[11px] font-bold transition-all ${
                      familyAccounts === num
                        ? 'bg-indigo-600 text-white shadow-md shadow-indigo-500/30'
                        : 'text-slate-400 hover:text-white hover:bg-slate-800'
                    }`}
                  >
                    {num}
                  </button>
                ))}
              </div>
            </div>

            {/* Probability Comparison Cards */}
            {(() => {
              const rawSub = ipo.subscription.final_day?.retail ?? ipo.subscription.day2?.retail ?? ipo.subscription.day1?.retail ?? 1.0;
              const retailSub = Math.max(0.1, rawSub);
              const singleChance = retailSub <= 1.0 ? 100 : Math.min(100, Math.round((1 / retailSub) * 1000) / 10);
              const multiChance = retailSub <= 1.0 ? 100 : Math.min(99.9, Math.round((1 - Math.pow(1 - (singleChance / 100), familyAccounts)) * 1000) / 10);
              const multiplier = (multiChance / singleChance).toFixed(1);

              return (
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                  <div className="bg-slate-900/80 p-3 rounded-xl border border-slate-800">
                    <div className="text-[10px] text-slate-400">Current Retail Demand</div>
                    <div className="text-lg font-bold text-white mt-0.5">{retailSub.toFixed(1)}x Overbooked</div>
                    <div className="text-[10px] text-slate-500 mt-0.5">
                      {retailSub <= 1.0 ? 'Guaranteed 100% 1-Lot Allotment' : `1 in every ${Math.round(retailSub)} applications wins`}
                    </div>
                  </div>

                  <div className="bg-slate-900/80 p-3 rounded-xl border border-slate-800">
                    <div className="text-[10px] text-slate-400">1 Demat Account (1 Lot)</div>
                    <div className="text-lg font-bold text-amber-400 mt-0.5">{singleChance}% Chance</div>
                    <div className="text-[10px] text-slate-500 mt-0.5">Baseline single lottery odds</div>
                  </div>

                  <div className="bg-indigo-950/40 p-3 rounded-xl border border-indigo-500/40">
                    <div className="text-[10px] text-indigo-300 font-semibold flex items-center justify-between">
                      <span>{familyAccounts} Family Demat Accounts</span>
                      <span className="text-[9px] px-1.5 py-0.2 bg-indigo-500 text-white rounded font-bold">+{multiplier}x Higher</span>
                    </div>
                    <div className="text-lg font-extrabold text-emerald-400 mt-0.5">{multiChance}% Win Chance</div>
                    <div className="text-[10px] text-indigo-200 mt-0.5">Compound probability of ≥1 lot</div>
                  </div>
                </div>
              );
            })()}

            {/* Strategic Checklist */}
            <div className="bg-slate-950/70 p-3.5 rounded-xl border border-slate-800/80 space-y-2">
              <div className="text-xs font-bold text-slate-200 flex items-center gap-1.5">
                <Zap className="w-3.5 h-3.5 text-amber-400" />
                <span>5 Golden Rules to Maximize IPO Allotment:</span>
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[11px] text-slate-300">
                <div className="flex items-start gap-1.5">
                  <span className="text-emerald-400 font-bold shrink-0">1.</span>
                  <span><strong>Different PANs Rule:</strong> Ek hi PAN se 5 lot lagane se chance nahi badhta. 3 family members ke alag PAN se 1-1 lot lagayein.</span>
                </div>
                <div className="flex items-start gap-1.5">
                  <span className="text-emerald-400 font-bold shrink-0">2.</span>
                  <span><strong>Always Bid Cut-Off Price:</strong> Lower band select karne par issue cut-off price par hote hi bid sidha reject ho jati hai.</span>
                </div>
                <div className="flex items-start gap-1.5">
                  <span className="text-emerald-400 font-bold shrink-0">3.</span>
                  <span><strong>Shareholder Quota (Double Dip):</strong> Agar parent company listed hai, to 1 share hold karke Shareholder + Retail dono me apply karein.</span>
                </div>
                <div className="flex items-start gap-1.5">
                  <span className="text-emerald-400 font-bold shrink-0">4.</span>
                  <span><strong>NetBanking ASBA Preference:</strong> UPI mandate delay ya bank server rejection se bachne ke liye NetBanking ASBA sabse safe hai.</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Footer Actions */}
        <div className="p-4 bg-slate-950 border-t border-slate-800 flex justify-between items-center">
          <div className="text-[11px] text-slate-500">
            Registrar: <strong className="text-slate-400">{ipo.registrar || 'Official Exchange Registrar'}</strong>
          </div>
          <button
            onClick={onClose}
            className="px-5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-semibold text-xs transition-colors"
          >
            Close Research Report
          </button>
        </div>
      </div>
    </div>
  );
};
