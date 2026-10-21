import React, { useState, useEffect } from 'react';
import { Filter, ArrowUpDown, ChevronRight, Loader2, Sparkles, ShieldCheck, AlertTriangle, RefreshCw, AlertCircle } from 'lucide-react';
import type { ScreenerItem } from '../types';
import { CompanyLogo } from './CompanyLogo';
import { API_BASE_URL } from '../config';

interface ScreenerViewProps {
  onSelectStock: (symbol: string) => void;
}

export const ScreenerView: React.FC<ScreenerViewProps> = ({ onSelectStock }) => {
  const [category, setCategory] = useState<string>(() => {
    try {
      return localStorage.getItem('dhakreystock_screener_cat') || 'nifty50';
    } catch {
      return 'nifty50';
    }
  });
  const [verdictFilter, setVerdictFilter] = useState<string>(() => {
    try {
      return localStorage.getItem('dhakreystock_screener_verdict') || 'ALL';
    } catch {
      return 'ALL';
    }
  });

  // Client-side cache: load instantly if available
  const [stocks, setStocks] = useState<ScreenerItem[]>(() => {
    try {
      const cached = sessionStorage.getItem(`dhakreystock_screener_${category}`);
      return cached ? JSON.parse(cached) : [];
    } catch {
      return [];
    }
  });

  const [loading, setLoading] = useState<boolean>(() => {
    try {
      return !sessionStorage.getItem(`dhakreystock_screener_${category}`);
    } catch {
      return true;
    }
  });

  const [isBackgroundRefreshing, setIsBackgroundRefreshing] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [sortBy, setSortBy] = useState<'margin_of_safety' | 'composite_score' | 'current_price'>('margin_of_safety');
  const [sortAsc, setSortAsc] = useState<boolean>(false);

  useEffect(() => {
    try {
      localStorage.setItem('dhakreystock_screener_cat', category);
    } catch (e) {
      console.error(e);
    }

    // Check if we already have this category cached
    try {
      const cached = sessionStorage.getItem(`dhakreystock_screener_${category}`);
      if (cached) {
        setStocks(JSON.parse(cached));
        setLoading(false);
      } else {
        setLoading(true);
      }
    } catch {
      setLoading(true);
    }

    fetchScreener(category);
  }, [category]);

  useEffect(() => {
    try {
      localStorage.setItem('dhakreystock_screener_verdict', verdictFilter);
    } catch (e) {
      console.error(e);
    }
  }, [verdictFilter]);

  const fetchScreener = async (cat: string) => {
    setError(null);
    const hasCachedData = stocks.length > 0;
    if (hasCachedData) {
      setIsBackgroundRefreshing(true);
    } else {
      setLoading(true);
    }

    try {
      const res = await fetch(`${API_BASE_URL}/api/screener?category=${cat}`);
      if (res.ok) {
        const data = await res.json();
        const items = data.stocks || [];
        setStocks(items);
        try {
          sessionStorage.setItem(`dhakreystock_screener_${cat}`, JSON.stringify(items));
        } catch {
          // Ignore storage overflow
        }
      } else {
        throw new Error(`Server returned HTTP ${res.status}`);
      }
    } catch (err: any) {
      console.error('Failed to fetch screener stocks:', err);
      if (stocks.length === 0) {
        setError(err.message || 'Error connecting to screener service.');
      }
    } finally {
      setLoading(false);
      setIsBackgroundRefreshing(false);
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
      <div className="bg-slate-900/90 border border-slate-800 rounded-2xl sm:rounded-3xl p-4 sm:p-6 shadow-xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <h2 className="text-lg sm:text-xl font-extrabold text-white flex items-center gap-2">
              <Sparkles className="w-4 h-4 sm:w-5 sm:h-5 text-emerald-400 shrink-0" />
              <span>NSE & BSE Valuation Screener</span>
            </h2>
            <p className="text-[11px] sm:text-xs text-slate-400 mt-1">
              Screen and rank Indian companies by margin of safety, intrinsic valuation, and technical timing
            </p>
          </div>

          {/* Verdict Filter Buttons */}
          <div className="flex items-center gap-1 bg-slate-950 p-1 rounded-2xl border border-slate-800 text-[11px] sm:text-xs overflow-x-auto scrollbar-none max-w-full">
            {['ALL', 'BEST BUY', 'AT FAIR PRICE', 'CURRENTLY EXPENSIVE'].map((v) => (
              <button
                key={v}
                onClick={() => setVerdictFilter(v)}
                className={`px-2.5 sm:px-3 py-1.5 rounded-xl font-medium transition-all whitespace-nowrap shrink-0 ${
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
        <div className="flex items-center gap-1.5 sm:gap-2 mt-4 sm:mt-5 pt-3 sm:pt-4 border-t border-slate-800/80 overflow-x-auto scrollbar-none text-xs -mx-1 px-1">
          <span className="text-slate-500 font-medium whitespace-nowrap shrink-0 text-[11px] sm:text-xs">Index / Sector:</span>
          {[
            { id: 'nifty50', label: 'Nifty 50' },
            { id: 'next50', label: 'Nifty Next 50' },
            { id: 'midcap', label: 'Midcap Growth' },
            { id: 'tech', label: 'IT & Software' },
            { id: 'banking', label: 'Banking & NBFCs' },
            { id: 'auto', label: 'Automobiles' },
          ].map((cat) => (
            <button
              key={cat.id}
              onClick={() => setCategory(cat.id)}
              className={`px-2.5 sm:px-3 py-1.5 rounded-xl whitespace-nowrap transition-all font-medium text-[11px] sm:text-xs shrink-0 ${
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
      <div className="bg-slate-900/90 border border-slate-800 rounded-2xl sm:rounded-3xl overflow-hidden shadow-xl">
        <div className="px-4 py-2.5 bg-slate-950/60 border-b border-slate-800 text-[10px] text-slate-400 flex items-center justify-between">
          <span className="sm:hidden font-medium text-slate-300">💡 Tap any stock to view full intrinsic & chart analysis</span>
          <span className="hidden sm:inline">Ranked by quantitative margin of safety & composite score</span>
          {isBackgroundRefreshing && (
            <span className="inline-flex items-center gap-1.5 text-emerald-400 font-medium">
              <Loader2 className="w-3 h-3 animate-spin" /> Updating live prices...
            </span>
          )}
        </div>

        {loading ? (
          <div className="p-16 text-center space-y-3">
            <Loader2 className="w-8 h-8 text-emerald-400 animate-spin mx-auto" />
            <p className="text-xs sm:text-sm text-slate-400">
              Running hybrid valuation algorithms for {category} equities...
            </p>
          </div>
        ) : error && sortedStocks.length === 0 ? (
          <div className="p-12 text-center space-y-3">
            <AlertCircle className="w-8 h-8 text-rose-400 mx-auto" />
            <h4 className="text-sm font-bold text-white">Screener Data Unavailable</h4>
            <p className="text-xs text-rose-300 max-w-sm mx-auto">{error}</p>
            <button
              onClick={() => fetchScreener(category)}
              className="mt-2 px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold inline-flex items-center gap-1.5 transition-colors"
            >
              <RefreshCw className="w-3.5 h-3.5" />
              <span>Retry</span>
            </button>
          </div>
        ) : sortedStocks.length === 0 ? (
          <div className="p-16 text-center text-slate-500 text-xs sm:text-sm">
            No stocks found matching the selected verdict filter.
          </div>
        ) : (
          <>
            {/* Mobile View: Clean, uncluttered stock cards focused on primary suggestion */}
            <div className="block sm:hidden divide-y divide-slate-800/80">
              {sortedStocks.map((stock) => {
                const isPos = stock.change_percent >= 0;
                const isMoSPos = stock.margin_of_safety > 0;

                return (
                  <div
                    key={stock.symbol}
                    onClick={() => onSelectStock(stock.symbol)}
                    className="p-3.5 hover:bg-slate-850/60 active:bg-slate-800 transition-colors cursor-pointer group"
                  >
                    {/* Top Row: Company Logo, Name & Current Price */}
                    <div className="flex items-start justify-between gap-2.5">
                      <div className="flex items-start gap-2.5 min-w-0 flex-1">
                        <CompanyLogo
                          name={stock.name}
                          symbol={stock.symbol}
                          size="sm"
                          className="mt-0.5 rounded-lg shrink-0"
                        />
                        <div className="min-w-0 flex-1">
                          <div className="font-bold text-white text-sm group-hover:text-emerald-400 transition-colors truncate">
                            {stock.name}
                          </div>
                          <div className="text-[11px] text-slate-400 flex items-center gap-1.5 mt-0.5">
                            <span className="font-mono text-slate-300 font-semibold">{stock.display_symbol}</span>
                            <span>•</span>
                            <span className="px-1.5 py-0.2 rounded bg-slate-800 text-slate-300 font-bold text-[9px]">
                              {stock.exchange}
                            </span>
                            <span>•</span>
                            <span className="truncate max-w-[120px]">{stock.sector}</span>
                          </div>
                        </div>
                      </div>

                      <div className="text-right shrink-0">
                        <div className="font-extrabold text-white text-sm">
                          ₹{stock.current_price.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                        </div>
                        <div className={`text-[11px] font-bold ${isPos ? 'text-emerald-400' : 'text-rose-400'}`}>
                          {isPos ? '+' : ''}{stock.change_percent.toFixed(2)}%
                        </div>
                      </div>
                    </div>

                    {/* Bottom Row: Primary Suggestion Verdict & Fair Value Target */}
                    <div className="flex items-center justify-between gap-2 mt-2.5 pt-2 border-t border-slate-800/60">
                      <div className="flex items-center gap-2">
                        <span
                          className={`px-2 py-0.5 rounded-lg font-extrabold text-[10px] uppercase tracking-wider ${
                            stock.verdict === 'BEST BUY'
                              ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40'
                              : stock.verdict === 'CURRENTLY EXPENSIVE'
                              ? 'bg-rose-500/20 text-rose-300 border border-rose-500/40'
                              : 'bg-amber-500/20 text-amber-300 border border-amber-500/40'
                          }`}
                        >
                          {stock.verdict}
                        </span>
                        <span className="text-[11px] text-slate-400">
                          Target: <span className="text-white font-semibold">₹{stock.fair_value.toLocaleString('en-IN', { maximumFractionDigits: 0 })}</span>
                        </span>
                      </div>

                      <div className="flex items-center gap-1.5 text-[11px] font-bold">
                        <span
                          className={`px-1.5 py-0.5 rounded text-[10px] ${
                            isMoSPos
                              ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30'
                              : 'bg-rose-500/10 text-rose-400 border border-rose-500/30'
                          }`}
                        >
                          {isMoSPos ? '+' : ''}{stock.margin_of_safety.toFixed(0)}% Margin
                        </span>
                        <ChevronRight className="w-3.5 h-3.5 text-slate-500 group-hover:text-emerald-400 transition-colors" />
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Desktop View: Full Analytical Multi-Column Table */}
            <div className="hidden sm:block overflow-x-auto">
              <table className="w-full text-left text-xs">
                <thead className="bg-slate-950/80 text-slate-400 uppercase text-[10px] tracking-wider border-b border-slate-800 font-semibold">
                  <tr>
                    <th className="py-3.5 px-4 sticky left-0 bg-slate-950 z-20 shadow-[2px_0_5px_rgba(0,0,0,0.3)]">Company</th>
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
                        <td className="py-3.5 px-4 sticky left-0 bg-slate-900 group-hover:bg-slate-850 z-10 shadow-[2px_0_5px_rgba(0,0,0,0.3)]">
                          <div className="flex items-center gap-2.5">
                            <CompanyLogo
                              name={stock.name}
                              symbol={stock.symbol}
                              size="sm"
                              className="rounded-lg shrink-0"
                            />
                            <div>
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
                            </div>
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
          </>
        )}
      </div>
    </div>
  );
};
