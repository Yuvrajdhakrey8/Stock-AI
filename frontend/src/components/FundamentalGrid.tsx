import React, { useState } from 'react';
import { Info } from 'lucide-react';
import type { StockAnalysisResponse } from '../types';
import { MetricInfoModal } from './MetricInfoModal';

interface FundamentalGridProps {
  stock: StockAnalysisResponse;
}

export const FundamentalGrid: React.FC<FundamentalGridProps> = ({ stock }) => {
  const [selectedMetric, setSelectedMetric] = useState<string | null>(null);
  const { valuation, ratios } = stock;
  const dToE = ratios.debt_to_equity;

  // Format Market Cap in Indian Crores
  const formatMarketCap = (cap?: number | null, formatted?: string) => {
    if (formatted) return formatted;
    if (!cap) return 'N/A';
    if (cap >= 1e7) {
      return `₹${(cap / 1e7).toLocaleString('en-IN', { maximumFractionDigits: 0 })}Cr`;
    }
    return `₹${cap.toLocaleString('en-IN')}`;
  };

  const leftColumnMetrics = [
    {
      key: 'market_cap',
      label: 'Market Cap',
      value: formatMarketCap(stock.market_cap, stock.market_cap_formatted),
    },
    {
      key: 'pe_ratio',
      label: 'P/E Ratio (TTM)',
      value: ratios.pe_ratio ? `${ratios.pe_ratio.toFixed(2)}` : 'N/A',
    },
    {
      key: 'pb_ratio',
      label: 'P/B Ratio',
      value: ratios.pb_ratio ? `${ratios.pb_ratio.toFixed(2)}` : 'N/A',
    },
    {
      key: 'debt_to_equity',
      label: 'Debt to Equity',
      value: dToE != null ? dToE.toFixed(2) : 'N/A',
    },
    {
      key: 'dcf_intrinsic_value',
      label: 'DCF Intrinsic Value',
      value: valuation.dcf_intrinsic_value ? `₹${valuation.dcf_intrinsic_value.toFixed(2)}` : 'N/A',
    },
  ];

  const rightColumnMetrics = [
    {
      key: 'roe',
      label: 'ROE',
      value: ratios.roe ? `${ratios.roe.toFixed(2)}%` : 'N/A',
    },
    {
      key: 'eps',
      label: 'EPS (TTM)',
      value: ratios.eps ? `₹${ratios.eps.toFixed(2)}` : 'N/A',
    },
    {
      key: 'dividend_yield',
      label: 'Dividend Yield',
      value: ratios.dividend_yield != null ? `${ratios.dividend_yield.toFixed(2)}%` : '0.00%',
    },
    {
      key: 'book_value',
      label: 'Book Value',
      value: ratios.book_value ? `₹${ratios.book_value.toFixed(2)}` : 'N/A',
    },
    {
      key: 'graham_number',
      label: 'Graham Number',
      value: valuation.graham_number ? `₹${valuation.graham_number.toFixed(2)}` : 'N/A',
    },
  ];

  return (
    <div className="bg-slate-900/50 border border-slate-800 rounded-2xl p-4 sm:p-6 space-y-4">
      {/* Section Header with Groww-style (i) icon */}
      <div className="flex items-center justify-between border-b border-slate-800/80 pb-3">
        <div className="flex items-center gap-2">
          <h3 className="text-base sm:text-lg font-bold text-white tracking-tight">
            Fundamentals
          </h3>
          <button
            onClick={() => setSelectedMetric('market_cap')}
            className="text-slate-500 hover:text-slate-300 transition-colors p-0.5 rounded cursor-pointer"
            title="What do these fundamental metrics mean?"
          >
            <Info className="w-3.5 h-3.5 sm:w-4 sm:h-4" />
          </button>
        </div>
        <span className="text-[11px] text-slate-500 font-medium">Audited Financial Ratios</span>
      </div>

      {/* 2-Column Minimal Key-Value Table (Direct Groww Reference) */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-y-1 md:gap-x-12">
        {/* Left Column */}
        <div className="divide-y divide-slate-800/60">
          {leftColumnMetrics.map((item) => (
            <div key={item.key} className="flex items-center justify-between py-2.5 sm:py-3 text-xs sm:text-sm">
              <div className="flex items-center gap-1.5 text-slate-400">
                <span>{item.label}</span>
                <button
                  onClick={() => setSelectedMetric(item.key)}
                  className="text-slate-600 hover:text-slate-400 transition-colors cursor-pointer"
                  title={`Learn about ${item.label}`}
                >
                  <Info className="w-3 h-3" />
                </button>
              </div>
              <span className="font-medium text-white tracking-tight">{item.value}</span>
            </div>
          ))}
        </div>

        {/* Right Column */}
        <div className="divide-y divide-slate-800/60">
          {rightColumnMetrics.map((item) => (
            <div key={item.key} className="flex items-center justify-between py-2.5 sm:py-3 text-xs sm:text-sm">
              <div className="flex items-center gap-1.5 text-slate-400">
                <span>{item.label}</span>
                <button
                  onClick={() => setSelectedMetric(item.key)}
                  className="text-slate-600 hover:text-slate-400 transition-colors cursor-pointer"
                  title={`Learn about ${item.label}`}
                >
                  <Info className="w-3 h-3" />
                </button>
              </div>
              <span className="font-medium text-white tracking-tight">{item.value}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Modal for Metric Explanations */}
      <MetricInfoModal
        metricKey={selectedMetric}
        onClose={() => setSelectedMetric(null)}
      />
    </div>
  );
};
