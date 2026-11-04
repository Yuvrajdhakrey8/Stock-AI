import React from 'react';
import { X, HelpCircle, Info } from 'lucide-react';

export interface MetricDefinition {
  name: string;
  shortFormula?: string;
  explanation: string;
  idealRange?: string;
}

export const METRIC_DEFINITIONS: Record<string, MetricDefinition> = {
  market_cap: {
    name: 'Market Cap (Market Capitalization)',
    shortFormula: 'Current Share Price × Total Outstanding Shares',
    explanation: 'Total market value of all of a company\'s outstanding shares. It indicates the size and scale of the company (Large-Cap > ₹20,000 Cr, Mid-Cap ₹5,000-₹20,000 Cr, Small-Cap < ₹5,000 Cr).',
  },
  pe_ratio: {
    name: 'P/E Ratio (Price to Earnings)',
    shortFormula: 'Stock Price ÷ Earnings Per Share (EPS)',
    explanation: 'Measures how much investors are willing to pay for each rupee of annual earnings. A lower P/E relative to industry peers often signals an attractive value, while a very high P/E demands strong future growth.',
    idealRange: 'Typically 15x – 30x depending on sector growth rate.',
  },
  pb_ratio: {
    name: 'P/B Ratio (Price to Book Value)',
    shortFormula: 'Stock Price ÷ Book Value Per Share',
    explanation: 'Compares a company\'s market valuation to its net tangible asset value. Especially useful for banks, financial institutions, and capital-intensive manufacturers.',
    idealRange: '< 3.0x is generally considered reasonable for capital-heavy firms.',
  },
  industry_pe: {
    name: 'Industry P/E',
    explanation: 'The weighted median P/E multiple of all publicly traded peers in the same industry sector. Comparing a stock\'s P/E against the Industry P/E shows if it trades at a discount or premium.',
  },
  debt_to_equity: {
    name: 'Debt to Equity Ratio',
    shortFormula: 'Total Debt ÷ Total Shareholders\' Equity',
    explanation: 'Evaluates a company\'s financial leverage. A high ratio indicates that the company finances its operations heavily through debt rather than its own funds.',
    idealRange: '< 0.5 is safe & conservative. > 1.5 indicates elevated financial risk.',
  },
  roe: {
    name: 'ROE (Return on Equity)',
    shortFormula: '(Net Profit ÷ Shareholders\' Equity) × 100',
    explanation: 'Indicates how efficiently company management allocates capital to generate profits from shareholders\' net investments.',
    idealRange: '> 15% consistently is considered high capital efficiency.',
  },
  eps: {
    name: 'EPS (Earnings Per Share)',
    shortFormula: 'Net Profit after Tax ÷ Total Shares',
    explanation: 'Portion of the company\'s net profit allocated to each individual share of common stock. Rising EPS year-over-year is a primary driver of stock price appreciation.',
  },
  dividend_yield: {
    name: 'Dividend Yield',
    shortFormula: '(Annual Dividend Per Share ÷ Current Price) × 100',
    explanation: 'Percentage return a company pays out to shareholders in dividends each year relative to its current share price.',
  },
  book_value: {
    name: 'Book Value Per Share',
    shortFormula: '(Total Assets − Total Liabilities) ÷ Shares',
    explanation: 'The theoretical net asset value each shareholder would receive if the company paid off all its liabilities and liquidated today.',
  },
  face_value: {
    name: 'Face Value (Nominal Value)',
    explanation: 'The original nominal value of a share as recorded on the stock certificate and in the company\'s charter. Dividends and splits are declared based on face value.',
  },
  dcf_intrinsic_value: {
    name: 'DCF Intrinsic Fair Value',
    shortFormula: 'Sum of Discounted 5-Year Free Cash Flows + Terminal Value',
    explanation: 'A fundamental valuation model that calculates a company\'s true business worth based on its projected future cash generation, discounted back to present value using the cost of capital.',
  },
  graham_number: {
    name: 'Benjamin Graham Number',
    shortFormula: '√(22.5 × EPS × Book Value)',
    explanation: 'The maximum fair purchase price calculated according to the legendary value investor Benjamin Graham. Provides a conservative safety ceiling.',
  },
  margin_of_safety: {
    name: 'Margin of Safety',
    shortFormula: '((Intrinsic Value − Current Price) ÷ Intrinsic Value) × 100',
    explanation: 'The buffer or discount between what a company is fundamentally worth and what it currently costs in the market. A positive margin provides a cushion against error or market corrections.',
  },
  rsi: {
    name: '14-Day RSI (Relative Strength Index)',
    explanation: 'A momentum oscillator that measures the speed and change of price moves on a scale of 0 to 100. RSI below 35 indicates oversold conditions, while RSI above 70 indicates overbought conditions.',
  },
  gmp: {
    name: 'GMP (Grey Market Premium)',
    explanation: 'The unofficial premium or discount at which IPO applications or shares are traded in the unofficial grey market prior to their official listing on NSE/BSE.',
  },
  subscription: {
    name: 'Subscription Rate',
    explanation: 'How many times the offered shares in an IPO have been applied for across QIB (institutions), NII (high-net-worth), and Retail categories.',
  },
};

interface MetricInfoModalProps {
  metricKey: string | null;
  onClose: () => void;
}

export const MetricInfoModal: React.FC<MetricInfoModalProps> = ({ metricKey, onClose }) => {
  if (!metricKey) return null;

  const definition = METRIC_DEFINITIONS[metricKey] || {
    name: metricKey,
    explanation: 'Financial metric used in quantitative equity evaluation.',
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-xs animate-in fade-in duration-150">
      <div
        className="fixed inset-0"
        onClick={onClose}
        aria-hidden="true"
      />
      <div className="relative w-full max-w-md bg-slate-900 border border-slate-750 rounded-2xl p-5 sm:p-6 shadow-2xl z-10 text-left">
        {/* Header */}
        <div className="flex items-start justify-between gap-3 border-b border-slate-800 pb-3">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg bg-slate-800 flex items-center justify-center text-slate-300 shrink-0">
              <Info className="w-4 h-4 text-slate-200" />
            </div>
            <h4 className="text-sm sm:text-base font-bold text-white tracking-tight">
              {definition.name}
            </h4>
          </div>
          <button
            onClick={onClose}
            className="p-1 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors cursor-pointer"
            title="Close"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Content */}
        <div className="mt-3.5 space-y-3 text-xs leading-relaxed text-slate-300">
          <p>{definition.explanation}</p>

          {definition.shortFormula && (
            <div className="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
              <span className="text-[10px] text-slate-400 uppercase font-semibold block mb-0.5">
                Formula
              </span>
              <code className="text-xs font-mono text-slate-200 block">
                {definition.shortFormula}
              </code>
            </div>
          )}

          {definition.idealRange && (
            <div className="flex items-start gap-1.5 text-[11px] text-slate-400">
              <span className="font-semibold text-slate-300">Benchmark:</span>
              <span>{definition.idealRange}</span>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="mt-4 pt-3 border-t border-slate-800 flex justify-end">
          <button
            onClick={onClose}
            className="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-medium transition-colors cursor-pointer"
          >
            Got it
          </button>
        </div>
      </div>
    </div>
  );
};
