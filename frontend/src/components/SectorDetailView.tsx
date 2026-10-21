import React, { useState, useEffect } from 'react';
import {
  ArrowLeft,
  RefreshCw,
  Filter,
  ChevronDown,
  Sparkles,
  TrendingUp,
  TrendingDown,
  SlidersHorizontal,
  X,
  Loader2,
} from 'lucide-react';
import type { SectorStockItem } from '../types';
import { CompanyLogo } from './CompanyLogo';
import { API_BASE_URL } from '../config';

interface SectorDetailViewProps {
  sectorName: string;
  onBack: () => void;
  onSelectStock: (symbol: string) => void;
}

export const SectorDetailView: React.FC<SectorDetailViewProps> = ({
  sectorName,
  onBack,
  onSelectStock,
}) => {
  const [stocks, setStocks] = useState<SectorStockItem[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [isRefreshing, setIsRefreshing] = useState<boolean>(false);

  // Filters matching Groww screenshot
  const [priceChangeFilter, setPriceChangeFilter] = useState<'all' | 'gainers_1' | 'losers_1'>('all');
  const [perf52wFilter, setPerf52wFilter] = useState<'all' | 'high' | 'low'>('all');
  const [rsiFilter, setRsiFilter] = useState<'all' | 'overbought' | 'oversold'>('all');
  const [macdFilter, setMacdFilter] = useState<'all' | 'bullish' | 'bearish'>('all');

  useEffect(() => {
    fetchSectorStocks(false);
  }, [sectorName]);

  const fetchSectorStocks = async (isManualRefresh: boolean = false) => {
    if (isManualRefresh) {
      setIsRefreshing(true);
    } else {
      setLoading(true);
    }

    try {
      const res = await fetch(`${API_BASE_URL}/api/market/sector/${encodeURIComponent(sectorName)}`);
      if (res.ok) {
        const data = await res.json();
        setStocks(data.stocks || []);
      }
    } catch (e) {
      console.error('Failed to load sector stocks', e);
    } finally {
      setLoading(false);
      setIsRefreshing(false);
    }
  };

  const handleClearAll = () => {
    setPriceChangeFilter('all');
    setPerf52wFilter('all');
    setRsiFilter('all');
    setMacdFilter('all');
  };

  // Active filter count
  const activeFilterCount = [
    priceChangeFilter !== 'all',
    perf52wFilter !== 'all',
    rsiFilter !== 'all',
    macdFilter !== 'all',
  ].filter(Boolean).length + 1; // +1 for the Sector itself

  // Filter stocks
  const filteredStocks = stocks.filter((stock) => {
    if (priceChangeFilter === 'gainers_1' && stock.change_percent <= 1.0) return false;
    if (priceChangeFilter === 'losers_1' && stock.change_percent >= -1.0) return false;

    if (perf52wFilter === 'high' && (stock.position_52w_percent ?? 50) < 65) return false;
    if (perf52wFilter === 'low' && (stock.position_52w_percent ?? 50) > 35) return false;

    if (rsiFilter === 'overbought' && (stock.rsi ?? 50) < 65) return false;
    if (rsiFilter === 'oversold' && (stock.rsi ?? 50) > 40) return false;

    if (macdFilter === 'bullish' && stock.macd !== 'Bullish') return false;
    if (macdFilter === 'bearish' && stock.macd !== 'Bearish') return false;

    return true;
  });

  const renderSparkline = (points: number[], isPositive: boolean) => {
    if (!points || points.length < 2) return null;
    const min = Math.min(...points);
    const max = Math.max(...points);
    const range = max - min || 1;
    const width = 64;
    const height = 20;

    const path = points
      .map((val, idx) => {
        const x = (idx / (points.length - 1)) * width;
        const y = height - ((val - min) / range) * (height - 4) - 2;
        return `${idx === 0 ? 'M' : 'L'} ${x.toFixed(1)} ${y.toFixed(1)}`;
      })
      .join(' ');

    return (
      <svg width={width} height={height} className="overflow-visible shrink-0 hidden sm:block">
        <path
          d={path}
          fill="none"
          stroke={isPositive ? '#10b981' : '#f43f5e'}
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </svg>
    );
  };

  return (
    <div className="space-y-5 animate-in fade-in duration-300">
      {/* Top Header: Back button, Title & Refresh */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <button
            onClick={onBack}
            className="p-2 rounded-xl bg-slate-900 border border-slate-800 hover:bg-slate-800 text-slate-300 hover:text-white transition-all shadow-md active:scale-95 cursor-pointer shrink-0"
            title="Back to Explore"
          >
            <ArrowLeft className="w-5 h-5 text-emerald-400" />
          </button>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-xl sm:text-2xl font-extrabold text-white tracking-tight">
                {sectorName}
              </h1>
              <button
                onClick={() => fetchSectorStocks(true)}
                disabled={isRefreshing}
                className="p-1 text-slate-400 hover:text-emerald-400 transition-colors disabled:opacity-50 cursor-pointer"
                title="Refresh Sector Data"
              >
                <RefreshCw className={`w-4 h-4 ${isRefreshing ? 'animate-spin text-emerald-400' : ''}`} />
              </button>
            </div>
            <p className="text-xs text-slate-400 mt-0.5">
              Sector momentum, volume anomalies, and 52-week price performance
            </p>
          </div>
        </div>
      </div>

      {/* Filter Pills Toolbar (Exact Groww Screenshot Layout) */}
      <div className="bg-slate-900/95 border border-slate-800 rounded-2xl p-2.5 sm:p-3 shadow-xl">
        <div className="flex items-center gap-2 overflow-x-auto scrollbar-none text-xs pb-1 sm:pb-0">
          {/* Active Filter Count Button */}
          <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-950 border border-slate-800 text-white font-bold shrink-0">
            <SlidersHorizontal className="w-3.5 h-3.5 text-emerald-400" />
            <span className="w-4 h-4 rounded-full bg-emerald-500 text-slate-950 text-[10px] font-black flex items-center justify-center">
              {activeFilterCount}
            </span>
          </div>

          {/* Filter 1: Price Change */}
          <div className="relative shrink-0">
            <select
              value={priceChangeFilter}
              onChange={(e) => setPriceChangeFilter(e.target.value as any)}
              className={`appearance-none bg-slate-950 border px-3 py-1.5 pr-7 rounded-xl font-medium focus:outline-none cursor-pointer transition-all ${
                priceChangeFilter !== 'all'
                  ? 'border-emerald-500 text-emerald-300 font-bold bg-emerald-950/20'
                  : 'border-slate-800 text-slate-300 hover:text-white'
              }`}
            >
              <option value="all" className="bg-slate-900 text-white">Price change: All</option>
              <option value="gainers_1" className="bg-slate-900 text-white">Price change &gt; 1%</option>
              <option value="losers_1" className="bg-slate-900 text-white">Price change &lt; -1%</option>
            </select>
            <ChevronDown className="w-3.5 h-3.5 text-slate-400 absolute right-2.5 top-1/2 -translate-y-1/2 pointer-events-none" />
          </div>

          {/* Filter 2: 52W Performance */}
          <div className="relative shrink-0">
            <select
              value={perf52wFilter}
              onChange={(e) => setPerf52wFilter(e.target.value as any)}
              className={`appearance-none bg-slate-950 border px-3 py-1.5 pr-7 rounded-xl font-medium focus:outline-none cursor-pointer transition-all ${
                perf52wFilter !== 'all'
                  ? 'border-emerald-500 text-emerald-300 font-bold bg-emerald-950/20'
                  : 'border-slate-800 text-slate-300 hover:text-white'
              }`}
            >
              <option value="all" className="bg-slate-900 text-white">52W Performance</option>
              <option value="high" className="bg-slate-900 text-white">Near 52W High (&gt;65%)</option>
              <option value="low" className="bg-slate-900 text-white">Near 52W Low (&lt;35%)</option>
            </select>
            <ChevronDown className="w-3.5 h-3.5 text-slate-400 absolute right-2.5 top-1/2 -translate-y-1/2 pointer-events-none" />
          </div>

          {/* Filter 3: RSI */}
          <div className="relative shrink-0">
            <select
              value={rsiFilter}
              onChange={(e) => setRsiFilter(e.target.value as any)}
              className={`appearance-none bg-slate-950 border px-3 py-1.5 pr-7 rounded-xl font-medium focus:outline-none cursor-pointer transition-all ${
                rsiFilter !== 'all'
                  ? 'border-emerald-500 text-emerald-300 font-bold bg-emerald-950/20'
                  : 'border-slate-800 text-slate-300 hover:text-white'
              }`}
            >
              <option value="all" className="bg-slate-900 text-white">RSI: All</option>
              <option value="overbought" className="bg-slate-900 text-white">RSI &gt; 65 (Strong)</option>
              <option value="oversold" className="bg-slate-900 text-white">RSI &lt; 40 (Oversold)</option>
            </select>
            <ChevronDown className="w-3.5 h-3.5 text-slate-400 absolute right-2.5 top-1/2 -translate-y-1/2 pointer-events-none" />
          </div>

          {/* Filter 4: MACD */}
          <div className="relative shrink-0">
            <select
              value={macdFilter}
              onChange={(e) => setMacdFilter(e.target.value as any)}
              className={`appearance-none bg-slate-950 border px-3 py-1.5 pr-7 rounded-xl font-medium focus:outline-none cursor-pointer transition-all ${
                macdFilter !== 'all'
                  ? 'border-emerald-500 text-emerald-300 font-bold bg-emerald-950/20'
                  : 'border-slate-800 text-slate-300 hover:text-white'
              }`}
            >
              <option value="all" className="bg-slate-900 text-white">MACD: All</option>
              <option value="bullish" className="bg-slate-900 text-white">Bullish</option>
              <option value="bearish" className="bg-slate-900 text-white">Bearish</option>
            </select>
            <ChevronDown className="w-3.5 h-3.5 text-slate-400 absolute right-2.5 top-1/2 -translate-y-1/2 pointer-events-none" />
          </div>

          {/* Sector Active Chip */}
          <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-950 border border-slate-700 text-slate-200 font-semibold shrink-0">
            <span>Sector (1)</span>
          </div>

          {/* Clear All */}
          {activeFilterCount > 1 && (
            <button
              onClick={handleClearAll}
              className="text-xs font-bold text-slate-400 hover:text-white px-2 py-1 transition-colors shrink-0 cursor-pointer"
            >
              Clear all
            </button>
          )}
        </div>
      </div>

      {/* Stock List Content */}
      {loading ? (
        <div className="py-20 text-center space-y-3">
          <Loader2 className="w-8 h-8 text-emerald-400 animate-spin mx-auto" />
          <p className="text-sm text-slate-400">Loading {sectorName} constituents...</p>
        </div>
      ) : filteredStocks.length === 0 ? (
        <div className="py-16 text-center text-slate-500 bg-slate-900/60 rounded-3xl border border-slate-800 space-y-2">
          <p className="font-semibold text-white">No stocks match the selected filters.</p>
          <button
            onClick={handleClearAll}
            className="text-xs font-bold text-emerald-400 hover:text-emerald-300 underline"
          >
            Reset Filters
          </button>
        </div>
      ) : (
        <div className="bg-slate-900/90 border border-slate-800 rounded-2xl sm:rounded-3xl overflow-hidden shadow-xl">
          {/* Table Header (Exact Groww Column Spec) */}
          <div className="grid grid-cols-12 px-4 py-3.5 bg-slate-950/80 border-b border-slate-800 text-[11px] font-bold uppercase tracking-wider text-slate-400">
            <div className="col-span-5 sm:col-span-3">Company</div>
            <div className="col-span-3 sm:col-span-2 text-right">Market price</div>
            <div className="col-span-4 sm:col-span-2 text-right">1D price change</div>
            <div className="hidden sm:block sm:col-span-2 text-right">Volume</div>
            <div className="hidden md:block md:col-span-1 text-right">1W avg vol</div>
            <div className="hidden lg:block lg:col-span-2 text-center">52W performance</div>
          </div>

          {/* Rows */}
          <div className="divide-y divide-slate-800/80">
            {filteredStocks.map((stock) => {
              const isPos = stock.change >= 0;
              const isVolPos = (stock.vol_diff_percent ?? 0) >= 0;
              const pos52w = stock.position_52w_percent ?? 50;

              return (
                <div
                  key={stock.symbol}
                  onClick={() => onSelectStock(stock.symbol)}
                  className="grid grid-cols-12 items-center px-4 py-3.5 hover:bg-slate-850/60 active:bg-slate-800 transition-colors cursor-pointer group"
                >
                  {/* Company */}
                  <div className="col-span-5 sm:col-span-3 flex items-center gap-2.5 sm:gap-3 min-w-0 pr-2">
                    <CompanyLogo
                      name={stock.name}
                      symbol={stock.symbol}
                      size="sm"
                      className="rounded-lg shrink-0 shadow-sm"
                    />
                    <div className="min-w-0">
                      <div className="font-bold text-white text-xs sm:text-sm group-hover:text-emerald-400 transition-colors truncate">
                        {stock.name}
                      </div>
                      <div className="flex items-center gap-1.5 mt-0.5">
                        {stock.in_news && (
                          <span className="text-[9px] font-bold text-sky-400 bg-sky-950/60 border border-sky-800/60 px-1 rounded">
                            In news
                          </span>
                        )}
                        <span className="text-[10px] text-slate-400 truncate">
                          {stock.symbol.replace('.NS', '')}
                        </span>
                      </div>
                    </div>
                  </div>

                  {/* Market price */}
                  <div className="col-span-3 sm:col-span-2 flex items-center justify-end gap-2">
                    {renderSparkline(stock.sparkline, isPos)}
                    <span className="font-extrabold text-white text-xs sm:text-sm">
                      ₹{stock.current_price.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                    </span>
                  </div>

                  {/* 1D price change */}
                  <div className="col-span-4 sm:col-span-2 text-right">
                    <span className={`font-extrabold text-xs sm:text-sm ${isPos ? 'text-emerald-400' : 'text-rose-400'}`}>
                      {isPos ? '+' : ''}{stock.change.toFixed(2)} ({isPos ? '+' : ''}{stock.change_percent.toFixed(2)}%)
                    </span>
                  </div>

                  {/* Volume */}
                  <div className="hidden sm:block sm:col-span-2 text-right">
                    <span className="font-semibold text-slate-300 text-xs sm:text-sm">
                      {stock.volume_formatted}
                    </span>
                  </div>

                  {/* 1W avg vol diff */}
                  <div className="hidden md:block md:col-span-1 text-right">
                    <span className={`text-xs font-bold ${isVolPos ? 'text-emerald-400' : 'text-rose-400'}`}>
                      {isVolPos ? '+' : ''}{(stock.vol_diff_percent ?? 0).toFixed(1)}%
                    </span>
                  </div>

                  {/* 52W performance slider */}
                  <div className="hidden lg:flex lg:col-span-2 items-center justify-center gap-2 px-3">
                    <span className="text-[10px] font-bold text-slate-500">L</span>
                    <div className="relative w-full h-1 bg-slate-800 rounded-full flex items-center">
                      <div
                        className="absolute w-2 h-2 rounded-full bg-slate-200 border border-slate-900 shadow-md transform -translate-x-1/2"
                        style={{ left: `${pos52w}%` }}
                      />
                    </div>
                    <span className="text-[10px] font-bold text-slate-500">H</span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
};
