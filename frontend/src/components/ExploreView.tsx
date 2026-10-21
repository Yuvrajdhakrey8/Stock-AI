import React, { useState, useEffect } from 'react';
import {
  TrendingUp,
  TrendingDown,
  Sparkles,
  ChevronRight,
  Flame,
  Layers,
  Laptop,
  Fuel,
  Package,
  Building2,
  Car,
  Activity,
  CupSoda,
  Droplet,
  ArrowUpRight,
  ArrowDownRight,
  Loader2,
  Search,
} from 'lucide-react';
import type { MarketExploreData, MostTradedStock, TopMoverStock, TrendingSector } from '../types';
import { CompanyLogo } from './CompanyLogo';
import { API_BASE_URL } from '../config';

interface ExploreViewProps {
  onSelectStock: (symbol: string) => void;
  onExploreSector?: (sectorName: string) => void;
}

// Built-in resilient fallback dataset for instant, zero-delay initial render
const FALLBACK_EXPLORE_DATA: MarketExploreData = {
  most_traded: [
    {
      symbol: 'RELIANCE.NS',
      name: 'Reliance Industries',
      exchange: 'NSE',
      current_price: 1211.20,
      change: 8.10,
      change_percent: 0.67,
      volume: 9482150,
      volume_formatted: '94.82 L',
      sparkline: [1203, 1205, 1208, 1206, 1209, 1211.2],
    },
    {
      symbol: 'TCS.NS',
      name: 'TCS',
      exchange: 'NSE',
      current_price: 2514.40,
      change: 53.50,
      change_percent: 2.17,
      volume: 4215900,
      volume_formatted: '42.15 L',
      sparkline: [2460, 2475, 2490, 2485, 2505, 2514.4],
    },
    {
      symbol: 'HDFCBANK.NS',
      name: 'HDFC Bank',
      exchange: 'NSE',
      current_price: 1715.50,
      change: 19.50,
      change_percent: 1.15,
      volume: 14250000,
      volume_formatted: '1.42 Cr',
      sparkline: [1695, 1702, 1708, 1712, 1710, 1715.5],
    },
    {
      symbol: 'INFY.NS',
      name: 'Infosys',
      exchange: 'NSE',
      current_price: 1160.40,
      change: 29.70,
      change_percent: 2.63,
      volume: 12416176,
      volume_formatted: '1.24 Cr',
      sparkline: [1130, 1138, 1145, 1142, 1155, 1160.4],
    },
    {
      symbol: 'ETERNAL.NS',
      name: 'Zomato',
      exchange: 'NSE',
      current_price: 245.00,
      change: 4.30,
      change_percent: 1.78,
      volume: 38450120,
      volume_formatted: '3.84 Cr',
      sparkline: [240, 241, 242.5, 243.8, 244.2, 245.0],
    },
    {
      symbol: 'TATAMOTORS.NS',
      name: 'Tata Motors',
      exchange: 'NSE',
      current_price: 925.00,
      change: 16.30,
      change_percent: 1.80,
      volume: 16580900,
      volume_formatted: '1.65 Cr',
      sparkline: [908, 912, 918, 915, 922, 925.0],
    },
    {
      symbol: 'SBIN.NS',
      name: 'State Bank of India',
      exchange: 'NSE',
      current_price: 785.00,
      change: 5.45,
      change_percent: 0.70,
      volume: 18920400,
      volume_formatted: '1.89 Cr',
      sparkline: [779, 781, 783, 782, 784, 785.0],
    },
    {
      symbol: 'ICICIBANK.NS',
      name: 'ICICI Bank',
      exchange: 'NSE',
      current_price: 1245.00,
      change: 11.70,
      change_percent: 0.95,
      volume: 11400200,
      volume_formatted: '1.14 Cr',
      sparkline: [1233, 1238, 1240, 1242, 1241, 1245.0],
    },
    {
      symbol: 'LT.NS',
      name: 'L&T',
      exchange: 'NSE',
      current_price: 3450.00,
      change: 37.50,
      change_percent: 1.10,
      volume: 3120400,
      volume_formatted: '31.20 L',
      sparkline: [3412, 3425, 3438, 3432, 3445, 3450.0],
    },
    {
      symbol: 'MUTHOOTFIN.NS',
      name: 'Muthoot Finance',
      exchange: 'NSE',
      current_price: 1945.00,
      change: 24.10,
      change_percent: 1.25,
      volume: 2180400,
      volume_formatted: '21.80 L',
      sparkline: [1920, 1928, 1935, 1932, 1940, 1945.0],
    },
    {
      symbol: 'HAL.NS',
      name: 'Hindustan Aeronautics',
      exchange: 'NSE',
      current_price: 4280.00,
      change: 63.20,
      change_percent: 1.50,
      volume: 2540100,
      volume_formatted: '25.40 L',
      sparkline: [4215, 4235, 4250, 4260, 4272, 4280.0],
    },
    {
      symbol: 'BHARTIARTL.NS',
      name: 'Bharti Airtel',
      exchange: 'NSE',
      current_price: 1650.00,
      change: 22.80,
      change_percent: 1.40,
      volume: 6890300,
      volume_formatted: '68.90 L',
      sparkline: [1627, 1635, 1642, 1638, 1645, 1650.0],
    },
  ],
  top_movers: {
    gainers: [
      {
        symbol: 'WIPRO.NS',
        name: 'Wipro',
        exchange: 'NSE',
        current_price: 188.98,
        change: 6.84,
        change_percent: 3.76,
        volume: 27561408,
        volume_formatted: '2,75,61,408',
        sparkline: [182.1, 183.5, 185.0, 184.2, 187.1, 188.98],
      },
      {
        symbol: 'INFY.NS',
        name: 'Infosys',
        exchange: 'NSE',
        current_price: 1160.40,
        change: 29.70,
        change_percent: 2.63,
        volume: 12416176,
        volume_formatted: '1,24,16,176',
        sparkline: [1130, 1138, 1145, 1142, 1155, 1160.4],
      },
      {
        symbol: 'TCS.NS',
        name: 'TCS',
        exchange: 'NSE',
        current_price: 2514.40,
        change: 53.50,
        change_percent: 2.17,
        volume: 4215900,
        volume_formatted: '42,15,900',
        sparkline: [2460, 2475, 2490, 2485, 2505, 2514.4],
      },
      {
        symbol: 'TECHM.NS',
        name: 'Tech Mahindra',
        exchange: 'NSE',
        current_price: 1828.90,
        change: 49.80,
        change_percent: 2.80,
        volume: 3720726,
        volume_formatted: '37,20,726',
        sparkline: [1779, 1795, 1810, 1805, 1822, 1828.9],
      },
      {
        symbol: 'ULTRACEMCO.NS',
        name: 'UltraTech Cement',
        exchange: 'NSE',
        current_price: 10814.00,
        change: 164.00,
        change_percent: 1.54,
        volume: 250828,
        volume_formatted: '2,50,828',
        sparkline: [10650, 10690, 10740, 10710, 10780, 10814],
      },
      {
        symbol: 'HCLTECH.NS',
        name: 'HCL Technologies',
        exchange: 'NSE',
        current_price: 1402.50,
        change: 22.60,
        change_percent: 1.64,
        volume: 2749617,
        volume_formatted: '27,49,617',
        sparkline: [1379, 1388, 1395, 1390, 1400, 1402.5],
      },
    ],
    losers: [
      {
        symbol: 'INDUSINDBK.NS',
        name: 'IndusInd Bank',
        exchange: 'NSE',
        current_price: 1040.00,
        change: -15.80,
        change_percent: -1.50,
        volume: 4821900,
        volume_formatted: '48,21,900',
        sparkline: [1055, 1052, 1048, 1049, 1044, 1040.0],
      },
      {
        symbol: 'TITAN.NS',
        name: 'Titan Company',
        exchange: 'NSE',
        current_price: 3420.00,
        change: -38.00,
        change_percent: -1.10,
        volume: 1250400,
        volume_formatted: '12,50,400',
        sparkline: [3458, 3445, 3435, 3440, 3428, 3420.0],
      },
      {
        symbol: 'HINDUNILVR.NS',
        name: 'Hindustan Unilever',
        exchange: 'NSE',
        current_price: 2380.00,
        change: -19.20,
        change_percent: -0.80,
        volume: 2180400,
        volume_formatted: '21,80,400',
        sparkline: [2399, 2392, 2388, 2390, 2384, 2380.0],
      },
      {
        symbol: 'ASIANPAINT.NS',
        name: 'Asian Paints',
        exchange: 'NSE',
        current_price: 2450.00,
        change: -17.20,
        change_percent: -0.70,
        volume: 1840200,
        volume_formatted: '18,40,200',
        sparkline: [2467, 2460, 2455, 2458, 2452, 2450.0],
      },
      {
        symbol: 'BRITANNIA.NS',
        name: 'Britannia Industries',
        exchange: 'NSE',
        current_price: 4950.00,
        change: -29.90,
        change_percent: -0.60,
        volume: 845200,
        volume_formatted: '8,45,200',
        sparkline: [4979, 4970, 4962, 4965, 4956, 4950.0],
      },
      {
        symbol: 'NESTLEIND.NS',
        name: 'Nestle India',
        exchange: 'NSE',
        current_price: 2250.00,
        change: -9.00,
        change_percent: -0.40,
        volume: 620400,
        volume_formatted: '6,20,400',
        sparkline: [2259, 2255, 2252, 2254, 2251, 2250.0],
      },
    ],
    volume_shockers: [
      {
        symbol: 'WIPRO.NS',
        name: 'Wipro',
        exchange: 'NSE',
        current_price: 188.98,
        change: 6.84,
        change_percent: 3.76,
        volume: 27561408,
        volume_formatted: '2,75,61,408',
        sparkline: [182.1, 183.5, 185.0, 184.2, 187.1, 188.98],
      },
      {
        symbol: 'ETERNAL.NS',
        name: 'Zomato',
        exchange: 'NSE',
        current_price: 245.00,
        change: 4.30,
        change_percent: 1.78,
        volume: 38450120,
        volume_formatted: '3,84,50,120',
        sparkline: [240, 241, 242.5, 243.8, 244.2, 245.0],
      },
      {
        symbol: 'SBIN.NS',
        name: 'State Bank of India',
        exchange: 'NSE',
        current_price: 785.00,
        change: 5.45,
        change_percent: 0.70,
        volume: 18920400,
        volume_formatted: '1,89,20,400',
        sparkline: [779, 781, 783, 782, 784, 785.0],
      },
      {
        symbol: 'TATAMOTORS.NS',
        name: 'Tata Motors',
        exchange: 'NSE',
        current_price: 925.00,
        change: 16.30,
        change_percent: 1.80,
        volume: 16580900,
        volume_formatted: '1,65,80,900',
        sparkline: [908, 912, 918, 915, 922, 925.0],
      },
      {
        symbol: 'INFY.NS',
        name: 'Infosys',
        exchange: 'NSE',
        current_price: 1160.40,
        change: 29.70,
        change_percent: 2.63,
        volume: 12416176,
        volume_formatted: '1,24,16,176',
        sparkline: [1130, 1138, 1145, 1142, 1155, 1160.4],
      },
      {
        symbol: 'HDFCBANK.NS',
        name: 'HDFC Bank',
        exchange: 'NSE',
        current_price: 1715.50,
        change: 19.50,
        change_percent: 1.15,
        volume: 14250000,
        volume_formatted: '1,42,50,000',
        sparkline: [1695, 1702, 1708, 1712, 1710, 1715.5],
      },
    ],
  },
  trending_sectors: [
    {
      id: 'it',
      name: 'Information Technology',
      icon: 'laptop',
      gainers: 84,
      losers: 141,
      change_percent: 1.79,
    },
    {
      id: 'oil',
      name: 'Oil',
      icon: 'fuel',
      gainers: 5,
      losers: 26,
      change_percent: 1.00,
    },
    {
      id: 'cement',
      name: 'Cement',
      icon: 'package',
      gainers: 13,
      losers: 22,
      change_percent: 0.81,
    },
    {
      id: 'banking',
      name: 'Banking & Financial Services',
      icon: 'building',
      gainers: 46,
      losers: 38,
      change_percent: 0.72,
    },
    {
      id: 'auto',
      name: 'Automobiles',
      icon: 'car',
      gainers: 32,
      losers: 19,
      change_percent: 0.65,
    },
    {
      id: 'pharma',
      name: 'Healthcare & Pharma',
      icon: 'activity',
      gainers: 28,
      losers: 24,
      change_percent: 0.40,
    },
    {
      id: 'plastics',
      name: 'Plastic and Polymers',
      icon: 'cup',
      gainers: 8,
      losers: 31,
      change_percent: -3.09,
    },
    {
      id: 'textiles',
      name: 'Textiles',
      icon: 'layers',
      gainers: 83,
      losers: 144,
      change_percent: -3.11,
    },
    {
      id: 'water',
      name: 'Water Distribution',
      icon: 'droplet',
      gainers: 0,
      losers: 8,
      change_percent: -3.38,
    },
  ],
};

export const ExploreView: React.FC<ExploreViewProps> = ({
  onSelectStock,
  onExploreSector,
}) => {
  const [data, setData] = useState<MarketExploreData>(FALLBACK_EXPLORE_DATA);
  const [loading, setLoading] = useState<boolean>(false);
  const [showAllTraded, setShowAllTraded] = useState<boolean>(false);
  const [moverTab, setMoverTab] = useState<'gainers' | 'losers' | 'volume_shockers'>('gainers');
  const [indexFilter, setIndexFilter] = useState<string>('NIFTY 100');
  const [showAllMovers, setShowAllMovers] = useState<boolean>(false);
  const [showAllSectors, setShowAllSectors] = useState<boolean>(false);

  useEffect(() => {
    fetchExploreData();
  }, []);

  const fetchExploreData = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/market/explore`);
      if (res.ok) {
        const json = await res.json();
        setData(json);
      }
    } catch {
      // Keep resilient fallback
    }
  };

  const renderSparkline = (points: number[], isPositive: boolean) => {
    if (!points || points.length < 2) return null;
    const min = Math.min(...points);
    const max = Math.max(...points);
    const range = max - min || 1;
    const width = 72;
    const height = 22;

    const path = points
      .map((val, idx) => {
        const x = (idx / (points.length - 1)) * width;
        const y = height - ((val - min) / range) * (height - 6) - 3;
        return `${idx === 0 ? 'M' : 'L'} ${x.toFixed(1)} ${y.toFixed(1)}`;
      })
      .join(' ');

    return (
      <svg width={width} height={height} className="overflow-visible shrink-0 hidden sm:block">
        <path
          d={path}
          fill="none"
          stroke={isPositive ? '#10b981' : '#f43f5e'}
          strokeWidth="1.75"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </svg>
    );
  };

  const renderSectorIcon = (icon?: string) => {
    switch (icon) {
      case 'laptop':
        return <Laptop className="w-4 h-4 text-slate-300" />;
      case 'fuel':
        return <Fuel className="w-4 h-4 text-slate-300" />;
      case 'package':
        return <Package className="w-4 h-4 text-slate-300" />;
      case 'building':
        return <Building2 className="w-4 h-4 text-slate-300" />;
      case 'car':
        return <Car className="w-4 h-4 text-slate-300" />;
      case 'activity':
        return <Activity className="w-4 h-4 text-slate-300" />;
      case 'cup':
        return <CupSoda className="w-4 h-4 text-slate-300" />;
      case 'layers':
        return <Layers className="w-4 h-4 text-slate-300" />;
      case 'droplet':
        return <Droplet className="w-4 h-4 text-slate-300" />;
      default:
        return <Layers className="w-4 h-4 text-slate-300" />;
    }
  };

  const displayedTraded = showAllTraded ? data.most_traded : data.most_traded.slice(0, 4);
  const activeMoversList = data.top_movers[moverTab] || [];
  const displayedMovers = showAllMovers ? activeMoversList : activeMoversList.slice(0, 6);
  const displayedSectors = showAllSectors ? data.trending_sectors : data.trending_sectors.slice(0, 6);

  return (
    <div className="space-y-7 animate-in fade-in duration-300">
      {/* 1. SECTION: Most Traded Stocks (Groww style cards) */}
      <section className="space-y-3">
        <div className="flex items-center justify-between">
          <h2 className="text-lg sm:text-xl font-extrabold text-white tracking-tight flex items-center gap-2">
            <span>Most traded stocks</span>
          </h2>
          <button
            onClick={() => setShowAllTraded(!showAllTraded)}
            className="text-xs font-bold text-emerald-400 hover:text-emerald-300 flex items-center gap-1 transition-colors cursor-pointer"
          >
            <span>{showAllTraded ? 'Show less' : 'See more'}</span>
            <ChevronRight className="w-3.5 h-3.5" />
          </button>
        </div>

        {/* Horizontal Scroll on Mobile / Responsive Grid on Desktop */}
        <div className="grid grid-cols-2 sm:grid-cols-2 md:grid-cols-4 gap-3">
          {displayedTraded.map((item) => {
            const isPos = item.change >= 0;
            return (
              <div
                key={item.symbol}
                onClick={() => onSelectStock(item.symbol)}
                className="bg-slate-900/90 border border-slate-800 hover:border-slate-700 rounded-2xl p-3.5 sm:p-4 transition-all cursor-pointer shadow-lg group active:scale-[0.98] flex flex-col justify-between"
              >
                <div>
                  <CompanyLogo
                    name={item.name}
                    symbol={item.symbol}
                    size="md"
                    className="rounded-xl shadow-md"
                  />
                  <div className="mt-3">
                    <h3 className="font-bold text-white text-xs sm:text-sm group-hover:text-emerald-400 transition-colors line-clamp-1">
                      {item.name}
                    </h3>
                  </div>
                </div>

                <div className="mt-3 pt-2.5 border-t border-slate-800/80">
                  <div className="font-extrabold text-white text-sm">
                    ₹{item.current_price.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                  </div>
                  <div className={`text-xs font-semibold mt-0.5 ${isPos ? 'text-emerald-400' : 'text-rose-400'}`}>
                    {isPos ? '+' : ''}{item.change.toFixed(2)} ({isPos ? '+' : ''}{item.change_percent.toFixed(2)}%)
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {/* 2. SECTION: Top Movers Today (Groww style table with Gainers, Losers, Volume shockers) */}
      <section className="space-y-3">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5">
          <h2 className="text-lg sm:text-xl font-extrabold text-white tracking-tight">
            Top movers today
          </h2>

          <div className="flex items-center gap-2 flex-wrap">
            {/* Filter Pills */}
            <div className="bg-slate-900/90 p-1 rounded-xl border border-slate-800 flex items-center gap-1 text-xs">
              <button
                onClick={() => setMoverTab('gainers')}
                className={`px-3 py-1.5 rounded-lg font-bold transition-all text-xs cursor-pointer ${
                  moverTab === 'gainers'
                    ? 'bg-slate-800 text-white shadow-sm ring-1 ring-slate-700'
                    : 'text-slate-400 hover:text-white'
                }`}
              >
                Gainers
              </button>
              <button
                onClick={() => setMoverTab('losers')}
                className={`px-3 py-1.5 rounded-lg font-bold transition-all text-xs cursor-pointer ${
                  moverTab === 'losers'
                    ? 'bg-slate-800 text-white shadow-sm ring-1 ring-slate-700'
                    : 'text-slate-400 hover:text-white'
                }`}
              >
                Losers
              </button>
              <button
                onClick={() => setMoverTab('volume_shockers')}
                className={`px-3 py-1.5 rounded-lg font-bold transition-all text-xs cursor-pointer ${
                  moverTab === 'volume_shockers'
                    ? 'bg-slate-800 text-white shadow-sm ring-1 ring-slate-700'
                    : 'text-slate-400 hover:text-white'
                }`}
              >
                Volume shockers
              </button>
            </div>

            {/* Index Filter Dropdown */}
            <div className="bg-slate-900/90 border border-slate-800 rounded-xl px-2.5 py-1.5 text-xs text-slate-300">
              <select
                value={indexFilter}
                onChange={(e) => setIndexFilter(e.target.value)}
                className="bg-transparent font-semibold text-white focus:outline-none cursor-pointer"
              >
                <option value="NIFTY 100" className="bg-slate-900 text-white">NIFTY 100</option>
                <option value="NIFTY 50" className="bg-slate-900 text-white">NIFTY 50</option>
                <option value="ALL" className="bg-slate-900 text-white">All Equities</option>
              </select>
            </div>
          </div>
        </div>

        {/* Movers Table (Groww layout) */}
        <div className="bg-slate-900/90 border border-slate-800 rounded-2xl overflow-hidden shadow-xl">
          <div className="grid grid-cols-12 px-4 py-3 bg-slate-950/80 border-b border-slate-800 text-[11px] font-bold uppercase tracking-wider text-slate-400">
            <div className="col-span-6 sm:col-span-5">Company</div>
            <div className="col-span-4 sm:col-span-4 text-right sm:text-center">Market price (1D)</div>
            <div className="col-span-2 sm:col-span-3 text-right">Volume</div>
          </div>

          <div className="divide-y divide-slate-800/80">
            {displayedMovers.map((stock) => {
              const isPos = stock.change >= 0;
              return (
                <div
                  key={stock.symbol}
                  onClick={() => onSelectStock(stock.symbol)}
                  className="grid grid-cols-12 items-center px-4 py-3 hover:bg-slate-850/60 active:bg-slate-800 transition-colors cursor-pointer group"
                >
                  {/* Company */}
                  <div className="col-span-6 sm:col-span-5 flex items-center gap-2.5 sm:gap-3 min-w-0 pr-2">
                    <CompanyLogo
                      name={stock.name}
                      symbol={stock.symbol}
                      size="sm"
                      className="rounded-lg shrink-0"
                    />
                    <div className="min-w-0">
                      <div className="font-bold text-white text-xs sm:text-sm group-hover:text-emerald-400 transition-colors truncate">
                        {stock.name}
                      </div>
                      <div className="text-[10px] text-slate-400 mt-0.5 truncate hidden sm:block">
                        {stock.exchange} • {stock.symbol.replace('.NS', '')}
                      </div>
                    </div>
                  </div>

                  {/* Market price (1D) with mini sparkline chart */}
                  <div className="col-span-4 sm:col-span-4 flex items-center justify-end sm:justify-center gap-3">
                    {renderSparkline(stock.sparkline, isPos)}
                    <div className="text-right">
                      <div className="font-extrabold text-white text-xs sm:text-sm">
                        ₹{stock.current_price.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                      </div>
                      <div className={`text-[11px] font-bold ${isPos ? 'text-emerald-400' : 'text-rose-400'}`}>
                        {isPos ? '+' : ''}{stock.change.toFixed(2)} ({isPos ? '+' : ''}{stock.change_percent.toFixed(2)}%)
                      </div>
                    </div>
                  </div>

                  {/* Volume */}
                  <div className="col-span-2 sm:col-span-3 text-right">
                    <span className="font-semibold text-slate-300 text-xs sm:text-sm">
                      {stock.volume_formatted}
                    </span>
                  </div>
                </div>
              );
            })}
          </div>

          <div className="p-3 bg-slate-950/60 border-t border-slate-800 text-center">
            <button
              onClick={() => setShowAllMovers(!showAllMovers)}
              className="text-xs font-bold text-emerald-400 hover:text-emerald-300 inline-flex items-center gap-1 transition-colors cursor-pointer"
            >
              <span>{showAllMovers ? 'Show less' : 'See more'}</span>
              <ChevronRight className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>
      </section>

      {/* 3. SECTION: Sectors Trending Today (Groww visual split progress bar) */}
      <section className="space-y-3">
        <div className="flex items-center justify-between">
          <h2 className="text-lg sm:text-xl font-extrabold text-white tracking-tight">
            Sectors trending today
          </h2>
          <button
            onClick={() => setShowAllSectors(!showAllSectors)}
            className="text-xs font-bold text-emerald-400 hover:text-emerald-300 flex items-center gap-1 transition-colors cursor-pointer"
          >
            <span>{showAllSectors ? 'Show less' : 'See all sectors'}</span>
            <ChevronRight className="w-3.5 h-3.5" />
          </button>
        </div>

        <div className="bg-slate-900/90 border border-slate-800 rounded-2xl overflow-hidden shadow-xl">
          <div className="grid grid-cols-12 px-4 py-3 bg-slate-950/80 border-b border-slate-800 text-[11px] font-bold uppercase tracking-wider text-slate-400">
            <div className="col-span-5 sm:col-span-5">Sector</div>
            <div className="col-span-4 sm:col-span-4 text-center">Gainers / Losers</div>
            <div className="col-span-3 sm:col-span-3 text-right">1D price change</div>
          </div>

          <div className="divide-y divide-slate-800/80">
            {displayedSectors.map((sector) => {
              const isPos = sector.change_percent >= 0;
              const total = sector.gainers + sector.losers || 1;
              const gainerPct = Math.round((sector.gainers / total) * 100);

              return (
                <div
                  key={sector.id}
                  onClick={() => onExploreSector && onExploreSector(sector.name)}
                  className="grid grid-cols-12 items-center px-4 py-3.5 hover:bg-slate-850/60 active:bg-slate-800 transition-colors cursor-pointer group"
                >
                  {/* Sector Icon & Name */}
                  <div className="col-span-5 sm:col-span-5 flex items-center gap-2.5 min-w-0 pr-2">
                    <div className="w-8 h-8 rounded-xl bg-slate-800 border border-slate-700/80 flex items-center justify-center shrink-0 shadow-sm">
                      {renderSectorIcon(sector.icon)}
                    </div>
                    <span className="font-bold text-white text-xs sm:text-sm group-hover:text-emerald-400 transition-colors truncate">
                      {sector.name}
                    </span>
                  </div>

                  {/* Gainers / Losers Split Bar (Groww Image 2 design) */}
                  <div className="col-span-4 sm:col-span-4 px-2">
                    <div className="flex items-center justify-between text-[11px] font-bold mb-1">
                      <span className="text-emerald-400">{sector.gainers}</span>
                      <span className="text-orange-400">{sector.losers}</span>
                    </div>
                    {/* Visual Two-Tone Progress Bar */}
                    <div className="w-full h-1.5 rounded-full bg-slate-800 overflow-hidden flex">
                      <div
                        className="h-full bg-emerald-400 transition-all duration-500"
                        style={{ width: `${gainerPct}%` }}
                      />
                      <div
                        className="h-full bg-orange-500 transition-all duration-500"
                        style={{ width: `${100 - gainerPct}%` }}
                      />
                    </div>
                  </div>

                  {/* 1D Price Change */}
                  <div className="col-span-3 sm:col-span-3 text-right">
                    <span
                      className={`font-extrabold text-xs sm:text-sm ${
                        isPos ? 'text-emerald-400' : 'text-rose-400'
                      }`}
                    >
                      {isPos ? '+' : ''}{sector.change_percent.toFixed(2)}%
                    </span>
                  </div>
                </div>
              );
            })}
          </div>

          <div className="p-3 bg-slate-950/60 border-t border-slate-800 text-center">
            <button
              onClick={() => setShowAllSectors(!showAllSectors)}
              className="text-xs font-bold text-emerald-400 hover:text-emerald-300 inline-flex items-center gap-1 transition-colors cursor-pointer"
            >
              <span>{showAllSectors ? 'Show less' : 'See all sectors'}</span>
              <ChevronRight className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>
      </section>
    </div>
  );
};
