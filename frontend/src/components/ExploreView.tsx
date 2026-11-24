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
  Clock,
  X,
  RefreshCw,
} from 'lucide-react';
import type { MarketExploreData, MostTradedStock, TopMoverStock, TrendingSector, RecentSearchItem } from '../types';
import { CompanyLogo } from './CompanyLogo';
import { API_BASE_URL } from '../config';
import { getRecentSearches, removeRecentSearch, clearRecentSearches } from '../utils/recentSearches';

interface ExploreViewProps {
  onSelectStock: (symbol: string) => void;
  onExploreSector?: (sectorName: string) => void;
}

// Built-in resilient fallback dataset for instant, zero-delay initial render
const FALLBACK_EXPLORE_DATA: MarketExploreData = {
  most_traded: [
    {
      symbol: 'TATASTEEL.NS',
      name: 'Tata Steel',
      exchange: 'NSE',
      current_price: 163.00,
      change: -15.00,
      change_percent: -8.43,
      volume: 168843913,
      volume_formatted: '16.88 Cr',
      sparkline: [178, 175, 172, 170, 166, 163.0],
    },
    {
      symbol: 'HDFCBANK.NS',
      name: 'HDFC Bank',
      exchange: 'NSE',
      current_price: 817.80,
      change: -28.20,
      change_percent: -3.33,
      volume: 55628667,
      volume_formatted: '5.56 Cr',
      sparkline: [846, 840, 835, 830, 822, 817.8],
    },
    {
      symbol: 'ITC.NS',
      name: 'ITC',
      exchange: 'NSE',
      current_price: 301.00,
      change: 1.90,
      change_percent: 0.64,
      volume: 27512525,
      volume_formatted: '2.75 Cr',
      sparkline: [299, 298.5, 300, 301.5, 300.8, 301.0],
    },
    {
      symbol: 'ICICIBANK.NS',
      name: 'ICICI Bank',
      exchange: 'NSE',
      current_price: 1585.50,
      change: -54.50,
      change_percent: -3.32,
      volume: 22243169,
      volume_formatted: '2.22 Cr',
      sparkline: [1640, 1630, 1615, 1610, 1595, 1585.5],
    },
    {
      symbol: 'SBIN.NS',
      name: 'State Bank of India',
      exchange: 'NSE',
      current_price: 1132.65,
      change: -32.45,
      change_percent: -2.79,
      volume: 14924743,
      volume_formatted: '1.49 Cr',
      sparkline: [1165, 1158, 1150, 1144, 1138, 1132.65],
    },
    {
      symbol: 'RELIANCE.NS',
      name: 'Reliance Industries',
      exchange: 'NSE',
      current_price: 1351.00,
      change: -26.50,
      change_percent: -1.92,
      volume: 12845010,
      volume_formatted: '1.28 Cr',
      sparkline: [1377.5, 1370, 1365, 1360, 1355, 1351.0],
    },
    {
      symbol: 'INFY.NS',
      name: 'Infosys',
      exchange: 'NSE',
      current_price: 1782.40,
      change: 14.80,
      change_percent: 0.84,
      volume: 11420500,
      volume_formatted: '1.14 Cr',
      sparkline: [1767, 1770, 1775, 1772, 1780, 1782.4],
    },
    {
      symbol: 'TCS.NS',
      name: 'TCS',
      exchange: 'NSE',
      current_price: 2460.00,
      change: 83.80,
      change_percent: 3.53,
      volume: 7386320,
      volume_formatted: '73.86 L',
      sparkline: [2376, 2400, 2420, 2435, 2450, 2460.0],
    },
    {
      symbol: 'SHRIRAMFIN.NS',
      name: 'Shriram Finance',
      exchange: 'NSE',
      current_price: 995.90,
      change: 23.90,
      change_percent: 2.46,
      volume: 9471534,
      volume_formatted: '94.72 L',
      sparkline: [972, 978, 984, 988, 992, 995.9],
    },
    {
      symbol: 'TECHM.NS',
      name: 'Tech Mahindra',
      exchange: 'NSE',
      current_price: 1777.50,
      change: 31.30,
      change_percent: 1.79,
      volume: 3180662,
      volume_formatted: '31.81 L',
      sparkline: [1746, 1755, 1765, 1762, 1772, 1777.5],
    },
    {
      symbol: 'HCLTECH.NS',
      name: 'HCL Technologies',
      exchange: 'NSE',
      current_price: 1364.30,
      change: 19.90,
      change_percent: 1.48,
      volume: 3981800,
      volume_formatted: '39.82 L',
      sparkline: [1344, 1350, 1356, 1352, 1360, 1364.3],
    },
    {
      symbol: 'HINDZINC.NS',
      name: 'Hindustan Zinc',
      exchange: 'NSE',
      current_price: 528.95,
      change: 7.35,
      change_percent: 1.41,
      volume: 4880379,
      volume_formatted: '48.80 L',
      sparkline: [521.6, 523.5, 525.0, 524.2, 527.5, 528.95],
    },
  ],
  top_movers: {
    gainers: [
      {
        symbol: 'TCS.NS',
        name: 'TCS',
        exchange: 'NSE',
        current_price: 2460.00,
        change: 83.80,
        change_percent: 3.53,
        volume: 7386320,
        volume_formatted: '73.86 L',
        sparkline: [2376, 2400, 2420, 2435, 2450, 2460.0],
      },
      {
        symbol: 'SHRIRAMFIN.NS',
        name: 'Shriram Finance',
        exchange: 'NSE',
        current_price: 995.90,
        change: 23.90,
        change_percent: 2.46,
        volume: 9471534,
        volume_formatted: '94.72 L',
        sparkline: [972, 978, 984, 988, 992, 995.9],
      },
      {
        symbol: 'TECHM.NS',
        name: 'Tech Mahindra',
        exchange: 'NSE',
        current_price: 1777.50,
        change: 31.30,
        change_percent: 1.79,
        volume: 3180662,
        volume_formatted: '31.81 L',
        sparkline: [1746, 1755, 1765, 1762, 1772, 1777.5],
      },
      {
        symbol: 'TORNTPHARM.NS',
        name: 'Torrent Pharma',
        exchange: 'NSE',
        current_price: 4763.70,
        change: 74.20,
        change_percent: 1.58,
        volume: 585099,
        volume_formatted: '5.85 L',
        sparkline: [4689, 4710, 4725, 4740, 4755, 4763.7],
      },
      {
        symbol: 'HCLTECH.NS',
        name: 'HCL Technologies',
        exchange: 'NSE',
        current_price: 1364.30,
        change: 19.90,
        change_percent: 1.48,
        volume: 3981800,
        volume_formatted: '39.82 L',
        sparkline: [1344, 1350, 1356, 1352, 1360, 1364.3],
      },
      {
        symbol: 'HINDZINC.NS',
        name: 'Hindustan Zinc',
        exchange: 'NSE',
        current_price: 528.95,
        change: 7.35,
        change_percent: 1.41,
        volume: 4880379,
        volume_formatted: '48.80 L',
        sparkline: [521.6, 523.5, 525.0, 524.2, 527.5, 528.95],
      },
    ],
    losers: [
      {
        symbol: 'TATASTEEL.NS',
        name: 'Tata Steel',
        exchange: 'NSE',
        current_price: 163.00,
        change: -15.00,
        change_percent: -8.43,
        volume: 168843913,
        volume_formatted: '16.88 Cr',
        sparkline: [178, 175, 172, 170, 166, 163.0],
      },
      {
        symbol: 'AXISBANK.NS',
        name: 'Axis Bank',
        exchange: 'NSE',
        current_price: 1388.60,
        change: -57.40,
        change_percent: -3.97,
        volume: 10853616,
        volume_formatted: '1.09 Cr',
        sparkline: [1446, 1435, 1420, 1412, 1398, 1388.6],
      },
      {
        symbol: 'IOC.NS',
        name: 'Indian Oil',
        exchange: 'NSE',
        current_price: 145.00,
        change: -5.50,
        change_percent: -3.65,
        volume: 13240500,
        volume_formatted: '1.32 Cr',
        sparkline: [150.5, 149.2, 148.0, 147.1, 146.0, 145.0],
      },
      {
        symbol: 'HDFCBANK.NS',
        name: 'HDFC Bank',
        exchange: 'NSE',
        current_price: 817.80,
        change: -28.20,
        change_percent: -3.33,
        volume: 55628667,
        volume_formatted: '5.56 Cr',
        sparkline: [846, 840, 835, 830, 822, 817.8],
      },
      {
        symbol: 'ICICIBANK.NS',
        name: 'ICICI Bank',
        exchange: 'NSE',
        current_price: 1585.50,
        change: -54.50,
        change_percent: -3.32,
        volume: 22243169,
        volume_formatted: '2.22 Cr',
        sparkline: [1640, 1630, 1615, 1610, 1595, 1585.5],
      },
      {
        symbol: 'SBIN.NS',
        name: 'State Bank of India',
        exchange: 'NSE',
        current_price: 1132.65,
        change: -32.45,
        change_percent: -2.79,
        volume: 14924743,
        volume_formatted: '1.49 Cr',
        sparkline: [1165, 1158, 1150, 1144, 1138, 1132.65],
      },
    ],
    volume_shockers: [
      {
        symbol: 'TATASTEEL.NS',
        name: 'Tata Steel',
        exchange: 'NSE',
        current_price: 163.00,
        change: -15.00,
        change_percent: -8.43,
        volume: 168843913,
        volume_formatted: '16.88 Cr',
        sparkline: [178, 175, 172, 170, 166, 163.0],
      },
      {
        symbol: 'HDFCBANK.NS',
        name: 'HDFC Bank',
        exchange: 'NSE',
        current_price: 817.80,
        change: -28.20,
        change_percent: -3.33,
        volume: 55628667,
        volume_formatted: '5.56 Cr',
        sparkline: [846, 840, 835, 830, 822, 817.8],
      },
      {
        symbol: 'ITC.NS',
        name: 'ITC',
        exchange: 'NSE',
        current_price: 301.00,
        change: 1.90,
        change_percent: 0.64,
        volume: 27512525,
        volume_formatted: '2.75 Cr',
        sparkline: [299, 298.5, 300, 301.5, 300.8, 301.0],
      },
      {
        symbol: 'ICICIBANK.NS',
        name: 'ICICI Bank',
        exchange: 'NSE',
        current_price: 1585.50,
        change: -54.50,
        change_percent: -3.32,
        volume: 22243169,
        volume_formatted: '2.22 Cr',
        sparkline: [1640, 1630, 1615, 1610, 1595, 1585.5],
      },
      {
        symbol: 'SBIN.NS',
        name: 'State Bank of India',
        exchange: 'NSE',
        current_price: 1132.65,
        change: -32.45,
        change_percent: -2.79,
        volume: 14924743,
        volume_formatted: '1.49 Cr',
        sparkline: [1165, 1158, 1150, 1144, 1138, 1132.65],
      },
      {
        symbol: 'RELIANCE.NS',
        name: 'Reliance Industries',
        exchange: 'NSE',
        current_price: 1351.00,
        change: -26.50,
        change_percent: -1.92,
        volume: 12845010,
        volume_formatted: '1.28 Cr',
        sparkline: [1377.5, 1370, 1365, 1360, 1355, 1351.0],
      },
    ],
  },
  trending_sectors: [
    {
      id: 'it',
      name: 'Information Technology',
      icon: 'laptop',
      gainers: 5,
      losers: 0,
      change_percent: 1.76,
    },
    {
      id: 'pharma',
      name: 'Healthcare & Pharma',
      icon: 'activity',
      gainers: 4,
      losers: 2,
      change_percent: 0.85,
    },
    {
      id: 'fmcg',
      name: 'FMCG & Consumer Goods',
      icon: 'package',
      gainers: 3,
      losers: 3,
      change_percent: 0.12,
    },
    {
      id: 'auto',
      name: 'Automobiles',
      icon: 'car',
      gainers: 2,
      losers: 4,
      change_percent: -0.65,
    },
    {
      id: 'energy',
      name: 'Oil, Gas & Consumable Fuels',
      icon: 'fuel',
      gainers: 1,
      losers: 4,
      change_percent: -1.45,
    },
    {
      id: 'banking',
      name: 'Banking & Financial Services',
      icon: 'building',
      gainers: 2,
      losers: 7,
      change_percent: -2.35,
    },
    {
      id: 'metals',
      name: 'Metals & Mining',
      icon: 'layers',
      gainers: 1,
      losers: 5,
      change_percent: -3.10,
    },
  ],
  popular_picks: [
    {
      symbol: 'RELIANCE.NS',
      name: 'Reliance Industries',
      exchange: 'NSE',
      current_price: 1351.00,
      change: -26.50,
      change_percent: -1.92,
      volume: 12845010,
      volume_formatted: '1.28 Cr',
      sparkline: [1377.5, 1370, 1365, 1360, 1355, 1351.0],
    },
    {
      symbol: 'TCS.NS',
      name: 'TCS',
      exchange: 'NSE',
      current_price: 2460.00,
      change: 83.80,
      change_percent: 3.53,
      volume: 7386320,
      volume_formatted: '73.86 L',
      sparkline: [2376, 2400, 2420, 2435, 2450, 2460.0],
    },
    {
      symbol: 'HDFCBANK.NS',
      name: 'HDFC Bank',
      exchange: 'NSE',
      current_price: 817.80,
      change: -28.20,
      change_percent: -3.33,
      volume: 55628667,
      volume_formatted: '5.56 Cr',
      sparkline: [846, 840, 835, 830, 822, 817.8],
    },
    {
      symbol: 'INFY.NS',
      name: 'Infosys',
      exchange: 'NSE',
      current_price: 1782.40,
      change: 14.80,
      change_percent: 0.84,
      volume: 11420500,
      volume_formatted: '1.14 Cr',
      sparkline: [1767, 1770, 1775, 1772, 1780, 1782.4],
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
      symbol: 'MARUTI.NS',
      name: 'Maruti Suzuki',
      exchange: 'NSE',
      current_price: 11840.00,
      change: 85.00,
      change_percent: 0.72,
      volume: 842100,
      volume_formatted: '8.42 L',
      sparkline: [11755, 11780, 11810, 11795, 11825, 11840.0],
    },
    {
      symbol: 'SBIN.NS',
      name: 'State Bank of India',
      exchange: 'NSE',
      current_price: 1132.65,
      change: -32.45,
      change_percent: -2.79,
      volume: 14924743,
      volume_formatted: '1.49 Cr',
      sparkline: [1165, 1158, 1150, 1144, 1138, 1132.65],
    },
    {
      symbol: 'ITC.NS',
      name: 'ITC',
      exchange: 'NSE',
      current_price: 301.00,
      change: 1.90,
      change_percent: 0.64,
      volume: 27512525,
      volume_formatted: '2.75 Cr',
      sparkline: [299, 298.5, 300, 301.5, 300.8, 301.0],
    },
  ],
};

export const ExploreView: React.FC<ExploreViewProps> = ({
  onSelectStock,
  onExploreSector,
}) => {
  const [data, setData] = useState<MarketExploreData>(FALLBACK_EXPLORE_DATA);
  const [loading, setLoading] = useState<boolean>(false);
  const [refreshing, setRefreshing] = useState<boolean>(false);
  const [showAllTraded, setShowAllTraded] = useState<boolean>(false);
  const [moverTab, setMoverTab] = useState<'gainers' | 'losers' | 'volume_shockers'>('gainers');
  const [indexFilter, setIndexFilter] = useState<string>('NIFTY 100');
  const [showAllMovers, setShowAllMovers] = useState<boolean>(false);
  const [showAllSectors, setShowAllSectors] = useState<boolean>(false);

  // Recent Searches & Related Stocks State
  const [recentSearches, setRecentSearches] = useState<RecentSearchItem[]>(() => getRecentSearches());
  const [relatedStocks, setRelatedStocks] = useState<MostTradedStock[]>([]);
  const [relatedSector, setRelatedSector] = useState<string>('');
  const [relatedLoading, setRelatedLoading] = useState<boolean>(false);

  useEffect(() => {
    fetchExploreData();
    const handleRecentUpdate = () => {
      setRecentSearches(getRecentSearches());
    };
    window.addEventListener('stockly_recent_searches_updated', handleRecentUpdate);
    return () => window.removeEventListener('stockly_recent_searches_updated', handleRecentUpdate);
  }, []);

  // When recent searches change, fetch related stocks for the most recently searched stock
  useEffect(() => {
    if (recentSearches.length > 0) {
      const topRecent = recentSearches[0];
      fetchRelatedStocks(topRecent.symbol);
    } else {
      setRelatedStocks([]);
      setRelatedSector('');
    }
  }, [recentSearches]);

  const fetchExploreData = async (forceRefresh: boolean = false) => {
    try {
      if (forceRefresh) setRefreshing(true);
      const res = await fetch(`${API_BASE_URL}/api/market/explore${forceRefresh ? '?refresh=true' : ''}`);
      if (res.ok) {
        const json = await res.json();
        setData(json);
      }
    } catch {
      // Keep resilient fallback
    } finally {
      setRefreshing(false);
    }
  };

  const fetchRelatedStocks = async (symbol: string) => {
    try {
      setRelatedLoading(true);
      const res = await fetch(`${API_BASE_URL}/api/market/related?symbol=${encodeURIComponent(symbol)}`);
      if (res.ok) {
        const json = await res.json();
        setRelatedStocks(json.related || []);
        setRelatedSector(json.sector || '');
      }
    } catch {
      // Ignore
    } finally {
      setRelatedLoading(false);
    }
  };

  const handleRemoveRecent = (e: React.MouseEvent, symbol: string) => {
    e.stopPropagation();
    const updated = removeRecentSearch(symbol);
    setRecentSearches(updated);
  };

  const handleClearAllRecent = (e: React.MouseEvent) => {
    e.stopPropagation();
    clearRecentSearches();
    setRecentSearches([]);
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
    <div className="space-y-6 sm:space-y-7 animate-in fade-in duration-300">
      {/* Live Market Bar / Quick Status */}
      <div className="flex items-center justify-between pb-2 border-b border-slate-800/80">
        <div className="flex items-center gap-2">
          <span className="w-2 h-2 rounded-full bg-teal-400 animate-pulse" />
          <span className="text-xs font-semibold text-slate-300">
            Live NSE & BSE Markets
          </span>
          {data.last_updated && (
            <span className="text-[11px] text-slate-500 hidden sm:inline">
              • {data.last_updated}
            </span>
          )}
        </div>
        <button
          onClick={() => fetchExploreData(true)}
          disabled={refreshing}
          className="text-xs text-slate-400 hover:text-white flex items-center gap-1.5 transition-colors cursor-pointer disabled:opacity-50"
        >
          <RefreshCw className={`w-3.5 h-3.5 ${refreshing ? 'animate-spin text-teal-400' : ''}`} />
          <span className="hidden sm:inline">{refreshing ? 'Refreshing...' : 'Refresh Live'}</span>
        </button>
      </div>

      {/* 0. SECTION: Recently Searched & Related Picks OR Popular on Stockly */}
      {recentSearches.length > 0 ? (
        <section className="space-y-4">
          {/* Recently Searched Header */}
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <Clock className="w-4 h-4 text-teal-400" />
              <h2 className="text-base sm:text-lg font-extrabold text-white tracking-tight">
                Recently searched
              </h2>
              <span className="text-[11px] px-1.5 py-0.5 rounded-full bg-slate-800 text-slate-400 font-semibold">
                {recentSearches.length}
              </span>
            </div>
            <button
              onClick={handleClearAllRecent}
              className="text-xs font-medium text-slate-400 hover:text-slate-200 transition-colors cursor-pointer"
            >
              Clear history
            </button>
          </div>

          {/* Horizontal scrollable cards for recently searched stocks */}
          <div className="flex items-center gap-2.5 overflow-x-auto scrollbar-none pb-1 -mx-1 px-1">
            {recentSearches.map((item) => {
              const isPos = (item.change_percent ?? 0) >= 0;
              return (
                <div
                  key={item.symbol}
                  onClick={() => onSelectStock(item.symbol)}
                  className="group shrink-0 bg-slate-900/90 border border-slate-800 hover:border-slate-700 rounded-xl p-3 flex items-center gap-3 cursor-pointer transition-all active:scale-[0.98] shadow-sm hover:shadow-md"
                >
                  <CompanyLogo
                    name={item.name}
                    symbol={item.symbol}
                    size="sm"
                    className="rounded-lg shrink-0 shadow"
                  />
                  <div className="min-w-0 pr-1">
                    <div className="text-xs font-bold text-white truncate max-w-[130px] group-hover:text-slate-200">
                      {item.name}
                    </div>
                    <div className="text-[10px] text-slate-400">
                      {item.symbol.replace('.NS', '').replace('.BO', '')}
                    </div>
                  </div>
                  {item.current_price !== undefined && (
                    <div className="text-right pl-2 border-l border-slate-800/80">
                      <div className="text-xs font-extrabold text-white">
                        ₹{item.current_price.toLocaleString('en-IN', { minimumFractionDigits: 1, maximumFractionDigits: 2 })}
                      </div>
                      {item.change_percent !== undefined && (
                        <div className={`text-[10px] font-semibold ${isPos ? 'text-teal-400' : 'text-rose-400'}`}>
                          {isPos ? '+' : ''}{item.change_percent.toFixed(1)}%
                        </div>
                      )}
                    </div>
                  )}
                  <button
                    onClick={(e) => handleRemoveRecent(e, item.symbol)}
                    title="Remove from history"
                    className="text-slate-500 hover:text-slate-300 p-1 rounded-md hover:bg-slate-800 transition-colors cursor-pointer ml-0.5"
                  >
                    <X className="w-3 h-3" />
                  </button>
                </div>
              );
            })}
          </div>

          {/* Related Stocks to the most recently searched stock */}
          {relatedStocks.length > 0 && (
            <div className="bg-slate-900/60 border border-slate-800/90 rounded-2xl p-3.5 sm:p-4 space-y-3">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <Sparkles className="w-4 h-4 text-amber-400" />
                  <span className="text-xs sm:text-sm font-semibold text-slate-200">
                    Related to <span className="text-white font-bold">{recentSearches[0]?.name || recentSearches[0]?.symbol}</span>
                  </span>
                  {relatedSector && (
                    <span className="text-[10px] px-2 py-0.5 rounded-md font-medium bg-slate-800 text-slate-300 hidden sm:inline">
                      {relatedSector}
                    </span>
                  )}
                </div>
                {onExploreSector && relatedSector && (
                  <button
                    onClick={() => onExploreSector(relatedSector)}
                    className="text-xs text-slate-400 hover:text-white flex items-center gap-1 transition-colors cursor-pointer"
                  >
                    <span>View all in sector</span>
                    <ChevronRight className="w-3.5 h-3.5" />
                  </button>
                )}
              </div>

              {/* 4 Related Cards Grid */}
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
                {relatedStocks.slice(0, 4).map((rel) => {
                  const isPos = (rel.change || 0) >= 0;
                  return (
                    <div
                      key={rel.symbol}
                      onClick={() => onSelectStock(rel.symbol)}
                      className="bg-slate-950/60 border border-slate-800/80 hover:border-slate-700 rounded-xl p-3 cursor-pointer transition-all hover:bg-slate-850/60 flex flex-col justify-between group active:scale-[0.98]"
                    >
                      <div className="flex items-center gap-2">
                        <CompanyLogo
                          name={rel.name}
                          symbol={rel.symbol}
                          size="sm"
                          className="rounded-lg shrink-0 shadow"
                        />
                        <div className="min-w-0">
                          <div className="text-xs font-bold text-white truncate group-hover:text-slate-200">
                            {rel.name}
                          </div>
                          <div className="text-[10px] text-slate-400">
                            {rel.symbol.replace('.NS', '').replace('.BO', '')}
                          </div>
                        </div>
                      </div>
                      <div className="mt-2.5 pt-2 border-t border-slate-800/60 flex items-center justify-between">
                        <span className="text-xs font-bold text-white">
                          ₹{rel.current_price?.toLocaleString('en-IN', { minimumFractionDigits: 1, maximumFractionDigits: 2 })}
                        </span>
                        <span className={`text-[10px] font-semibold ${isPos ? 'text-teal-400' : 'text-rose-400'}`}>
                          {isPos ? '+' : ''}{(rel.change_percent || 0).toFixed(1)}%
                        </span>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          )}
        </section>
      ) : (
        /* Clean State: User hasn't searched anything yet -> Show Popular on Stockly */
        <section className="space-y-3">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <Flame className="w-4 h-4 text-orange-400" />
              <h2 className="text-base sm:text-lg font-extrabold text-white tracking-tight">
                Popular on Stockly
              </h2>
            </div>
            <span className="text-xs text-slate-400">Most actively tracked today</span>
          </div>

          {/* Grid of 4 to 8 popular stocks */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5 sm:gap-3">
            {(data.popular_picks && data.popular_picks.length > 0 ? data.popular_picks.slice(0, 4) : data.most_traded.slice(0, 4)).map((item) => {
              const isPos = item.change >= 0;
              return (
                <div
                  key={item.symbol}
                  onClick={() => onSelectStock(item.symbol)}
                  className="bg-slate-900/90 border border-slate-800 hover:border-slate-700 rounded-2xl p-3.5 transition-all cursor-pointer shadow-md group active:scale-[0.98] flex flex-col justify-between"
                >
                  <div className="flex items-center justify-between gap-2">
                    <CompanyLogo
                      name={item.name}
                      symbol={item.symbol}
                      size="sm"
                      className="rounded-xl shadow"
                    />
                    <span className={`text-[10px] font-semibold px-1.5 py-0.5 rounded ${isPos ? 'bg-teal-950/60 text-teal-300' : 'bg-rose-950/60 text-rose-300'}`}>
                      {isPos ? '+' : ''}{item.change_percent.toFixed(1)}%
                    </span>
                  </div>
                  <div className="mt-3">
                    <div className="text-xs font-bold text-white truncate group-hover:text-slate-200">
                      {item.name}
                    </div>
                    <div className="text-sm font-extrabold text-white mt-1">
                      ₹{item.current_price.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </section>
      )}

      {/* 1. SECTION: Most Traded Stocks (Groww style cards) */}
      <section className="space-y-3">
        <div className="flex items-center justify-between">
          <h2 className="text-lg sm:text-xl font-extrabold text-white tracking-tight flex items-center gap-2">
            <span>Most traded stocks</span>
          </h2>
          <button
            onClick={() => setShowAllTraded(!showAllTraded)}
            className="text-xs font-medium text-slate-400 hover:text-white flex items-center gap-1 transition-colors cursor-pointer"
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
                    <h3 className="font-bold text-white text-xs sm:text-sm group-hover:text-slate-200 transition-colors line-clamp-1">
                      {item.name}
                    </h3>
                    <div className="text-[10px] text-slate-400 mt-0.5">
                      Vol: {item.volume_formatted}
                    </div>
                  </div>
                </div>

                <div className="mt-3 pt-2.5 border-t border-slate-800/80">
                  <div className="font-extrabold text-white text-sm">
                    ₹{item.current_price.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                  </div>
                  <div className={`text-xs font-semibold mt-0.5 ${isPos ? 'text-teal-400' : 'text-rose-400'}`}>
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
          <div className="grid grid-cols-12 px-4 py-3 bg-slate-950/60 border-b border-slate-800 text-[11px] font-bold text-slate-400 tracking-wider uppercase">
            <div className="col-span-6 sm:col-span-5">Company</div>
            <div className="col-span-3 sm:col-span-4 text-right sm:text-center">Market price (1D)</div>
            <div className="col-span-3 text-right">Volume</div>
          </div>

          <div className="divide-y divide-slate-800/60">
            {displayedMovers.map((stock) => {
              const isPos = stock.change >= 0;
              return (
                <div
                  key={stock.symbol}
                  onClick={() => onSelectStock(stock.symbol)}
                  className="grid grid-cols-12 px-4 py-3 sm:py-3.5 items-center hover:bg-slate-850/50 cursor-pointer transition-colors group"
                >
                  {/* Company Column */}
                  <div className="col-span-6 sm:col-span-5 flex items-center gap-3 min-w-0 pr-2">
                    <CompanyLogo
                      name={stock.name}
                      symbol={stock.symbol}
                      size="sm"
                      className="rounded-lg shadow shrink-0"
                    />
                    <div className="min-w-0">
                      <div className="font-bold text-white text-xs sm:text-sm truncate group-hover:text-slate-200">
                        {stock.name}
                      </div>
                      <div className="text-[10px] sm:text-[11px] text-slate-400 truncate">
                        {stock.symbol.replace('.NS', '')}
                      </div>
                    </div>
                  </div>

                  {/* Market Price + Sparkline Column */}
                  <div className="col-span-3 sm:col-span-4 flex items-center justify-end sm:justify-center gap-3">
                    {renderSparkline(stock.sparkline, isPos)}
                    <div className="text-right">
                      <div className="font-extrabold text-white text-xs sm:text-sm">
                        ₹{stock.current_price.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                      </div>
                      <div className={`text-[11px] sm:text-xs font-semibold flex items-center justify-end gap-0.5 ${
                        isPos ? 'text-teal-400' : 'text-rose-400'
                      }`}>
                        {isPos ? (
                          <ArrowUpRight className="w-3 h-3 shrink-0" />
                        ) : (
                          <ArrowDownRight className="w-3 h-3 shrink-0" />
                        )}
                        <span>{isPos ? '+' : ''}{stock.change.toFixed(2)} ({isPos ? '+' : ''}{stock.change_percent.toFixed(2)}%)</span>
                      </div>
                    </div>
                  </div>

                  {/* Volume Column */}
                  <div className="col-span-3 text-right font-medium text-slate-300 text-xs sm:text-sm">
                    {stock.volume_formatted}
                  </div>
                </div>
              );
            })}
          </div>

          {activeMoversList.length > 6 && (
            <div className="p-3 bg-slate-950/40 border-t border-slate-800 text-center">
              <button
                onClick={() => setShowAllMovers(!showAllMovers)}
                className="text-xs font-bold text-slate-300 hover:text-white transition-colors cursor-pointer inline-flex items-center gap-1"
              >
                <span>{showAllMovers ? 'Show top 6' : `See all ${activeMoversList.length} movers`}</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </button>
            </div>
          )}
        </div>
      </section>

      {/* 3. SECTION: Sectors Trending Today (Groww visual ratio cards) */}
      <section className="space-y-3">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-lg sm:text-xl font-extrabold text-white tracking-tight flex items-center gap-2">
              <Layers className="w-5 h-5 text-slate-300" />
              <span>Sectors trending today</span>
            </h2>
            <p className="text-xs text-slate-400 mt-0.5">
              Live sector breadth and real-time gainers vs losers ratio
            </p>
          </div>
          <button
            onClick={() => setShowAllSectors(!showAllSectors)}
            className="text-xs font-medium text-slate-400 hover:text-white flex items-center gap-1 transition-colors cursor-pointer"
          >
            <span>{showAllSectors ? 'Show less' : 'See all'}</span>
            <ChevronRight className="w-3.5 h-3.5" />
          </button>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
          {displayedSectors.map((sector) => {
            const isPos = sector.change_percent >= 0;
            const total = sector.gainers + sector.losers || 1;
            const gainerRatio = Math.round((sector.gainers / total) * 100);

            return (
              <div
                key={sector.id}
                onClick={() => onExploreSector && onExploreSector(sector.name)}
                className="bg-slate-900/90 border border-slate-800 hover:border-slate-700 rounded-2xl p-4 transition-all cursor-pointer shadow-lg group active:scale-[0.99] flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between">
                    <div className="p-2 rounded-xl bg-slate-800/80 border border-slate-700/60 group-hover:bg-slate-700/80 transition-colors">
                      {renderSectorIcon(sector.icon)}
                    </div>
                    <div className={`text-xs font-bold px-2 py-0.5 rounded-md ${
                      isPos ? 'bg-teal-950/60 text-teal-300 border border-teal-800/40' : 'bg-rose-950/60 text-rose-300 border border-rose-800/40'
                    }`}>
                      {isPos ? '+' : ''}{sector.change_percent.toFixed(2)}%
                    </div>
                  </div>

                  <h3 className="font-extrabold text-white text-sm sm:text-base mt-3 group-hover:text-slate-100 transition-colors">
                    {sector.name}
                  </h3>
                </div>

                <div className="mt-4 pt-3 border-t border-slate-800/80 space-y-2">
                  {/* Gainers vs Losers Bar */}
                  <div className="h-1.5 w-full bg-slate-800 rounded-full overflow-hidden flex">
                    <div
                      style={{ width: `${gainerRatio}%` }}
                      className="bg-teal-400 h-full transition-all duration-500"
                    />
                    <div
                      style={{ width: `${100 - gainerRatio}%` }}
                      className="bg-rose-400 h-full transition-all duration-500"
                    />
                  </div>

                  <div className="flex items-center justify-between text-[11px] font-semibold">
                    <span className="text-teal-400">
                      {sector.gainers} Gainers
                    </span>
                    <span className="text-rose-400">
                      {sector.losers} Losers
                    </span>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </section>
    </div>
  );
};
