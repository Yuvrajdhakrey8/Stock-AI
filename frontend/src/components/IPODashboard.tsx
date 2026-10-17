import React, { useState, useEffect, useRef } from 'react';
import {
  Sparkles,
  TrendingUp,
  Calendar,
  DollarSign,
  Users,
  ShieldCheck,
  AlertTriangle,
  ChevronRight,
  Filter,
  Search,
  Layers,
  ArrowUpDown,
  CheckCircle2,
  Clock,
  Loader2,
  Scale,
  RefreshCw,
  Check,
} from 'lucide-react';
import type { IPOData, IPOSummaryMetrics } from '../types';
import { IPODetailModal } from './IPODetailModal';
import { IPOCompareModal } from './IPOCompareModal';
import { API_BASE_URL } from '../config';
import { mobileService } from '../services/mobileService';

export const IPODashboard: React.FC = () => {
  const [ipos, setIpos] = useState<IPOData[]>([]);
  const [summary, setSummary] = useState<IPOSummaryMetrics | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [statusFilter, setStatusFilter] = useState<string>(() => {
    try {
      return localStorage.getItem('dhakreystock_ipo_status') || 'all';
    } catch {
      return 'all';
    }
  });
  const [typeFilter, setTypeFilter] = useState<string>(() => {
    try {
      return localStorage.getItem('dhakreystock_ipo_type') || 'all';
    } catch {
      return 'all';
    }
  });
  const [sortBy, setSortBy] = useState<'gmp' | 'listing_gain' | 'issue_size' | 'date'>(() => {
    try {
      return (localStorage.getItem('dhakreystock_ipo_sort') as any) || 'gmp';
    } catch {
      return 'gmp';
    }
  });

  // Selected IPO for detail modal
  const [selectedIPO, setSelectedIPO] = useState<IPOData | null>(null);
  const [isDetailOpen, setIsDetailOpen] = useState<boolean>(false);

  // Selected IPO IDs for comparison
  const [compareIds, setCompareIds] = useState<string[]>([]);
  const [isCompareOpen, setIsCompareOpen] = useState<boolean>(false);

  const [isRefreshing, setIsRefreshing] = useState<boolean>(false);
  const listRef = useRef<HTMLDivElement>(null);

  const handleStatusCardClick = (status: 'open' | 'upcoming' | 'listed') => {
    if (statusFilter === status && typeFilter === 'all') {
      setStatusFilter('all');
    } else {
      setStatusFilter(status);
      setTypeFilter('all');
    }
    setTimeout(() => {
      listRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 60);
  };

  const handleSmeCardClick = () => {
    if (typeFilter === 'sme') {
      setTypeFilter('all');
    } else {
      setTypeFilter('sme');
      setStatusFilter('all');
    }
    setTimeout(() => {
      listRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 60);
  };

  // Mobile Back Button Handler for IPODashboard Modals
  useEffect(() => {
    const unregister = mobileService.registerBackHandler(() => {
      if (isCompareOpen) {
        setIsCompareOpen(false);
        return true;
      }
      if (isDetailOpen) {
        setIsDetailOpen(false);
        return true;
      }
      return false;
    });
    return unregister;
  }, [isCompareOpen, isDetailOpen]);

  useEffect(() => {
    try {
      localStorage.setItem('dhakreystock_ipo_status', statusFilter);
    } catch (e) {
      console.error(e);
    }
    fetchIPOData(false);
  }, [statusFilter]);

  useEffect(() => {
    try {
      localStorage.setItem('dhakreystock_ipo_type', typeFilter);
    } catch (e) {
      console.error(e);
    }
    fetchIPOData(false);
  }, [typeFilter]);

  useEffect(() => {
    try {
      localStorage.setItem('dhakreystock_ipo_sort', sortBy);
    } catch (e) {
      console.error(e);
    }
  }, [sortBy]);

  const fetchIPOData = async (forceRefresh: boolean = false) => {
    if (forceRefresh) {
      setIsRefreshing(true);
    } else {
      setLoading(true);
    }

    try {
      const [listRes, sumRes] = await Promise.all([
        fetch(`${API_BASE_URL}/api/ipo/list?status=${statusFilter}&type=${typeFilter}&refresh=${forceRefresh}`),
        fetch(`${API_BASE_URL}/api/ipo/summary`),
      ]);

      if (listRes.ok) {
        const listData = await listRes.json();
        setIpos(listData.ipos || []);
      }
      if (sumRes.ok) {
        const sumData = await sumRes.json();
        setSummary(sumData);
      }
    } catch (err) {
      console.error('Failed to load IPO data:', err);
    } finally {
      setLoading(false);
      setIsRefreshing(false);
    }
  };

  const handleOpenDetail = (ipo: IPOData) => {
    setSelectedIPO(ipo);
    setIsDetailOpen(true);
  };

  const toggleCompare = (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    if (compareIds.includes(id)) {
      setCompareIds(compareIds.filter((item) => item !== id));
    } else {
      if (compareIds.length >= 3) {
        alert('You can compare up to 3 IPOs at once.');
        return;
      }
      setCompareIds([...compareIds, id]);
    }
  };

  // Filter & Search
  const filteredIPOs = ipos.filter((ipo) => {
    if (!searchQuery) return true;
    const q = searchQuery.toLowerCase();
    return (
      ipo.name.toLowerCase().includes(q) ||
      ipo.sector.toLowerCase().includes(q) ||
      ipo.symbol.toLowerCase().includes(q)
    );
  });

  // Sort
  const sortedIPOs = [...filteredIPOs].sort((a, b) => {
    if (sortBy === 'gmp') {
      return b.gmp_closing_percent - a.gmp_closing_percent;
    }
    if (sortBy === 'listing_gain') {
      const gainA = a.listing?.listing_gain_percent ?? -999;
      const gainB = b.listing?.listing_gain_percent ?? -999;
      return gainB - gainA;
    }
    if (sortBy === 'issue_size') {
      return b.issue_size_cr - a.issue_size_cr;
    }
    return new Date(b.open_date).getTime() - new Date(a.open_date).getTime();
  });

  const comparedIPOs = ipos.filter((i) => compareIds.includes(i.id));

  return (
    <div className="space-y-6">
      {/* Top Header & Last Updated Badge */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div>
          <div className="flex items-center gap-2">
            <h1 className="text-xl sm:text-2xl font-extrabold text-white tracking-tight flex items-center gap-2">
              <Sparkles className="w-5 h-5 sm:w-6 sm:h-6 text-emerald-400 shrink-0" />
              <span>Indian IPO Research & Advisory</span>
            </h1>
          </div>
          <p className="text-[11px] sm:text-xs text-slate-400 mt-1">
            Complete analysis of Mainboard and SME IPOs with closing-day GMP, subscription progression, 1-lot retail profit, and missed opportunity retrospectives.
          </p>
        </div>

        <div className="flex items-center gap-2 self-stretch sm:self-auto flex-wrap">
          <button
            onClick={() => fetchIPOData(true)}
            disabled={isRefreshing}
            className="flex-1 sm:flex-initial flex items-center justify-center gap-1.5 text-xs text-slate-200 bg-slate-900 hover:bg-slate-800 border border-slate-700/80 px-3 py-2 sm:py-1.5 rounded-xl font-medium transition-colors shadow-sm disabled:opacity-50 active:scale-95"
            title="Fetch latest real-time Grey Market Premium and Subscription rates"
          >
            <RefreshCw className={`w-3.5 h-3.5 text-emerald-400 shrink-0 ${isRefreshing ? 'animate-spin' : ''}`} />
            <span>{isRefreshing ? 'Fetching Live...' : 'Refresh Live'}</span>
          </button>

          {summary?.last_updated && (
            <div className="flex items-center gap-1.5 text-[11px] sm:text-xs text-slate-400 bg-slate-900 border border-slate-800 px-2.5 sm:px-3 py-2 sm:py-1.5 rounded-xl">
              <Clock className="w-3.5 h-3.5 text-emerald-400 shrink-0" />
              <span className="truncate">{summary.last_updated}</span>
            </div>
          )}
        </div>
      </div>

      {/* Groww-style Interactive Category Cards */}
      {summary && (
        <div className="space-y-3">
          <div className="grid grid-cols-2 sm:grid-cols-2 lg:grid-cols-4 gap-2.5 sm:gap-3.5">
            {/* Card 1: Open for Bidding */}
            <div
              onClick={() => handleStatusCardClick('open')}
              className={`rounded-2xl p-3.5 sm:p-4 transition-all cursor-pointer shadow-md group relative overflow-hidden active:scale-[0.98] ${
                statusFilter === 'open' && typeFilter === 'all'
                  ? 'bg-emerald-950/50 border-2 border-emerald-500 ring-2 ring-emerald-500/30'
                  : 'bg-slate-900/90 border border-slate-800 hover:border-emerald-500/50 hover:bg-slate-850'
              }`}
            >
              <div className="flex items-center justify-between text-slate-300 text-[11px] sm:text-xs">
                <span className="font-semibold flex items-center gap-1.5">
                  <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                  Open Now
                </span>
                {statusFilter === 'open' && typeFilter === 'all' ? (
                  <span className="text-[10px] font-bold text-emerald-400 bg-emerald-900/50 px-2 py-0.5 rounded-full border border-emerald-500/40">
                    Active
                  </span>
                ) : (
                  <span className="text-[10px] text-slate-500 group-hover:text-emerald-400 font-medium">Filter</span>
                )}
              </div>
              <div className="text-2xl sm:text-3xl font-extrabold text-white mt-1.5 flex items-baseline gap-1.5">
                <span>{summary.open_count}</span>
                <span className="text-[11px] sm:text-xs text-emerald-400 font-medium">Bidding Live</span>
              </div>
              <div className="flex items-center justify-between mt-2 pt-2 border-t border-slate-800/60 text-[10px] sm:text-[11px]">
                <span className={summary.closes_today_count && summary.closes_today_count > 0 ? 'text-amber-400 font-semibold' : 'text-slate-400'}>
                  {summary.closes_today_count && summary.closes_today_count > 0 ? `⚡ ${summary.closes_today_count} Closes Today!` : 'Accepting Bids'}
                </span>
                <ChevronRight className="w-3.5 h-3.5 text-slate-400 group-hover:text-emerald-400 group-hover:translate-x-0.5 transition-all" />
              </div>
            </div>

            {/* Card 2: Upcoming Issues */}
            <div
              onClick={() => handleStatusCardClick('upcoming')}
              className={`rounded-2xl p-3.5 sm:p-4 transition-all cursor-pointer shadow-md group relative overflow-hidden active:scale-[0.98] ${
                statusFilter === 'upcoming' && typeFilter === 'all'
                  ? 'bg-sky-950/50 border-2 border-sky-500 ring-2 ring-sky-500/30'
                  : 'bg-slate-900/90 border border-slate-800 hover:border-sky-500/50 hover:bg-slate-850'
              }`}
            >
              <div className="flex items-center justify-between text-slate-300 text-[11px] sm:text-xs">
                <span className="font-semibold flex items-center gap-1.5">
                  <span className="w-2 h-2 rounded-full bg-sky-400" />
                  Upcoming
                </span>
                {statusFilter === 'upcoming' && typeFilter === 'all' ? (
                  <span className="text-[10px] font-bold text-sky-400 bg-sky-900/50 px-2 py-0.5 rounded-full border border-sky-500/40">
                    Active
                  </span>
                ) : (
                  <span className="text-[10px] text-slate-500 group-hover:text-sky-400 font-medium">Filter</span>
                )}
              </div>
              <div className="text-2xl sm:text-3xl font-extrabold text-sky-400 mt-1.5 flex items-baseline gap-1.5">
                <span>{summary.upcoming_count}</span>
                <span className="text-[11px] sm:text-xs text-slate-400 font-normal">Issues</span>
              </div>
              <div className="flex items-center justify-between mt-2 pt-2 border-t border-slate-800/60 text-[10px] sm:text-[11px] text-slate-400">
                <span>Announced / DRHP</span>
                <ChevronRight className="w-3.5 h-3.5 text-slate-400 group-hover:text-sky-400 group-hover:translate-x-0.5 transition-all" />
              </div>
            </div>

            {/* Card 3: Recently Listed */}
            <div
              onClick={() => handleStatusCardClick('listed')}
              className={`rounded-2xl p-3.5 sm:p-4 transition-all cursor-pointer shadow-md group relative overflow-hidden active:scale-[0.98] ${
                statusFilter === 'listed' && typeFilter === 'all'
                  ? 'bg-indigo-950/50 border-2 border-indigo-500 ring-2 ring-indigo-500/30'
                  : 'bg-slate-900/90 border border-slate-800 hover:border-indigo-500/50 hover:bg-slate-850'
              }`}
            >
              <div className="flex items-center justify-between text-slate-300 text-[11px] sm:text-xs">
                <span className="font-semibold flex items-center gap-1.5">
                  <span className="w-2 h-2 rounded-full bg-indigo-400" />
                  Recently Listed
                </span>
                {statusFilter === 'listed' && typeFilter === 'all' ? (
                  <span className="text-[10px] font-bold text-indigo-400 bg-indigo-900/50 px-2 py-0.5 rounded-full border border-indigo-500/40">
                    Active
                  </span>
                ) : (
                  <span className="text-[10px] text-slate-500 group-hover:text-indigo-400 font-medium">Filter</span>
                )}
              </div>
              <div className="text-2xl sm:text-3xl font-extrabold text-indigo-300 mt-1.5 flex items-baseline gap-1.5">
                <span>{summary.total_listed_tracked}</span>
                <span className="text-[11px] sm:text-xs text-emerald-400 font-semibold">+{summary.average_listing_gain_percent}% Pop</span>
              </div>
              <div className="flex items-center justify-between mt-2 pt-2 border-t border-slate-800/60 text-[10px] sm:text-[11px] text-slate-400">
                <span>Listing Day Profit</span>
                <ChevronRight className="w-3.5 h-3.5 text-slate-400 group-hover:text-indigo-400 group-hover:translate-x-0.5 transition-all" />
              </div>
            </div>

            {/* Card 4: SME Platform */}
            <div
              onClick={handleSmeCardClick}
              className={`rounded-2xl p-3.5 sm:p-4 transition-all cursor-pointer shadow-md group relative overflow-hidden active:scale-[0.98] ${
                typeFilter === 'sme'
                  ? 'bg-amber-950/50 border-2 border-amber-500 ring-2 ring-amber-500/30'
                  : 'bg-slate-900/90 border border-slate-800 hover:border-amber-500/50 hover:bg-slate-850'
              }`}
            >
              <div className="flex items-center justify-between text-slate-300 text-[11px] sm:text-xs">
                <span className="font-semibold flex items-center gap-1.5">
                  <span className="w-2 h-2 rounded-full bg-amber-400" />
                  SME Platform
                </span>
                {typeFilter === 'sme' ? (
                  <span className="text-[10px] font-bold text-amber-400 bg-amber-900/50 px-2 py-0.5 rounded-full border border-amber-500/40">
                    Active
                  </span>
                ) : (
                  <span className="text-[10px] text-slate-500 group-hover:text-amber-400 font-medium">Filter</span>
                )}
              </div>
              <div className="text-2xl sm:text-3xl font-extrabold text-amber-300 mt-1.5 flex items-baseline gap-1.5">
                <span>SME</span>
                <span className="text-[11px] sm:text-xs text-slate-400 font-normal">Issues</span>
              </div>
              <div className="flex items-center justify-between mt-2 pt-2 border-t border-slate-800/60 text-[10px] sm:text-[11px] text-slate-400">
                <span>NSE Emerge & BSE SME</span>
                <ChevronRight className="w-3.5 h-3.5 text-slate-400 group-hover:text-amber-400 group-hover:translate-x-0.5 transition-all" />
              </div>
            </div>
          </div>

          {/* Quick Performance Records Ribbon */}
          <div className="bg-slate-950/80 border border-slate-800/80 rounded-2xl px-3 py-2 text-xs flex items-center justify-between gap-3 overflow-x-auto scrollbar-none text-slate-400">
            <div className="flex items-center gap-1.5 shrink-0">
              <span className="text-[10px] uppercase font-bold text-slate-500">Track Record:</span>
              <span className="text-white font-semibold">+{summary.average_listing_gain_percent}%</span>
              <span>Avg Listing Gain</span>
            </div>
            {summary.best_performer && (
              <div className="flex items-center gap-1.5 shrink-0">
                <span className="text-emerald-400 font-bold">★ Top Winner:</span>
                <span className="text-white font-medium">{summary.best_performer.name.split(' ')[0]}</span>
                <span className="text-emerald-400 font-semibold">+{summary.best_performer.gain_percent}%</span>
              </div>
            )}
            {summary.worst_performer && (
              <div className="flex items-center gap-1.5 shrink-0">
                <span className="text-rose-400 font-bold">⚠ Weakest:</span>
                <span className="text-white font-medium">{summary.worst_performer.name.split(' ')[0]}</span>
                <span className="text-rose-400 font-semibold">{summary.worst_performer.gain_percent}%</span>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Toolbar: Search, Filters, Sort, Compare Action */}
      <div ref={listRef} className="bg-slate-900/90 border border-slate-800 rounded-2xl p-3.5 sm:p-4 shadow-xl flex flex-col md:flex-row md:items-center justify-between gap-3 sm:gap-4">
        {/* Search */}
        <div className="relative w-full md:max-w-md">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search IPO by company name or sector..."
            className="w-full pl-10 pr-4 py-2 bg-slate-950 border border-slate-800 rounded-xl text-xs text-white placeholder-slate-500 focus:outline-none focus:border-emerald-500"
          />
        </div>

        {/* Filters Group */}
        <div className="flex items-center gap-2 sm:gap-3 flex-wrap text-xs">
          {/* Status Pills */}
          <div className="bg-slate-950 p-1 rounded-xl border border-slate-800 flex items-center gap-1 overflow-x-auto scrollbar-none">
            {['all', 'open', 'upcoming', 'listed'].map((st) => (
              <button
                key={st}
                onClick={() => setStatusFilter(st)}
                className={`px-2 sm:px-2.5 py-1 rounded-lg font-medium transition-all uppercase text-[9px] sm:text-[10px] tracking-wider shrink-0 ${
                  statusFilter === st
                    ? 'bg-emerald-500 text-slate-950 font-bold'
                    : 'text-slate-400 hover:text-white'
                }`}
              >
                {st}
              </button>
            ))}
          </div>

          {/* Type Filter */}
          <div className="bg-slate-950 p-1 rounded-xl border border-slate-800 flex items-center gap-1 overflow-x-auto scrollbar-none">
            {['all', 'mainboard', 'sme'].map((tp) => (
              <button
                key={tp}
                onClick={() => setTypeFilter(tp)}
                className={`px-2 sm:px-2.5 py-1 rounded-lg font-medium transition-all uppercase text-[9px] sm:text-[10px] tracking-wider shrink-0 ${
                  typeFilter === tp
                    ? 'bg-emerald-500 text-slate-950 font-bold'
                    : 'text-slate-400 hover:text-white'
                }`}
              >
                {tp}
              </button>
            ))}
          </div>

          {/* Sort selector */}
          <div className="flex items-center gap-1.5 text-slate-400">
            <ArrowUpDown className="w-3.5 h-3.5 shrink-0" />
            <select
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value as any)}
              className="bg-slate-950 border border-slate-800 rounded-xl px-2.5 py-1.5 text-slate-200 text-xs focus:outline-none"
            >
              <option value="gmp">Sort by GMP %</option>
              <option value="listing_gain">Sort by Actual Gain</option>
              <option value="issue_size">Sort by Issue Size</option>
              <option value="date">Sort by Recent Date</option>
            </select>
          </div>

          {/* Compare Button */}
          {compareIds.length > 0 && (
            <button
              onClick={() => setIsCompareOpen(true)}
              className="px-3 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs inline-flex items-center gap-1.5 shadow-lg shadow-indigo-600/20 transition-all animate-bounce shrink-0"
            >
              <Scale className="w-3.5 h-3.5" />
              <span>Compare ({compareIds.length})</span>
            </button>
          )}
        </div>
      </div>

      {/* Active Filter Banner (Groww style) */}
      {(statusFilter !== 'all' || typeFilter !== 'all' || searchQuery.trim()) && (
        <div className="flex items-center justify-between p-3 bg-slate-900/90 border border-emerald-500/30 rounded-2xl shadow-md animate-in fade-in duration-200">
          <div className="flex items-center gap-2 flex-wrap">
            <span className="text-xs text-slate-400">Viewing:</span>
            {statusFilter !== 'all' && (
              <span className="text-xs font-bold text-emerald-400 bg-emerald-950 border border-emerald-500/40 px-2.5 py-0.5 rounded-lg uppercase tracking-wide flex items-center gap-1">
                <Check className="w-3 h-3" />
                {statusFilter} IPOs
              </span>
            )}
            {typeFilter !== 'all' && (
              <span className="text-xs font-bold text-amber-400 bg-amber-950 border border-amber-500/40 px-2.5 py-0.5 rounded-lg uppercase tracking-wide flex items-center gap-1">
                <Check className="w-3 h-3" />
                {typeFilter} Platform
              </span>
            )}
            {searchQuery.trim() && (
              <span className="text-xs text-slate-300 font-medium bg-slate-800 px-2 py-0.5 rounded-lg">
                "{searchQuery.trim()}"
              </span>
            )}
            <span className="text-xs text-slate-400 font-semibold">({sortedIPOs.length} results)</span>
          </div>

          <button
            onClick={() => {
              setStatusFilter('all');
              setTypeFilter('all');
              setSearchQuery('');
            }}
            className="text-xs font-semibold text-slate-300 hover:text-white px-2.5 py-1 rounded-xl bg-slate-800 hover:bg-slate-700 transition-colors shrink-0"
          >
            Show All ✕
          </button>
        </div>
      )}

      {/* IPO Cards Grid */}
      {loading ? (
        <div className="py-20 text-center space-y-3">
          <Loader2 className="w-8 h-8 text-emerald-400 animate-spin mx-auto" />
          <p className="text-sm text-slate-400">Loading verified Indian IPO dataset...</p>
        </div>
      ) : sortedIPOs.length === 0 ? (
        <div className="py-20 text-center text-slate-500 bg-slate-900/60 rounded-3xl border border-slate-800">
          No IPOs found matching the specified filters.
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {sortedIPOs.map((ipo) => {
            const isListed = ipo.status === 'Listed';
            const isSelectedForCompare = compareIds.includes(ipo.id);
            const rec = ipo.recommendation_at_ipo;
            const listing = ipo.listing;
            const missed = ipo.missed_opportunity_analysis;

            return (
              <div
                key={ipo.id}
                onClick={() => handleOpenDetail(ipo)}
                className={`bg-slate-900/90 border rounded-2xl sm:rounded-3xl p-4 sm:p-5 shadow-xl hover:border-slate-700 transition-all cursor-pointer flex flex-col justify-between group relative overflow-hidden active:scale-[0.99] ${
                  isSelectedForCompare ? 'ring-2 ring-indigo-500 border-indigo-500/50' : 'border-slate-800'
                }`}
              >
                {/* Top Badge Row */}
                <div>
                  <div className="flex items-center justify-between gap-2 mb-3">
                    <div className="flex items-center gap-1.5 flex-wrap">
                      {ipo.closes_today ? (
                        <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider bg-amber-500/20 text-amber-400 border border-amber-500/40 animate-pulse flex items-center gap-1">
                          <Clock className="w-3 h-3" /> Closes Today
                        </span>
                      ) : (
                        <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider border ${
                          ipo.status === 'Open'
                            ? 'bg-emerald-500/20 text-emerald-400 border-emerald-500/40 animate-pulse'
                            : ipo.status === 'Upcoming'
                            ? 'bg-sky-500/20 text-sky-400 border-sky-500/40'
                            : 'bg-slate-800 text-slate-400 border-slate-700'
                        }`}>
                          {ipo.status}
                        </span>
                      )}
                      <span className="text-[10px] px-2 py-0.5 rounded bg-slate-800/80 text-slate-300 font-semibold border border-slate-700/60">
                        {ipo.ipo_type}
                      </span>
                      {rec && (
                        <span className={`text-[10px] px-2 py-0.5 rounded-md font-bold ${
                          rec.verdict === 'Apply'
                            ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30'
                            : rec.verdict === 'Avoid'
                            ? 'bg-rose-500/20 text-rose-400 border border-rose-500/30'
                            : 'bg-amber-500/20 text-amber-400 border border-amber-500/30'
                        }`}>
                          Rec: {rec.verdict}
                        </span>
                      )}
                    </div>

                    {/* Compare Toggle Checkbox */}
                    <button
                      onClick={(e) => toggleCompare(ipo.id, e)}
                      className={`text-[10px] px-2 py-1 rounded-lg border font-medium transition-colors ${
                        isSelectedForCompare
                          ? 'bg-indigo-600 text-white border-indigo-500'
                          : 'bg-slate-950 text-slate-400 border-slate-800 hover:text-white'
                      }`}
                    >
                      {isSelectedForCompare ? '✓ In Compare' : '+ Compare'}
                    </button>
                  </div>

                  {/* Company Name & Sector */}
                  <h3 className="text-base font-bold text-white group-hover:text-emerald-400 transition-colors line-clamp-1">
                    {ipo.name}
                  </h3>
                  <p className="text-xs text-slate-400 mt-0.5 truncate">{ipo.sector}</p>

                  {/* Mobile-Only Clean Card Summary (Prevents detail bombardment on mobile screens) */}
                  <div className="block sm:hidden mt-3 pt-2.5 border-t border-slate-800/80 space-y-2">
                    <div className="flex items-center justify-between text-xs">
                      <div>
                        <span className="text-[10px] text-slate-500 block">Price Band</span>
                        <span className="font-bold text-white text-xs">{ipo.price_band}</span>
                      </div>
                      <div className="text-right">
                        <span className="text-[10px] text-slate-500 block">Expected GMP</span>
                        <span className={`font-extrabold text-xs ${ipo.gmp_closing_day >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                          {ipo.gmp_closing_day >= 0 ? '+' : ''}₹{ipo.gmp_closing_day} ({ipo.gmp_closing_percent.toFixed(0)}%)
                        </span>
                      </div>
                    </div>
                    <div className="pt-1 text-[10px] text-emerald-400/90 font-medium flex items-center justify-between">
                      <span>Tap to view subscription, financials & GMP trend</span>
                      <ChevronRight className="w-3.5 h-3.5 text-slate-500 group-hover:text-emerald-400 transition-colors" />
                    </div>
                  </div>

                  {/* Desktop-Only Detailed Multi-Box Layout */}
                  <div className="hidden sm:block">
                    {/* Issue Date & Price Band */}
                    <div className="grid grid-cols-2 gap-2 mt-4 pt-3 border-t border-slate-800/80 text-xs">
                      <div>
                        <div className="text-[10px] text-slate-500">Price Band</div>
                        <div className="font-bold text-white mt-0.5">{ipo.price_band}</div>
                        <div className="text-[10px] text-slate-400 mt-0.5">
                          Lot: {ipo.lot_size} (₹{ipo.min_investment.toLocaleString('en-IN')})
                        </div>
                      </div>
                      <div>
                        <div className="text-[10px] text-slate-500">Issue Size</div>
                        <div className="font-bold text-white mt-0.5">₹{ipo.issue_size_cr.toLocaleString('en-IN')} Cr</div>
                        <div className={`text-[10px] mt-0.5 ${ipo.closes_today ? 'text-amber-400 font-bold' : 'text-slate-400'}`}>
                          {ipo.closes_today ? '⚡ Closes Today!' : (ipo.close_date ? `Closes: ${ipo.close_date}` : 'Dates TBA')}
                        </div>
                      </div>
                    </div>

                    {/* Closing GMP & Subscription Progress */}
                    <div className="mt-3 p-3 rounded-2xl bg-slate-950/70 border border-slate-800 text-xs space-y-2">
                      <div className="flex items-center justify-between">
                        <span className="text-[11px] text-slate-400">Closing-Day GMP</span>
                        <span className={`font-bold ${ipo.gmp_closing_day >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                          {ipo.gmp_closing_day >= 0 ? '+' : ''}₹{ipo.gmp_closing_day} ({ipo.gmp_closing_percent.toFixed(1)}%)
                        </span>
                      </div>

                      <div className="flex items-center justify-between">
                        <span className="text-[11px] text-slate-400">Subscription Total</span>
                        <span className="font-bold text-slate-200">
                          {ipo.subscription.final_day
                            ? `${ipo.subscription.final_day.total}x`
                            : ipo.subscription.day2
                            ? `${ipo.subscription.day2.total}x (Day 2)`
                            : 'Pending'}
                        </span>
                      </div>
                    </div>

                    {/* Outcome Box (If Listed) */}
                    {isListed && listing && (
                      <div className="mt-3 p-3 rounded-2xl bg-emerald-950/20 border border-emerald-900/40 text-xs space-y-1.5">
                        <div className="flex items-center justify-between">
                          <span className="text-[11px] text-slate-400">Actual Listing Gain</span>
                          <span className={`font-bold ${listing.listing_gain_percent >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                            {listing.listing_gain_percent >= 0 ? '+' : ''}{listing.listing_gain_percent.toFixed(1)}% (₹{listing.listing_gain_rs})
                          </span>
                        </div>
                        <div className="flex items-center justify-between">
                          <span className="text-[11px] text-slate-400">Retail 1-Lot Profit</span>
                          <span className={`font-bold text-sm ${listing.profit_per_lot >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                            {listing.profit_per_lot >= 0 ? '+' : ''}₹{listing.profit_per_lot.toLocaleString('en-IN')}
                          </span>
                        </div>
                      </div>
                    )}

                    {/* Missed Opportunity Badge */}
                    {missed && (
                      <div className="mt-3 flex items-center justify-between text-[11px] px-2.5 py-1.5 rounded-xl bg-slate-950 border border-slate-800">
                        <span className="text-slate-400">Skipping Decision:</span>
                        <span className={`font-bold ${
                          missed.is_missed_opp ? 'text-amber-400' : 'text-emerald-400'
                        }`}>
                          {missed.verdict}
                        </span>
                      </div>
                    )}
                  </div>
                </div>

                {/* Bottom Action CTA (Desktop only) */}
                <div className="hidden sm:flex mt-4 pt-3 border-t border-slate-800/80 items-center justify-between text-xs">
                  <span className="text-slate-500 font-medium">Click to see full analysis</span>
                  <div className="flex items-center gap-1 font-bold text-emerald-400 group-hover:translate-x-1 transition-all">
                    <span>Research Report</span>
                    <ChevronRight className="w-4 h-4" />
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* Detailed Modal */}
      <IPODetailModal
        ipo={selectedIPO}
        isOpen={isDetailOpen}
        onClose={() => setIsDetailOpen(false)}
      />

      {/* Comparison Modal */}
      <IPOCompareModal
        ipos={comparedIPOs}
        isOpen={isCompareOpen}
        onClose={() => setIsCompareOpen(false)}
        onSelectIPO={handleOpenDetail}
      />
    </div>
  );
};
