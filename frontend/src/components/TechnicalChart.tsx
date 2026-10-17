import React, { useState } from 'react';
import {
  ResponsiveContainer,
  AreaChart,
  Area,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ReferenceLine,
} from 'recharts';
import type { ChartPoint, ValuationData } from '../types';
import { Activity } from 'lucide-react';

interface TechnicalChartProps {
  chartData: ChartPoint[];
  valuation: ValuationData;
  currentPrice: number;
}

export const TechnicalChart: React.FC<TechnicalChartProps> = ({
  chartData,
  valuation,
  currentPrice,
}) => {
  const [timeframe, setTimeframe] = useState<'1M' | '3M' | '6M' | '1Y'>('6M');
  const [showSMA50, setShowSMA50] = useState(true);
  const [showSMA200, setShowSMA200] = useState(true);

  if (!chartData || chartData.length === 0) {
    return (
      <div className="bg-slate-900/80 border border-slate-800 rounded-3xl p-8 text-center text-slate-500">
        No chart history available for this security.
      </div>
    );
  }

  // Filter timeframe
  const pointsMap = {
    '1M': 22,
    '3M': 65,
    '6M': 130,
    '1Y': 250,
  };
  const filteredData = chartData.slice(-pointsMap[timeframe]);

  // Compute min and max for responsive Y-axis padding
  const prices = filteredData.map((d) => d.close);
  const minPrice = Math.floor(Math.min(...prices) * 0.96);
  const maxPrice = Math.ceil(Math.max(...prices) * 1.04);

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl sm:rounded-3xl p-4 sm:p-6 shadow-xl space-y-4 sm:space-y-6">
      {/* Chart Controls & Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 sm:gap-4">
        <div>
          <div className="flex items-center gap-2">
            <h3 className="text-sm sm:text-base font-bold text-white flex items-center gap-2">
              <Activity className="w-4 h-4 text-emerald-400 shrink-0" />
              <span>Price Trend & Moving Average Timing</span>
            </h3>
          </div>
          <p className="text-[11px] sm:text-xs text-slate-400 mt-0.5">
            Compare live price with 50 DMA and 200 DMA institutional support levels
          </p>
        </div>

        {/* Toggles & Timeframe selector */}
        <div className="flex items-center gap-2 sm:gap-3 flex-wrap justify-between sm:justify-start">
          {/* DMA Toggles */}
          <div className="flex items-center gap-1.5 sm:gap-2 text-[11px] sm:text-xs">
            <button
              onClick={() => setShowSMA50(!showSMA50)}
              className={`px-2 sm:px-2.5 py-1 rounded-lg border flex items-center gap-1.5 transition-all ${
                showSMA50
                  ? 'bg-amber-500/20 text-amber-300 border-amber-500/50 font-semibold'
                  : 'bg-slate-800/60 text-slate-500 border-slate-700/60'
              }`}
            >
              <span className="w-1.5 h-1.5 sm:w-2 sm:h-2 rounded-full bg-amber-400" />
              <span>50 DMA</span>
            </button>
            <button
              onClick={() => setShowSMA200(!showSMA200)}
              className={`px-2 sm:px-2.5 py-1 rounded-lg border flex items-center gap-1.5 transition-all ${
                showSMA200
                  ? 'bg-indigo-500/20 text-indigo-300 border-indigo-500/50 font-semibold'
                  : 'bg-slate-800/60 text-slate-500 border-slate-700/60'
              }`}
            >
              <span className="w-1.5 h-1.5 sm:w-2 sm:h-2 rounded-full bg-indigo-400" />
              <span>200 DMA</span>
            </button>
          </div>

          {/* Timeframe selector */}
          <div className="bg-slate-800/80 p-0.5 rounded-xl border border-slate-700 flex text-xs">
            {(['1M', '3M', '6M', '1Y'] as const).map((tf) => (
              <button
                key={tf}
                onClick={() => setTimeframe(tf)}
                className={`px-2.5 sm:px-3 py-1 rounded-lg font-medium transition-all text-[11px] sm:text-xs ${
                  timeframe === tf
                    ? 'bg-emerald-500 text-slate-950 font-bold'
                    : 'text-slate-400 hover:text-white'
                }`}
              >
                {tf}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Primary Price & Moving Averages Chart */}
      <div className="h-64 sm:h-72 w-full" style={{ touchAction: 'pan-y' }}>
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={filteredData} margin={{ top: 10, right: 10, left: -15, bottom: 0 }}>
            <defs>
              <linearGradient id="priceGradient" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#10b981" stopOpacity={0.35} />
                <stop offset="95%" stopColor="#10b981" stopOpacity={0.0} />
              </linearGradient>
            </defs>
            <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
            <XAxis
              dataKey="date"
              stroke="#64748b"
              fontSize={11}
              tickLine={false}
              tickFormatter={(str) => {
                const parts = str.split('-');
                return parts.length >= 3 ? `${parts[2]}/${parts[1]}` : str;
              }}
            />
            <YAxis
              domain={[minPrice, maxPrice]}
              stroke="#64748b"
              fontSize={11}
              tickLine={false}
              axisLine={false}
              tickFormatter={(val) => `₹${val}`}
            />
            <Tooltip
              contentStyle={{
                backgroundColor: '#0f172a',
                borderColor: '#334155',
                borderRadius: '1rem',
                fontSize: '12px',
                boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.5)',
              }}
              formatter={(val: any, name: any) => {
                if (val === null || val === undefined) return ['N/A', name];
                const label = name === 'close' ? 'Price' : name === 'sma_50' ? '50 DMA' : '200 DMA';
                return [`₹${Number(val).toFixed(2)}`, label];
              }}
              labelFormatter={(label) => `Date: ${label}`}
            />
            
            {/* Intrinsic Fair Value Benchmark Reference Line */}
            {valuation.fair_value && (
              <ReferenceLine
                y={valuation.fair_value}
                stroke="#38bdf8"
                strokeDasharray="4 4"
                label={{
                  value: `Fair Value: ₹${valuation.fair_value}`,
                  fill: '#38bdf8',
                  fontSize: 10,
                  position: 'insideTopRight',
                }}
              />
            )}

            {/* Price Area */}
            <Area
              type="monotone"
              dataKey="close"
              stroke="#10b981"
              strokeWidth={2}
              fillOpacity={1}
              fill="url(#priceGradient)"
              name="close"
            />

            {/* 50 DMA */}
            {showSMA50 && (
              <Line
                type="monotone"
                dataKey="sma_50"
                stroke="#f59e0b"
                strokeWidth={1.8}
                dot={false}
                strokeDasharray="3 3"
                name="sma_50"
              />
            )}

            {/* 200 DMA */}
            {showSMA200 && (
              <Line
                type="monotone"
                dataKey="sma_200"
                stroke="#818cf8"
                strokeWidth={2}
                dot={false}
                strokeDasharray="4 4"
                name="sma_200"
              />
            )}
          </AreaChart>
        </ResponsiveContainer>
      </div>

      {/* Technical Summary Pills */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 sm:gap-3 pt-2 border-t border-slate-800/80 text-xs">
        <div className="bg-slate-950/60 p-2.5 sm:p-3 rounded-xl border border-slate-800">
          <div className="text-[11px] sm:text-xs text-slate-400">RSI (14-period)</div>
          <div className="text-sm sm:text-base font-bold text-white mt-0.5">
            {valuation.rsi !== null && valuation.rsi !== undefined ? valuation.rsi : 'N/A'}
          </div>
          <div className="text-[10px] sm:text-[11px] font-medium text-slate-500 mt-0.5 truncate">
            {valuation.rsi && valuation.rsi < 35
              ? '🟢 Oversold'
              : valuation.rsi && valuation.rsi > 70
              ? '🔴 Overbought'
              : '🟡 Neutral'}
          </div>
        </div>

        <div className="bg-slate-950/60 p-2.5 sm:p-3 rounded-xl border border-slate-800">
          <div className="text-[11px] sm:text-xs text-slate-400">50 DMA Level</div>
          <div className="text-sm sm:text-base font-bold text-amber-400 mt-0.5">
            {valuation.dma_50 ? `₹${valuation.dma_50.toFixed(2)}` : 'N/A'}
          </div>
          <div className="text-[10px] sm:text-[11px] font-medium text-slate-500 mt-0.5 truncate">
            {valuation.dma_50 && currentPrice >= valuation.dma_50 ? 'Above 50 DMA' : 'Below 50 DMA'}
          </div>
        </div>

        <div className="bg-slate-950/60 p-2.5 sm:p-3 rounded-xl border border-slate-800">
          <div className="text-[11px] sm:text-xs text-slate-400">200 DMA</div>
          <div className="text-sm sm:text-base font-bold text-indigo-400 mt-0.5">
            {valuation.dma_200 ? `₹${valuation.dma_200.toFixed(2)}` : 'N/A'}
          </div>
          <div className="text-[10px] sm:text-[11px] font-medium text-slate-500 mt-0.5 truncate">
            {valuation.dma_200 && currentPrice >= valuation.dma_200 ? 'Bull Trend' : 'Consolidation'}
          </div>
        </div>

        <div className="bg-slate-950/60 p-2.5 sm:p-3 rounded-xl border border-slate-800">
          <div className="text-[11px] sm:text-xs text-slate-400">Timing Score</div>
          <div className="text-sm sm:text-base font-bold text-teal-400 mt-0.5">
            {valuation.technical_score}/100
          </div>
          <div className="text-[10px] sm:text-[11px] font-medium text-slate-500 mt-0.5 truncate">
            {valuation.technical_score >= 60 ? 'Optimal Timing' : valuation.technical_score <= 40 ? 'Cautious Timing' : 'Fair Timing'}
          </div>
        </div>
      </div>
    </div>
  );
};
