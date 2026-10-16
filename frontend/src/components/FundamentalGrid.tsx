import React, { useState } from 'react';
import { ChevronDown, ChevronUp } from 'lucide-react';
import type { StockAnalysisResponse } from '../types';

interface FundamentalGridProps {
  stock: StockAnalysisResponse;
}

export const FundamentalGrid: React.FC<FundamentalGridProps> = ({ stock }) => {
  const [showSummary, setShowSummary] = useState(false);
  const { valuation, ratios } = stock;
  const dToE = ratios.debt_to_equity;

  const cards = [
    {
      title: 'DCF Intrinsic Value',
      value: valuation.dcf_intrinsic_value ? `₹${valuation.dcf_intrinsic_value.toFixed(2)}` : 'N/A',
      desc: '5-Yr discounted free cash flow fair value',
      highlight: valuation.dcf_intrinsic_value && stock.current_price < valuation.dcf_intrinsic_value ? 'positive' : 'neutral',
      badge: 'Intrinsic Value',
    },
    {
      title: 'Graham Number',
      value: valuation.graham_number ? `₹${valuation.graham_number.toFixed(2)}` : 'N/A',
      desc: 'Benjamin Graham max conservative valuation',
      highlight: valuation.graham_number && stock.current_price < valuation.graham_number ? 'positive' : 'neutral',
      badge: 'Defensive Value',
    },
    {
      title: 'P/E Ratio',
      value: ratios.pe_ratio ? `${ratios.pe_ratio.toFixed(1)}x` : 'N/A',
      desc: ratios.pe_ratio && ratios.pe_ratio < 22 ? 'Attractive multiple' : 'Premium valuation multiple',
      highlight: ratios.pe_ratio && ratios.pe_ratio < 22 ? 'positive' : ratios.pe_ratio && ratios.pe_ratio > 45 ? 'negative' : 'neutral',
      badge: 'Valuation Multiple',
    },
    {
      title: 'PEG Ratio',
      value: ratios.peg_ratio ? `${ratios.peg_ratio.toFixed(2)}` : 'N/A',
      desc: ratios.peg_ratio && ratios.peg_ratio <= 1.2 ? 'Growth at reasonable price' : 'High growth required',
      highlight: ratios.peg_ratio && ratios.peg_ratio <= 1.2 ? 'positive' : ratios.peg_ratio && ratios.peg_ratio > 2.2 ? 'negative' : 'neutral',
      badge: 'Growth Adjusted',
    },
    {
      title: 'Price to Book (P/B)',
      value: ratios.pb_ratio ? `${ratios.pb_ratio.toFixed(2)}x` : 'N/A',
      desc: ratios.book_value ? `Book value: ₹${ratios.book_value.toFixed(2)}` : 'Net asset value per share',
      highlight: 'neutral',
      badge: 'Asset Value',
    },
    {
      title: 'Return on Equity (ROE)',
      value: ratios.roe ? `${ratios.roe.toFixed(1)}%` : 'N/A',
      desc: ratios.roe && ratios.roe >= 18 ? 'High capital efficiency' : 'Moderate capital returns',
      highlight: ratios.roe && ratios.roe >= 18 ? 'positive' : 'neutral',
      badge: 'Profitability',
    },
    {
      title: 'Debt to Equity',
      value: dToE != null ? dToE.toFixed(2) : 'N/A',
      desc: dToE != null && dToE < 0.5 ? 'Very low financial leverage' : 'Leverage in line with sector',
      highlight: dToE != null && dToE < 0.5 ? 'positive' : 'neutral',
      badge: 'Solvency Risk',
    },
    {
      title: 'Dividend Yield',
      value: ratios.dividend_yield ? `${ratios.dividend_yield.toFixed(2)}%` : '0.00%',
      desc: 'Annualized dividend yield',
      highlight: ratios.dividend_yield && ratios.dividend_yield > 2.0 ? 'positive' : 'neutral',
      badge: 'Income Yield',
    },
  ];

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="text-sm sm:text-base font-bold text-white flex items-center gap-2">
          <span>Fundamental Valuation & Solvency Matrix</span>
        </h3>
        <span className="text-[11px] sm:text-xs text-slate-400">Audited Financial Ratios</span>
      </div>

      <div className="grid grid-cols-2 sm:grid-cols-2 lg:grid-cols-4 gap-2.5 sm:gap-3.5">
        {cards.map((card, idx) => {
          const isPos = card.highlight === 'positive';
          const isNeg = card.highlight === 'negative';

          return (
            <div
              key={idx}
              className={`p-3 sm:p-4 rounded-xl sm:rounded-2xl border transition-all ${
                isPos
                  ? 'bg-slate-900/90 border-emerald-500/30 shadow-sm shadow-emerald-500/5'
                  : isNeg
                  ? 'bg-slate-900/90 border-rose-500/30'
                  : 'bg-slate-900/80 border-slate-800'
              }`}
            >
              <div className="flex justify-between items-start">
                <span className="text-[9px] sm:text-[10px] uppercase font-bold tracking-wider px-1.5 sm:px-2 py-0.5 rounded bg-slate-800/80 text-slate-400 border border-slate-700/60 truncate">
                  {card.badge}
                </span>
                {isPos && <span className="w-1.5 h-1.5 sm:w-2 sm:h-2 rounded-full bg-emerald-400 shrink-0 ml-1" />}
                {isNeg && <span className="w-1.5 h-1.5 sm:w-2 sm:h-2 rounded-full bg-rose-400 shrink-0 ml-1" />}
              </div>

              <div className="mt-2.5 sm:mt-3">
                <div className="text-[11px] sm:text-xs text-slate-400 font-medium truncate">{card.title}</div>
                <div className={`text-lg sm:text-xl font-bold mt-0.5 ${isPos ? 'text-emerald-400' : isNeg ? 'text-rose-400' : 'text-slate-100'}`}>
                  {card.value}
                </div>
                <div className="text-[10px] sm:text-[11px] text-slate-500 mt-1 line-clamp-1">{card.desc}</div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Business Overview Accordion */}
      {stock.description && (
        <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-4 text-xs">
          <button
            onClick={() => setShowSummary(!showSummary)}
            className="w-full flex items-center justify-between text-slate-300 hover:text-white font-semibold transition-colors"
          >
            <span>About {stock.name}</span>
            <div className="flex items-center gap-1 text-slate-400">
              <span className="text-[11px] font-normal">{showSummary ? 'Collapse' : 'Read Profile'}</span>
              {showSummary ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
            </div>
          </button>
          {showSummary && (
            <p className="mt-3 text-slate-400 leading-relaxed pt-3 border-t border-slate-800">
              {stock.description}
            </p>
          )}
        </div>
      )}
    </div>
  );
};
