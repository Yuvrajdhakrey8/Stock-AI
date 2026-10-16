import React from 'react';
import { X, CheckCircle2, ArrowRight } from 'lucide-react';
import type { IPOData } from '../types';

interface IPOCompareModalProps {
  ipos: IPOData[];
  isOpen: boolean;
  onClose: () => void;
  onSelectIPO: (ipo: IPOData) => void;
}

export const IPOCompareModal: React.FC<IPOCompareModalProps> = ({
  ipos,
  isOpen,
  onClose,
  onSelectIPO,
}) => {
  if (!isOpen || ipos.length === 0) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 overflow-y-auto">
      <div className="fixed inset-0 bg-black/75 backdrop-blur-sm" onClick={onClose} />

      <div className="relative w-full max-w-5xl bg-slate-900 border border-slate-700/80 rounded-3xl shadow-2xl z-10 max-h-[90vh] flex flex-col overflow-hidden">
        {/* Header */}
        <div className="p-6 bg-slate-950/80 border-b border-slate-800 flex items-center justify-between">
          <div>
            <h2 className="text-xl font-bold text-white">Side-by-Side IPO Comparison</h2>
            <p className="text-xs text-slate-400 mt-0.5">
              Comparing {ipos.length} IPOs across valuation, demand, grey market, and retail profit
            </p>
          </div>
          <button
            onClick={onClose}
            className="p-2 text-slate-400 hover:text-white rounded-xl hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Comparison Table */}
        <div className="flex-1 overflow-x-auto p-6 text-xs">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="border-b border-slate-800">
                <th className="py-3 px-4 text-slate-500 font-semibold w-48 bg-slate-950/40">Parameters</th>
                {ipos.map((ipo) => (
                  <th key={ipo.id} className="py-3 px-4 min-w-[200px]">
                    <div className="font-bold text-white text-sm">{ipo.name}</div>
                    <div className="flex items-center gap-1.5 mt-1">
                      <span className="text-[10px] px-1.5 py-0.2 rounded bg-slate-800 text-slate-300 font-bold">
                        {ipo.ipo_type}
                      </span>
                      <span className="text-[10px] text-slate-400">{ipo.status}</span>
                    </div>
                  </th>
                ))}
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              <tr>
                <td className="py-3 px-4 font-semibold text-slate-400 bg-slate-950/40">Price Band</td>
                {ipos.map((ipo) => (
                  <td key={ipo.id} className="py-3 px-4 font-bold text-white">
                    {ipo.price_band}
                  </td>
                ))}
              </tr>
              <tr>
                <td className="py-3 px-4 font-semibold text-slate-400 bg-slate-950/40">Lot Size & Min Bid</td>
                {ipos.map((ipo) => (
                  <td key={ipo.id} className="py-3 px-4 text-slate-300">
                    {ipo.lot_size} shares (₹{ipo.min_investment.toLocaleString('en-IN')})
                  </td>
                ))}
              </tr>
              <tr>
                <td className="py-3 px-4 font-semibold text-slate-400 bg-slate-950/40">Total Issue Size</td>
                {ipos.map((ipo) => (
                  <td key={ipo.id} className="py-3 px-4 text-slate-300">
                    ₹{ipo.issue_size_cr.toLocaleString('en-IN')} Cr
                  </td>
                ))}
              </tr>
              <tr>
                <td className="py-3 px-4 font-semibold text-slate-400 bg-slate-950/40">Closing-Day GMP</td>
                {ipos.map((ipo) => (
                  <td key={ipo.id} className="py-3 px-4">
                    <span className={`font-bold ${ipo.gmp_closing_day >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                      {ipo.gmp_closing_day >= 0 ? '+' : ''}₹{ipo.gmp_closing_day} ({ipo.gmp_closing_percent.toFixed(1)}%)
                    </span>
                  </td>
                ))}
              </tr>
              <tr>
                <td className="py-3 px-4 font-semibold text-slate-400 bg-slate-950/40">Total Subscription</td>
                {ipos.map((ipo) => (
                  <td key={ipo.id} className="py-3 px-4 font-bold text-slate-200">
                    {ipo.subscription.final_day ? `${ipo.subscription.final_day.total}x` : ipo.subscription.day2 ? `${ipo.subscription.day2.total}x (Day 2)` : 'Open/Pending'}
                  </td>
                ))}
              </tr>
              <tr>
                <td className="py-3 px-4 font-semibold text-slate-400 bg-slate-950/40">Retail Bidding</td>
                {ipos.map((ipo) => (
                  <td key={ipo.id} className="py-3 px-4 text-slate-300">
                    {ipo.subscription.final_day ? `${ipo.subscription.final_day.retail}x` : ipo.subscription.day2 ? `${ipo.subscription.day2.retail}x` : '-'}
                  </td>
                ))}
              </tr>
              <tr>
                <td className="py-3 px-4 font-semibold text-slate-400 bg-slate-950/40">Listing Gain / Loss</td>
                {ipos.map((ipo) => (
                  <td key={ipo.id} className="py-3 px-4">
                    {ipo.listing ? (
                      <span className={`font-bold ${ipo.listing.listing_gain_percent >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                        {ipo.listing.listing_gain_percent >= 0 ? '+' : ''}{ipo.listing.listing_gain_percent.toFixed(1)}% (₹{ipo.listing.listing_gain_rs})
                      </span>
                    ) : (
                      <span className="text-slate-500 italic">Not Yet Listed</span>
                    )}
                  </td>
                ))}
              </tr>
              <tr>
                <td className="py-3 px-4 font-semibold text-slate-400 bg-slate-950/40">Retail 1-Lot Profit</td>
                {ipos.map((ipo) => (
                  <td key={ipo.id} className="py-3 px-4 font-extrabold text-sm">
                    {ipo.listing ? (
                      <span className={ipo.listing.profit_per_lot >= 0 ? 'text-emerald-400' : 'text-rose-400'}>
                        {ipo.listing.profit_per_lot >= 0 ? '+' : ''}₹{ipo.listing.profit_per_lot.toLocaleString('en-IN')}
                      </span>
                    ) : (
                      <span className="text-slate-500">-</span>
                    )}
                  </td>
                ))}
              </tr>
              <tr>
                <td className="py-3 px-4 font-semibold text-slate-400 bg-slate-950/40">Recommendation</td>
                {ipos.map((ipo) => (
                  <td key={ipo.id} className="py-3 px-4">
                    <span className={`px-2 py-0.5 rounded font-bold text-[11px] ${
                      ipo.recommendation_at_ipo?.verdict === 'Apply'
                        ? 'bg-emerald-500/20 text-emerald-400'
                        : ipo.recommendation_at_ipo?.verdict === 'Avoid'
                        ? 'bg-rose-500/20 text-rose-400'
                        : 'bg-amber-500/20 text-amber-400'
                    }`}>
                      {ipo.recommendation_at_ipo?.verdict || 'N/A'}
                    </span>
                  </td>
                ))}
              </tr>
              <tr>
                <td className="py-3 px-4 font-semibold text-slate-400 bg-slate-950/40">Action</td>
                {ipos.map((ipo) => (
                  <td key={ipo.id} className="py-3 px-4">
                    <button
                      onClick={() => {
                        onSelectIPO(ipo);
                        onClose();
                      }}
                      className="px-3 py-1.5 rounded-lg bg-emerald-500 text-slate-950 font-bold hover:bg-emerald-400 transition-colors inline-flex items-center gap-1"
                    >
                      <span>Full Report</span>
                      <ArrowRight className="w-3.5 h-3.5" />
                    </button>
                  </td>
                ))}
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
