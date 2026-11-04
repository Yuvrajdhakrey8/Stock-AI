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
  ArrowUpDown,
  Clock,
  Loader2,
  Scale,
  RefreshCw,
  ExternalLink,
  CheckCircle2,
  Info,
} from 'lucide-react';
import type { IPOData, IPOSummaryMetrics, ListingRadarData } from '../types';
import { IPODetailModal } from './IPODetailModal';
import { IPOCompareModal } from './IPOCompareModal';
import { ListingRadarCard } from './ListingRadarCard';
import { CompanyLogo } from './CompanyLogo';
import { API_BASE_URL } from '../config';
import { mobileService } from '../services/mobileService';
import { adService } from '../services/adService';

type TabType = 'open' | 'closed' | 'upcoming';

export const IPODashboard: React.FC = () => {
  const [ipos, setIpos] = useState<IPOData[]>([]);
  const [summary, setSummary] = useState<IPOSummaryMetrics | null>(null);
  const [radarData, setRadarData] = useState<ListingRadarData | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [searchQuery, setSearchQuery] = useState<string>('');

  // Exactly 3 Categories: Open, Closed, Upcoming (Groww UI)
  const [statusFilter, setStatusFilter] = useState<TabType>(() => {
    try {
      const saved = localStorage.getItem('dhakreystock_ipo_status');
      if (saved === 'open' || saved === 'closed' || saved === 'upcoming') {
        return saved;
      }
      return 'open';
    } catch {
      return 'open';
    }
  });

  const [typeFilter, setTypeFilter] = useState<string>(() => {
    try {
      return localStorage.getItem('dhakreystock_ipo_type') || 'all';
    } catch {
      return 'all';
    }
  });

  const [sortBy, setSortBy] = useState<'date' | 'gmp' | 'gain' | 'issue_size'>('date');

  // Selected IPO for detail modal
  const [selectedIPO, setSelectedIPO] = useState<IPOData | null>(null);
  const [isDetailOpen, setIsDetailOpen] = useState<boolean>(false);

  // Selected IPO IDs for comparison
  const [compareIds, setCompareIds] = useState<string[]>([]);
  const [isCompareOpen, setIsCompareOpen] = useState<boolean>(false);

  const [isRefreshing, setIsRefreshing] = useState<boolean>(false);
  const listRef = useRef<HTMLDivElement>(null);

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

  // Hide bottom banner during full-screen modals to prevent covering modal buttons
  useEffect(() => {
    if (isDetailOpen || isCompareOpen) {
      adService.hideBanner();
    } else {
      adService.showBottomBanner();
    }
  }, [isDetailOpen, isCompareOpen]);

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

  const fetchIPOData = async (forceRefresh: boolean = false) => {
    if (forceRefresh) {
      setIsRefreshing(true);
    } else {
      setLoading(true);
    }

    try {
      const [listRes, sumRes, radarRes] = await Promise.all([
        fetch(`${API_BASE_URL}/api/ipo/list?status=${statusFilter}&type=${typeFilter}&refresh=${forceRefresh}`),
        fetch(`${API_BASE_URL}/api/ipo/summary?type=${typeFilter}`),
        fetch(`${API_BASE_URL}/api/ipo/listing-radar`),
      ]);

      if (listRes.ok) {
        const listData = await listRes.json();
        setIpos(listData.ipos || []);
      }
      if (sumRes.ok) {
        const sumData = await sumRes.json();
        setSummary(sumData);
      }
      if (radarRes.ok) {
        const radar = await radarRes.json();
        setRadarData(radar);
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

  const MONTH_MAP: Record<string, number> = {
    jan: 0, feb: 1, mar: 2, apr: 3, may: 4, jun: 5,
    jul: 6, aug: 7, sep: 8, oct: 9, nov: 10, dec: 11,
  };

  const parseIPODateToTime = (dStr?: string, defaultYear: number = 2026): number => {
    if (!dStr) return 0;
    const s = dStr.trim();
    const m = s.match(/^(\d{1,2})[\s\-]+([A-Za-z]{3})[\s\-]+(\d{2,4})$/);
    if (m) {
      const day = parseInt(m[1], 10);
      const mon = MONTH_MAP[m[2].toLowerCase()] ?? 0;
      let yr = parseInt(m[3], 10);
      if (yr < 100) yr = 2000 + yr;
      return new Date(yr, mon, day).getTime();
    }
    const m2 = s.match(/^(\d{1,2})[\s\-]+([A-Za-z]{3})$/);
    if (m2) {
      const day = parseInt(m2[1], 10);
      const mon = MONTH_MAP[m2[2].toLowerCase()] ?? 0;
      return new Date(defaultYear, mon, day).getTime();
    }
    const t = new Date(s).getTime();
    return isNaN(t) ? 0 : t;
  };

  // Sort: Latest one on top and then old ones
  const sortedIPOs = [...filteredIPOs].sort((a, b) => {
    if (sortBy === 'gmp') {
      return b.gmp_closing_percent - a.gmp_closing_percent;
    }
    if (sortBy === 'gain') {
      const gainA = a.listing?.listing_gain_percent ?? a.gmp_closing_percent ?? -999;
      const gainB = b.listing?.listing_gain_percent ?? b.gmp_closing_percent ?? -999;
      return gainB - gainA;
    }
    if (sortBy === 'issue_size') {
      return b.issue_size_cr - a.issue_size_cr;
    }
    // Default sortBy === 'date': Latest one on top, then old ones
    if (statusFilter === 'open') {
      if (a.closes_today && !b.closes_today) return -1;
      if (!a.closes_today && b.closes_today) return 1;
    }
    const timeA = parseIPODateToTime(a.listing_date || a.close_date || a.open_date);
    const timeB = parseIPODateToTime(b.listing_date || b.close_date || b.open_date);
    return timeB - timeA;
  });

  const comparedIPOs = ipos.filter((i) => compareIds.includes(i.id));

  const handleCheckAllotment = (e: React.MouseEvent) => {
    e.stopPropagation();
    window.open('https://ipostatus.kfintech.com/', '_blank', 'noopener,noreferrer');
  };

  // Helper function to render AI Suggestion badge (Soft, pastel tones: #fff1f3, #fff8eb, #f0fdf4)
  const renderAISuggestion = (ipo: IPOData) => {
    const isListed = ipo.status === 'Listed';
    const rec = ipo.recommendation_at_ipo;
    const listing = ipo.listing;

    if (isListed && listing) {
      const isPos = listing.listing_gain_percent >= 0;
      return (
        <span className={`text-[11px] font-semibold px-2.5 py-0.5 rounded-md ${
          isPos ? 'bg-[#f0fdf4] text-[#047857] border border-[#d1fae5]' : 'bg-[#fff1f3] text-[#be123c] border border-[#fecdd3]'
        }`}>
          {isPos ? '+' : ''}{listing.listing_gain_percent.toFixed(1)}%
        </span>
      );
    }

    if (ipo.status === 'Open' || ipo.status === 'Upcoming') {
      if (ipo.gmp_closing_percent >= 25 || rec?.verdict === 'Apply') {
        return (
          <span className="text-[11px] font-semibold px-2.5 py-0.5 rounded-md bg-[#f0fdf4] text-[#047857] border border-[#d1fae5]">
            Best Buy
          </span>
        );
      }
      if (ipo.gmp_closing_percent >= 8) {
        return (
          <span className="text-[11px] font-semibold px-2.5 py-0.5 rounded-md bg-[#fff8eb] text-[#b45309] border border-[#fef3c7]">
            Caution
          </span>
        );
      }
      return (
        <span className="text-[11px] font-semibold px-2.5 py-0.5 rounded-md bg-[#fff1f3] text-[#be123c] border border-[#fecdd3]">
          Avoid
        </span>
      );
    }

    return (
      <span className="text-[11px] font-semibold px-2.5 py-0.5 rounded-md bg-[#f8fafc] text-[#334155] border border-[#e2e8f0]">
        Watch
      </span>
    );
  };

  return (
    <div className="space-y-5">
      {/* Groww-style Page Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div>
          <div className="flex items-center gap-2">
            <h1 className="text-xl sm:text-2xl font-extrabold text-white tracking-tight flex items-center gap-2">
              <Sparkles className="w-5 h-5 sm:w-6 sm:h-6 text-slate-400 shrink-0" />
              <span>IPOs</span>
            </h1>
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Real-time Indian IPO tracking, Closing-Day GMP, Live subscriptions, and AI recommendations.
          </p>
        </div>

        <div className="flex items-center gap-2 self-stretch sm:self-auto flex-wrap">
          <button
            onClick={() => fetchIPOData(true)}
            disabled={isRefreshing}
            className="flex-1 sm:flex-initial flex items-center justify-center gap-1.5 text-xs text-slate-200 bg-slate-900 hover:bg-slate-800 border border-slate-700/80 px-3 py-2 sm:py-1.5 rounded-xl font-medium transition-colors shadow-sm disabled:opacity-50 active:scale-95"
            title="Fetch latest real-time Grey Market Premium and Subscription rates"
          >
            <RefreshCw className={`w-3.5 h-3.5 text-slate-400 shrink-0 ${isRefreshing ? 'animate-spin' : ''}`} />
            <span>{isRefreshing ? 'Updating...' : 'Refresh Live'}</span>
          </button>

          {summary?.last_updated && (
            <div className="flex items-center gap-1.5 text-[11px] sm:text-xs text-slate-400 bg-slate-900 border border-slate-800 px-2.5 sm:px-3 py-2 sm:py-1.5 rounded-xl">
              <Clock className="w-3.5 h-3.5 text-emerald-400 shrink-0" />
              <span className="truncate">{summary.last_updated}</span>
            </div>
          )}
        </div>
      </div>

      {/* Listing Day Radar & Pre-Market Price Discovery */}
      <ListingRadarCard
        radarData={radarData}
        onSelectIPO={(id) => {
          const found = ipos.find((item) => item.id === id);
          if (found) handleOpenDetail(found);
        }}
      />

      {/* Groww 3 Categories Pill Navigation + Type Filter */}
      <div className="bg-slate-900/95 border border-slate-800 rounded-2xl p-2.5 sm:p-3 shadow-xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-3">
          {/* Exactly 3 Categories: Open, Closed, Upcoming (Groww Style) */}
          <div className="flex items-center gap-2 overflow-x-auto scrollbar-none pb-1 md:pb-0">
            {/* 1. Open Tab */}
            <button
              onClick={() => setStatusFilter('open')}
              className={`flex items-center gap-2 px-3.5 py-1.5 rounded-xl text-xs sm:text-sm font-semibold transition-all shrink-0 cursor-pointer ${
                statusFilter === 'open'
                  ? 'bg-slate-100 text-slate-950 shadow-sm'
                  : 'bg-slate-950 text-slate-400 hover:text-white border border-slate-800'
              }`}
            >
              <span>Open</span>
              <span className={`px-1.5 py-0.2 rounded-md text-[10px] font-bold ${
                statusFilter === 'open' ? 'bg-slate-300 text-slate-950' : 'bg-slate-800 text-slate-400'
              }`}>
                {statusFilter === 'open' ? sortedIPOs.length : (summary?.open_count ?? 0)}
              </span>
            </button>

            {/* 2. Closed Tab */}
            <button
              onClick={() => setStatusFilter('closed')}
              className={`flex items-center gap-2 px-3.5 py-1.5 rounded-xl text-xs sm:text-sm font-semibold transition-all shrink-0 cursor-pointer ${
                statusFilter === 'closed'
                  ? 'bg-slate-100 text-slate-950 shadow-sm'
                  : 'bg-slate-950 text-slate-400 hover:text-white border border-slate-800'
              }`}
            >
              <span>Closed</span>
              <span className={`px-1.5 py-0.2 rounded-md text-[10px] font-bold ${
                statusFilter === 'closed' ? 'bg-slate-300 text-slate-950' : 'bg-slate-800 text-slate-400'
              }`}>
                {statusFilter === 'closed' ? sortedIPOs.length : (summary?.closed_count ?? 0)}
              </span>
            </button>

            {/* 3. Upcoming Tab */}
            <button
              onClick={() => setStatusFilter('upcoming')}
              className={`flex items-center gap-2 px-3.5 py-1.5 rounded-xl text-xs sm:text-sm font-semibold transition-all shrink-0 cursor-pointer ${
                statusFilter === 'upcoming'
                  ? 'bg-slate-100 text-slate-950 shadow-sm'
                  : 'bg-slate-950 text-slate-400 hover:text-white border border-slate-800'
              }`}
            >
              <span>Upcoming</span>
              <span className={`px-1.5 py-0.2 rounded-md text-[10px] font-bold ${
                statusFilter === 'upcoming' ? 'bg-slate-300 text-slate-950' : 'bg-slate-800 text-slate-400'
              }`}>
                {statusFilter === 'upcoming' ? sortedIPOs.length : (summary?.upcoming_count ?? 0)}
              </span>
            </button>
          </div>

          {/* Sub-Filters: Type & Sort */}
          <div className="flex items-center gap-2 flex-wrap">
            {/* IPO Type Dropdown (Groww: IPO type: All v) */}
            <div className="flex items-center gap-1.5 bg-slate-950 border border-slate-800 rounded-xl px-2.5 py-1.5 text-xs text-slate-300">
              <span className="text-slate-500">IPO type:</span>
              <select
                value={typeFilter}
                onChange={(e) => setTypeFilter(e.target.value)}
                className="bg-transparent font-semibold text-white focus:outline-none cursor-pointer"
              >
                <option value="all" className="bg-slate-900 text-white">All Types</option>
                <option value="mainboard" className="bg-slate-900 text-white">Mainboard</option>
                <option value="sme" className="bg-slate-900 text-white">SME</option>
              </select>
            </div>

            {/* Sort Selector */}
            <div className="flex items-center gap-1.5 bg-slate-950 border border-slate-800 rounded-xl px-2.5 py-1.5 text-xs text-slate-300">
              <ArrowUpDown className="w-3.5 h-3.5 text-slate-500 shrink-0" />
              <select
                value={sortBy}
                onChange={(e) => setSortBy(e.target.value as any)}
                className="bg-transparent font-medium text-white focus:outline-none cursor-pointer"
              >
                <option value="date" className="bg-slate-900 text-white">Sort by Date (Latest First)</option>
                <option value="gmp" className="bg-slate-900 text-white">Sort by GMP %</option>
                <option value="gain" className="bg-slate-900 text-white">Sort by Listing Gain</option>
                <option value="issue_size" className="bg-slate-900 text-white">Sort by Size</option>
              </select>
            </div>

            {/* Compare Button */}
            {compareIds.length > 0 && (
              <button
                onClick={() => setIsCompareOpen(true)}
                className="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-semibold text-xs inline-flex items-center gap-1.5 border border-slate-700 transition-all shrink-0"
              >
                <Scale className="w-3.5 h-3.5" />
                <span>Compare ({compareIds.length})</span>
              </button>
            )}
          </div>
        </div>

        {/* Search Bar */}
        <div className="mt-2.5 pt-2.5 border-t border-slate-800/80">
          <div className="relative">
            <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search IPO by company name or sector..."
              className="w-full pl-10 pr-4 py-2 bg-slate-950 border border-slate-800 rounded-xl text-xs text-white placeholder-slate-500 focus:outline-none focus:border-emerald-500"
            />
          </div>
        </div>
      </div>

      {/* IPO Cards Container */}
      <div ref={listRef}>
        {loading ? (
          <div className="py-20 text-center space-y-3">
            <Loader2 className="w-8 h-8 text-emerald-400 animate-spin mx-auto" />
            <p className="text-sm text-slate-400">Loading verified Indian IPO dataset...</p>
          </div>
        ) : sortedIPOs.length === 0 ? (
          <div className="py-14 px-4 text-center text-slate-400 bg-slate-900/60 rounded-3xl border border-slate-800 max-w-lg mx-auto space-y-3 shadow-xl">
            <Info className="w-8 h-8 text-slate-500 mx-auto" />
            <p className="font-bold text-white text-base">
              {searchQuery
                ? `No IPOs matching "${searchQuery}"`
                : typeFilter !== 'all'
                ? `No ${typeFilter === 'mainboard' ? 'Mainboard' : 'SME'} IPOs in ${statusFilter.toUpperCase()}`
                : `No IPOs currently in ${statusFilter.toUpperCase()}`}
            </p>
            <p className="text-xs text-slate-400 leading-relaxed max-w-md mx-auto">
              {searchQuery
                ? 'Try clearing your search query or searching with a different keyword.'
                : typeFilter === 'mainboard'
                ? 'There are currently no Mainboard IPOs in this tab. Switch to "All Types" to see available SME IPOs.'
                : typeFilter === 'sme'
                ? 'There are currently no SME IPOs in this tab. Switch to "All Types" to see available Mainboard IPOs.'
                : 'Check the Upcoming tab for upcoming bidding dates and notifications.'}
            </p>
            <div className="flex items-center justify-center gap-2 pt-1 flex-wrap">
              {searchQuery && (
                <button
                  onClick={() => setSearchQuery('')}
                  className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-semibold text-xs transition-colors cursor-pointer"
                >
                  Clear Search
                </button>
              )}
              {typeFilter !== 'all' && (
                <button
                  onClick={() => setTypeFilter('all')}
                  className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold text-xs border border-slate-700 transition-all active:scale-95 cursor-pointer"
                >
                  Switch to All Types (Mainboard & SME)
                </button>
              )}
            </div>
          </div>
        ) : (
          <div className="bg-slate-900/90 border border-slate-800 rounded-2xl sm:rounded-3xl shadow-xl overflow-hidden divide-y divide-slate-800/60">
            {/* Desktop Table Header: Shows AI Suggestion on Open & Upcoming only */}
            {statusFilter === 'closed' ? (
              <div className="hidden lg:grid grid-cols-12 gap-3 px-5 py-3.5 bg-slate-950/80 text-[11px] font-bold uppercase tracking-wider text-slate-400 border-b border-slate-800">
                <div className="col-span-4">Company</div>
                <div className="col-span-2">Listing Date</div>
                <div className="col-span-2">Price & Lot</div>
                <div className="col-span-2 text-right">Listing Gain</div>
                <div className="col-span-1 text-center">Sub.</div>
                <div className="col-span-1 text-right">Allotment</div>
              </div>
            ) : (
              <div className="hidden lg:grid grid-cols-12 gap-3 px-5 py-3.5 bg-slate-950/80 text-[11px] font-bold uppercase tracking-wider text-slate-400 border-b border-slate-800">
                <div className="col-span-3">Company</div>
                <div className="col-span-2">{statusFilter === 'open' ? 'Bidding Closes' : 'Opening Date'}</div>
                <div className="col-span-2">Price & Lot</div>
                <div className="col-span-2 text-right">Expected GMP</div>
                <div className="col-span-1 text-center">Sub.</div>
                <div className="col-span-2 text-right">AI Suggestion</div>
              </div>
            )}

            {/* List Rows */}
            {sortedIPOs.map((ipo) => {
              const isListed = ipo.status === 'Listed';
              const isSelectedForCompare = compareIds.includes(ipo.id);
              const listing = ipo.listing;

              return (
                <div
                  key={ipo.id}
                  onClick={() => handleOpenDetail(ipo)}
                  className={`p-3.5 sm:p-4 hover:bg-slate-800/40 transition-colors cursor-pointer group flex flex-col lg:grid lg:grid-cols-12 gap-3 lg:items-center ${
                    isSelectedForCompare ? 'bg-indigo-950/20' : ''
                  }`}
                >
                  {/* Company Info */}
                  <div className={`${statusFilter === 'closed' ? 'lg:col-span-4' : 'lg:col-span-3'} flex items-center justify-between lg:justify-start gap-3 min-w-0`}>
                    <div className="flex items-center gap-3 min-w-0">
                      <CompanyLogo
                        name={ipo.name}
                        symbol={ipo.symbol}
                        size="md"
                        className="rounded-xl shadow-md shrink-0"
                      />
                      <div className="min-w-0">
                        <div className="flex items-center gap-1.5 flex-wrap">
                          <span className="font-bold text-white text-sm sm:text-base group-hover:text-slate-200 transition-colors truncate">
                            {ipo.name}
                          </span>
                          {ipo.ipo_type === 'SME' && (
                            <span className="px-1.5 py-0.2 rounded text-[9px] font-semibold uppercase bg-amber-500/10 text-amber-300 border border-amber-500/30 shrink-0">
                              SME
                            </span>
                          )}
                          <span className="lg:hidden shrink-0">
                            {renderAISuggestion(ipo)}
                          </span>
                        </div>
                        <span className="text-xs text-slate-400 truncate block mt-0.5">
                          {ipo.sector}
                        </span>
                      </div>
                    </div>

                    {/* Compare Button on Mobile / Desktop */}
                    <button
                      onClick={(e) => toggleCompare(ipo.id, e)}
                      className={`text-[10px] px-2 py-0.5 rounded-lg border font-medium transition-colors shrink-0 lg:ml-auto ${
                        isSelectedForCompare
                          ? 'bg-indigo-600 text-white border-indigo-500'
                          : 'bg-slate-950 text-slate-400 border-slate-800 hover:text-white'
                      }`}
                      title="Add to side-by-side comparison"
                    >
                      {isSelectedForCompare ? '✓ In Compare' : '+ Compare'}
                    </button>
                  </div>

                  {/* Dates */}
                  <div className="hidden lg:block lg:col-span-2 text-xs">
                    {statusFilter === 'open' ? (
                      <span className={`font-semibold ${ipo.closes_today ? 'text-amber-400 animate-pulse font-bold' : 'text-slate-200'}`}>
                        {ipo.closes_today ? '⚡ Closes Today!' : (ipo.close_date || 'Live')}
                      </span>
                    ) : statusFilter === 'closed' ? (
                      <span className="font-semibold text-slate-200">
                        {ipo.listing_date || ipo.close_date || 'Listed'}
                      </span>
                    ) : (
                      <span className="font-semibold text-slate-200">
                        {ipo.open_date || 'Announced'}
                      </span>
                    )}
                    <span className="text-[10px] text-slate-500 block mt-0.5">
                      {statusFilter === 'open' ? (ipo.open_date ? `Opened ${ipo.open_date}` : 'Open Now') : 'Bidding closed'}
                    </span>
                  </div>

                  {/* Price & Lot */}
                  <div className="hidden lg:block lg:col-span-2 text-xs">
                    <span className="font-bold text-white block">{ipo.price_band}</span>
                    <span className="text-[10px] text-slate-400 block mt-0.5">
                      Lot: {ipo.lot_size} (₹{ipo.min_investment.toLocaleString('en-IN')})
                    </span>
                  </div>

                  {/* Expected GMP / Listing Return */}
                  <div className="hidden lg:block lg:col-span-2 text-right text-xs">
                    {statusFilter === 'closed' && listing ? (
                      <>
                        <span className={`font-extrabold text-sm block ${listing.listing_gain_percent >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                          {listing.listing_gain_percent >= 0 ? '+' : ''}{listing.listing_gain_percent.toFixed(1)}%
                        </span>
                        <span className="text-[10px] text-slate-400 block mt-0.5">
                          ₹{listing.profit_per_lot.toLocaleString('en-IN')} / lot
                        </span>
                      </>
                    ) : (
                      <>
                        <span className={`font-extrabold text-sm block ${ipo.gmp_closing_day >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                          {ipo.gmp_closing_day >= 0 ? '+' : ''}₹{ipo.gmp_closing_day} ({ipo.gmp_closing_percent.toFixed(0)}%)
                        </span>
                        <span className="text-[10px] text-slate-400 block mt-0.5">
                          Est: ₹{ipo.gmp_estimated_listing}
                        </span>
                      </>
                    )}
                  </div>

                  {/* Subscription */}
                  <div className="hidden lg:block lg:col-span-1 text-center text-xs">
                    <span className="font-bold text-slate-200 block">
                      {ipo.subscription.final_day?.total
                        ? `${ipo.subscription.final_day.total}x`
                        : ipo.subscription.day2?.total
                        ? `${ipo.subscription.day2.total}x`
                        : ipo.subscription.day1?.total
                        ? `${ipo.subscription.day1.total}x`
                        : 'Live'}
                    </span>
                    <span className="text-[10px] text-slate-500 block mt-0.5">Total</span>
                  </div>

                  {/* 6th Column: AI Suggestion on Table for Open/Upcoming, OR Check Allotment for Closed */}
                  {statusFilter === 'closed' ? (
                    <div className="hidden lg:flex lg:col-span-1 justify-end items-center">
                      <button
                        onClick={handleCheckAllotment}
                        className="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold text-xs inline-flex items-center gap-1 transition-all active:scale-95 cursor-pointer"
                        title="Check allotment status on KFintech"
                      >
                        <span>Allotment</span>
                        <ExternalLink className="w-3 h-3" />
                      </button>
                    </div>
                  ) : (
                    <div className="hidden lg:flex lg:col-span-2 justify-end items-center">
                      {renderAISuggestion(ipo)}
                    </div>
                  )}

                  {/* Mobile Row Quick Details */}
                  <div className="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs lg:hidden pt-2 border-t border-slate-800/60 mt-1">
                    <div>
                      <span className="text-[10px] text-slate-500 block">Price & Lot</span>
                      <span className="font-semibold text-white">{ipo.price_band}</span>
                      <span className="text-[10px] text-slate-400 block">Lot: {ipo.lot_size}</span>
                    </div>

                    <div className="text-right sm:text-left">
                      <span className="text-[10px] text-slate-500 block">
                        {statusFilter === 'closed' ? 'Listing Gain' : 'Expected GMP'}
                      </span>
                      {statusFilter === 'closed' && listing ? (
                        <span className={`font-bold text-xs ${listing.listing_gain_percent >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                          {listing.listing_gain_percent >= 0 ? '+' : ''}{listing.listing_gain_percent.toFixed(1)}% (₹{listing.profit_per_lot.toLocaleString('en-IN')})
                        </span>
                      ) : (
                        <span className={`font-bold text-xs ${ipo.gmp_closing_day >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                          {ipo.gmp_closing_day >= 0 ? '+' : ''}₹{ipo.gmp_closing_day} ({ipo.gmp_closing_percent.toFixed(0)}%)
                        </span>
                      )}
                    </div>

                    <div className="col-span-2 sm:col-span-1 flex items-center justify-between sm:justify-end gap-2 pt-1 sm:pt-0">
                      <span className="text-[11px] text-slate-400">
                        Sub: <strong className="text-slate-200">{ipo.subscription.final_day?.total ?? ipo.subscription.day2?.total ?? 'Live'}x</strong>
                      </span>

                      {statusFilter === 'closed' ? (
                        <button
                          onClick={handleCheckAllotment}
                          className="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold text-xs inline-flex items-center gap-1 transition-all active:scale-95 cursor-pointer"
                        >
                          <span>Check Allotment</span>
                          <ExternalLink className="w-3 h-3" />
                        </button>
                      ) : (
                        <span className="text-emerald-400 font-bold text-xs inline-flex items-center gap-1">
                          <span>Details</span>
                          <ChevronRight className="w-3.5 h-3.5" />
                        </span>
                      )}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>

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

