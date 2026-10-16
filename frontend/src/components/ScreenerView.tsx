import React, { useState, useEffect } from 'react';
import { Filter, ArrowUpDown, ChevronRight, Loader2, Sparkles, ShieldCheck, AlertTriangle } from 'lucide-react';
import type { ScreenerItem } from '../types';

interface ScreenerViewProps {
  onSelectStock: (symbol: string) => void;
}

export const ScreenerView: React.FC<ScreenerViewProps> = ({ onSelectStock }) => {
  const [category, setCategory] = useState<string>('nifty50');
  const [verdictFilter, setVerdictFilter] = useState<string>('ALL');
  const [stocks, setStocks] = useState<ScreenerItem[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [sortBy, setSortBy] = useState<'margin_of_safety' | 'composite_score' | 'current_price'>('margin_of_safety');
  const [sortAsc, setSortAsc] = useState<boolean>(false);

  useEffect(() => {
    fetchScreener(category);
  }, [category]);

  const fetchScreener = async (cat: string) => {
    setLoading(true);
    try {
      const res = await fetch(`/api/screener?category=${cat}`);
      if (res.ok) {
        const data = await res.json();
        setStocks(data.stocks || []);
      }
    } catch (err) {
      console.error('Failed to fetch screener stocks:', err);
    } finally {
      setLoading(false);
    }
  };

  // Filter stocks by verdict
  const filteredStocks = stocks.filter((stock) => {
    if (verdictFilter === 'ALL') return true;
    return stock.verdict === verdictFilter;
  });

  // Sort stocks
  const sortedStocks = [...filteredStocks].sort((a, b) => {
    const valA = a[sortBy] ?? 0;
    const valB = b[sortBy] ?? 0;
    return sortAsc ? valA - valB : valB - valA;
  });

  const handleSort = (field: 'margin_of_safety' | 'composite_score' | 'current_price') => {
    if (sortBy === field) {
      setSortAsc(!sortAsc);
    } else {
      setSortBy(field);
      setSortAsc(false);
    }
  };

  return (
    <div className="space-y-6">
      {/* Screener Controls Header */}
      <div className="bg-slate-900/90 border border-slate-800 rounded-3xl p-6 shadow-xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <h2 className="text-xl font-extrabold text-white flex items-center gap-2">
              <Sparkles className="w-5 h-5 text-emerald-400" />
              <span>NSE & BSE Valuation Screener</span>
            </h2>
            <p className="text-xs text-slate-400 mt-1">
              Screen and rank Indian companies by margin of safety, intrinsic valuation, and technical timing
            </p>
          </div>

          {/* Verdict Filter Buttons */}
          <div className="flex items-center gap-1.5 bg-slate-950 p-1.5 rounded-2xl border border-slate-800 text-xs">
            {['ALL', 'BEST BUY', 'AT FAIR PRICE', 'CURRENTLY EXPENSIVE'].map((v) => (
              <button
                key={v}
                onClick={() => setVerdictFilter(v)}
                className={`px-3 py-1.5 rounded-xl font-medium transition-all ${
                  verdictFilter === v
                    ? v === 'BEST BUY'
                      ? 'bg-emerald-500 text-slate-950 font-bold'
                      : v === 'CURRENTLY EXPENSIVE'
                      ? 'bg-rose-500 text-white font-bold'
                      : 'bg-amber-500 text-slate-950 font-bold'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                {v === 'ALL' ? 'All Stocks' : v}
              </button>
            ))}
          </div>
        </div>

        {/* Category Pills */}
        <div className="flex items-center gap-2 mt-5 pt-4 border-t border-slate-800/80 overflow-x-auto scrollbar-none text-xs">
          <span className="text-slate-500 font-medium">Index / Sector:</span>
          {[
            { id: 'nifty50', label: 'Nifty 50 Bluechips' },
            { id: 'next50', label: 'Nifty Next 50' },
            { id: 'midcap', label: 'Midcap Growth' },
            { id: 'tech', label: 'IT & Software' },
            { id: 'banking', label: 'Banking & NBFCs' },
            { id: 'auto', label: 'Automobiles' },
          ].map((cat) => (
            <button
              key={cat.id}
              onClick={() => setCategory(cat.id)}
              className={`px-3 py-1.5 rounded-xl whitespace-nowrap transition-all font-medium ${
                category === cat.id
                  ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/50 font-semibold'
                  : 'bg-slate-800/60 text-slate-400 border border-slate-700/60 hover:text-white'
              }`}
            >
              {cat.label}
            </button>
          ))}
        </div>
      </div>

      {/* Table Results */}
      <div className="bg-slate-900/90 border border-slate-800 rounded-3xl overflow-hidden shadow-xl">
        {loading ? (
          <div className="p-16 text-center space-y-3">
            <Loader2 className="w-8 h-8 text-emerald-400 animate-spin mx-auto" />
            <p className="text-sm text-slate-400">
              Running hybrid valuation algorithms for {category} equities...
            </p>
          </div>
        ) : sortedStocks.length === 0 ? (
          <div className="p-16 text-center text-slate-500">
            No stocks found matching the selected verdict filter.
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-950/80 text-slate-400 uppercase text-[10px] tracking-wider border-b border-slate-800 font-semibold">
                <tr>
                  <th className="py-3.5 px-4">Company</th>
                  <th className="py-3.5 px-4 cursor-pointer hover:text-white" onClick={() => handleSort('current_price')}>
                    <div className="flex items-center gap-1">
                      <span>Price (₹)</span>
                      <ArrowUpDown className="w-3 h-3" />
                    </div>
                  </th>
                  <th className="py-3.5 px-4">Fair Value (₹)</th>
                  <th className="py-3.5 px-4 cursor-pointer hover:text-white" onClick={() => handleSort('margin_of_safety')}>
                    <div className="flex items-center gap-1">
                      <span>Margin of Safety</span>
                      <ArrowUpDown className="w-3 h-3" />
                    </div>
                  </th>
                  <th className="py-3.5 px-4">Verdict</th>
                  <th className="py-3.5 px-4 cursor-pointer hover:text-white" onClick={() => handleSort('composite_score')}>
                    <div className="flex items-center gap-1">
                      <span>Score</span>
                      <ArrowUpDown className="w-3 h-3" />
                    </div>
                  </th>
                  <th className="py-3.5 px-4">P/E</th>
                  <th className="py-3.5 px-4">ROE</th>
                  <th className="py-3.5 px-4">RSI</th>
                  <th className="py-3.5 px-4 text-right">Action</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/60">
                {sortedStocks.map((stock) => {
                  const isPos = stock.change_percent >= 0;
                  const isMoSPos = stock.margin_of_safety > 0;

                  return (
                    <tr
                      key={stock.symbol}
                      className="hover:bg-slate-800/50 transition-colors cursor-pointer group"
                      onClick={() => onSelectStock(stock.symbol)}
                    >
                      <td className="py-3.5 px-4">
                        <div className="font-semibold text-white group-hover:text-emerald-400 transition-colors text-sm">
                          {stock.name}
                        </div>
                        <div className="text-[11px] text-slate-400 flex items-center gap-1.5 mt-0.5">
                          <span className="font-mono text-slate-300">{stock.display_symbol}</span>
                          <span>•</span>
                          <span className="px-1.5 py-0.2 rounded bg-slate-800 text-slate-300 font-bold text-[9px]">
                            {stock.exchange}
                          </span>
                          <span>•</span>
                          <span className="truncate max-w-[140px]">{stock.sector}</span>
                        </div>
                      </td>

                      <td className="py-3.5 px-4">
                        <div className="font-bold text-white text-sm">
                          ₹{stock.current_price.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                        </div>
                        <div className={`text-[11px] font-medium ${isPos ? 'text-emerald-400' : 'text-rose-400'}`}>
                          {isPos ? '+' : ''}{stock.change_percent.toFixed(2)}%
                        </div>
                      </td>

                      <td className="py-3.5 px-4 font-semibold text-slate-300">
                        ₹{stock.fair_value.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                      </td>

                      <td className="py-3.5 px-4">
                        <span
                          className={`font-bold px-2 py-0.5 rounded text-xs ${
                            isMoSPos
                              ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30'
                              : 'bg-rose-500/10 text-rose-400 border border-rose-500/30'
                          }`}
                        >
                          {isMoSPos ? '+' : ''}{stock.margin_of_safety.toFixed(1)}%
                        </span>
                      </td>

                      <td className="py-3.5 px-4">
                        <span
                          className={`px-2.5 py-1 rounded-xl font-bold text-[11px] uppercase tracking-wider inline-block ${
                            stock.verdict === 'BEST BUY'
                              ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40'
                              : stock.verdict === 'CURRENTLY EXPENSIVE'
                              ? 'bg-rose-500/20 text-rose-300 border border-rose-500/40'
                              : 'bg-amber-500/20 text-amber-300 border border-amber-500/40'
                          }`}
                        >
                          {stock.verdict}
                        </span>
                      </td>

                      <td className="py-3.5 px-4 font-bold text-white">
                        {stock.composite_score}/100
                      </td>

                      <td className="py-3.5 px-4 text-slate-300 font-medium">
                        {stock.pe_ratio ? `${stock.pe_ratio.toFixed(1)}x` : '-'}
                      </td>

                      <td className="py-3.5 px-4 text-slate-300 font-medium">
                        {stock.roe ? `${stock.roe.toFixed(1)}%` : '-'}
                      </td>

                      <td className="py-3.5 px-4">
                        <span
                          className={`font-semibold ${
                            stock.rsi && stock.rsi < 35
                              ? 'text-emerald-400 font-bold'
                              : stock.rsi && stock.rsi > 70
                              ? 'text-rose-400 font-bold'
                              : 'text-slate-300'
                          }`}
                        >
                          {stock.rsi ? stock.rsi.toFixed(0) : '-'}
                        </span>
                      </td>

                      <td className="py-3.5 px-4 text-right">
                        <button
                          onClick={(e) => {
                            e.stopPropagation();
                            onSelectStock(stock.symbol);
                          }}
                          className="px-3 py-1.5 rounded-xl bg-slate-800 text-slate-200 group-hover:bg-emerald-500 group-hover:text-slate-950 font-bold text-xs transition-all inline-flex items-center gap-1 shadow"
                        >
                          <span>Analyze</span>
                          <ChevronRight className="w-3.5 h-3.5" />
                        </button>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};
