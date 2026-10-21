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
import type { IPOData, IPOSummaryMetrics } from '../types';
import { IPODetailModal } from './IPODetailModal';
import { IPOCompareModal } from './IPOCompareModal';
import { CompanyLogo } from './CompanyLogo';
import { API_BASE_URL } from '../config';
import { mobileService } from '../services/mobileService';

type TabType = 'open' | 'closed' | 'upcoming';

export const IPODashboard: React.FC = () => {
  const [ipos, setIpos] = useState<IPOData[]>([]);
  const [summary, setSummary] = useState<IPOSummaryMetrics | null>(null);
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

  const [sortBy, setSortBy] = useState<'gmp' | 'gain' | 'issue_size' | 'date'>('gmp');

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
    if (sortBy === 'gain') {
      const gainA = a.listing?.listing_gain_percent ?? a.gmp_closing_percent ?? -999;
      const gainB = b.listing?.listing_gain_percent ?? b.gmp_closing_percent ?? -999;
      return gainB - gainA;
    }
    if (sortBy === 'issue_size') {
      return b.issue_size_cr - a.issue_size_cr;
    }
    return new Date(b.open_date).getTime() - new Date(a.open_date).getTime();
  });

  const comparedIPOs = ipos.filter((i) => compareIds.includes(i.id));

  // Helper function to render AI Suggestion badge
  const renderAISuggestion = (ipo: IPOData) => {
    const isListed = ipo.status === 'Listed';
    const rec = ipo.recommendation_at_ipo;
    const listing = ipo.listing;
    const missed = ipo.missed_opportunity_analysis;

    if (isListed && listing) {
      if (listing.listing_gain_percent >= 20) {
        return (
          <div className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs font-semibold">
            <span className="w-2 h-2 rounded-full bg-emerald-400 shrink-0" />
            <span>AI Review: <strong className="text-emerald-300">Stellar Gain (+{listing.listing_gain_percent.toFixed(1)}%)</strong> • ₹{listing.profit_per_lot.toLocaleString('en-IN')}/lot profit</span>
          </div>
        );
      }
      if (listing.listing_gain_percent < 0) {
        return (
          <div className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-300 text-xs font-semibold">
            <span className="w-2 h-2 rounded-full bg-rose-400 shrink-0" />
            <span>AI Review: <strong className="text-rose-300">Capital Protected</strong> • Avoided {listing.listing_gain_percent.toFixed(1)}% loss</span>
          </div>
        );
      }
      return (
        <div className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-slate-800/80 border border-slate-700/60 text-slate-300 text-xs font-semibold">
          <span className="w-2 h-2 rounded-full bg-amber-400 shrink-0" />
          <span>AI Review: <strong className="text-slate-200">Listed at Par (+{listing.listing_gain_percent.toFixed(1)}%)</strong></span>
        </div>
      );
    }

    if (ipo.status === 'Open') {
      if (ipo.gmp_closing_percent >= 25 || rec?.verdict === 'Apply') {
        return (
          <div className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs font-semibold">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse shrink-0" />
            <span>AI Suggestion: <strong className="text-emerald-300">Apply</strong> — Strong +{ipo.gmp_closing_percent.toFixed(0)}% GMP Expected</span>
          </div>
        );
      }
      if (ipo.gmp_closing_percent >= 8) {
        return (
          <div className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs font-semibold">
            <span className="w-2 h-2 rounded-full bg-amber-400 shrink-0" />
            <span>AI Suggestion: <strong className="text-amber-300">Caution</strong> — Moderate Demand ({ipo.gmp_closing_percent.toFixed(0)}% GMP)</span>
          </div>
        );
      }
      return (
        <div className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-300 text-xs font-semibold">
          <span className="w-2 h-2 rounded-full bg-rose-400 shrink-0" />
          <span>AI Suggestion: <strong className="text-rose-300">Avoid</strong> — High Valuation Risk / Subdued GMP</span>
        </div>
      );
    }

    // Upcoming
    if (ipo.gmp_closing_percent >= 20) {
      return (
        <div className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-sky-500/10 border border-sky-500/30 text-sky-300 text-xs font-semibold">
          <span className="w-2 h-2 rounded-full bg-sky-400 shrink-0" />
          <span>AI Outlook: <strong className="text-sky-300">Bullish Demand</strong> — High Grey Market Activity</span>
        </div>
      );
    }
    return (
      <div className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-slate-800/80 border border-slate-700/60 text-slate-300 text-xs font-semibold">
        <span className="w-2 h-2 rounded-full bg-slate-400 shrink-0" />
        <span>AI Outlook: <strong className="text-slate-200">Watch</strong> — Awaiting Bidding Dates & Valuation Details</span>
      </div>
    );
  };

  return (
    <div className="space-y-5">
      {/* Groww-style Page Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div>
          <div className="flex items-center gap-2">
            <h1 className="text-xl sm:text-2xl font-extrabold text-white tracking-tight flex items-center gap-2">
              <Sparkles className="w-5 h-5 sm:w-6 sm:h-6 text-emerald-400 shrink-0" />
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
            <RefreshCw className={`w-3.5 h-3.5 text-emerald-400 shrink-0 ${isRefreshing ? 'animate-spin' : ''}`} />
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

      {/* Groww 3 Categories Pill Navigation + Type Filter */}
      <div className="bg-slate-900/95 border border-slate-800 rounded-2xl p-2.5 sm:p-3 shadow-xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-3">
          {/* Exactly 3 Categories: Open, Closed, Upcoming (Groww Style) */}
          <div className="flex items-center gap-2 overflow-x-auto scrollbar-none pb-1 md:pb-0">
            {/* 1. Open Tab */}
            <button
              onClick={() => setStatusFilter('open')}
              className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all shrink-0 cursor-pointer ${
                statusFilter === 'open'
                  ? 'bg-emerald-500 text-slate-950 shadow-md shadow-emerald-500/20'
                  : 'bg-slate-950 text-slate-300 hover:text-white border border-slate-800'
              }`}
            >
              <span className={`w-2 h-2 rounded-full ${statusFilter === 'open' ? 'bg-slate-950 animate-pulse' : 'bg-emerald-400'}`} />
              <span>Open</span>
              <span className={`px-1.5 py-0.2 rounded-md text-[10px] font-extrabold ${
                statusFilter === 'open' ? 'bg-slate-950/20 text-slate-950' : 'bg-slate-800 text-slate-300'
              }`}>
                {summary?.open_count ?? 0}
              </span>
            </button>

            {/* 2. Closed Tab */}
            <button
              onClick={() => setStatusFilter('closed')}
              className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all shrink-0 cursor-pointer ${
                statusFilter === 'closed'
                  ? 'bg-emerald-500 text-slate-950 shadow-md shadow-emerald-500/20'
                  : 'bg-slate-950 text-slate-300 hover:text-white border border-slate-800'
              }`}
            >
              <span>Closed</span>
              <span className={`px-1.5 py-0.2 rounded-md text-[10px] font-extrabold ${
                statusFilter === 'closed' ? 'bg-slate-950/20 text-slate-950' : 'bg-slate-800 text-slate-300'
              }`}>
                {summary?.closed_count ?? 0}
              </span>
            </button>

            {/* 3. Upcoming Tab */}
            <button
              onClick={() => setStatusFilter('upcoming')}
              className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all shrink-0 cursor-pointer ${
                statusFilter === 'upcoming'
                  ? 'bg-emerald-500 text-slate-950 shadow-md shadow-emerald-500/20'
                  : 'bg-slate-950 text-slate-300 hover:text-white border border-slate-800'
              }`}
            >
              <span>Upcoming</span>
              <span className={`px-1.5 py-0.2 rounded-md text-[10px] font-extrabold ${
                statusFilter === 'upcoming' ? 'bg-slate-950/20 text-slate-950' : 'bg-slate-800 text-slate-300'
              }`}>
                {summary?.upcoming_count ?? 0}
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
                <option value="gmp" className="bg-slate-900 text-white">Sort by GMP %</option>
                <option value="gain" className="bg-slate-900 text-white">Sort by Listing Gain</option>
                <option value="issue_size" className="bg-slate-900 text-white">Sort by Size</option>
                <option value="date" className="bg-slate-900 text-white">Sort by Date</option>
              </select>
            </div>

            {/* Compare Button */}
            {compareIds.length > 0 && (
              <button
                onClick={() => setIsCompareOpen(true)}
                className="px-3 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs inline-flex items-center gap-1.5 shadow-lg shadow-indigo-600/20 transition-all shrink-0"
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
          <div className="py-16 text-center text-slate-400 bg-slate-900/60 rounded-3xl border border-slate-800 space-y-2">
            <Info className="w-6 h-6 text-slate-500 mx-auto" />
            <p className="font-semibold text-white">No IPOs found in this category.</p>
            <p className="text-xs text-slate-500">Try changing your search query or selecting a different IPO type.</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {sortedIPOs.map((ipo) => {
              const isListed = ipo.status === 'Listed';
              const isSelectedForCompare = compareIds.includes(ipo.id);
              const listing = ipo.listing;

              return (
                <div
                  key={ipo.id}
                  onClick={() => handleOpenDetail(ipo)}
                  className={`bg-slate-900/90 border rounded-2xl sm:rounded-3xl p-4 sm:p-5 shadow-xl hover:border-slate-700 transition-all cursor-pointer flex flex-col justify-between group relative overflow-hidden active:scale-[0.99] ${
                    isSelectedForCompare ? 'ring-2 ring-indigo-500 border-indigo-500/50' : 'border-slate-800'
                  }`}
                >
                  <div>
                    {/* Top Row: Company Logo + Name + SME chip + Compare Toggle */}
                    <div className="flex items-start justify-between gap-3">
                      <div className="flex items-start gap-3 min-w-0">
                        {/* Company Logo */}
                        <CompanyLogo
                          name={ipo.name}
                          symbol={ipo.symbol}
                          size="md"
                          className="mt-0.5 rounded-xl shadow-md"
                        />

                        {/* Name & Sector */}
                        <div className="min-w-0">
                          <div className="flex items-center gap-1.5 flex-wrap">
                            <h3 className="font-bold text-white text-sm sm:text-base group-hover:text-emerald-400 transition-colors line-clamp-1">
                              {ipo.name}
                            </h3>
                            {ipo.ipo_type === 'SME' && (
                              <span className="px-1.5 py-0.2 rounded text-[9px] font-extrabold uppercase bg-amber-500/10 text-amber-300 border border-amber-500/30">
                                SME
                              </span>
                            )}
                          </div>
                          <p className="text-[11px] text-slate-400 truncate mt-0.5">
                            {ipo.sector}
                          </p>
                        </div>
                      </div>

                      {/* Compare Checkbox */}
                      <button
                        onClick={(e) => toggleCompare(ipo.id, e)}
                        className={`text-[10px] px-2 py-0.5 rounded-lg border font-medium transition-colors shrink-0 ${
                          isSelectedForCompare
                            ? 'bg-indigo-600 text-white border-indigo-500'
                            : 'bg-slate-950 text-slate-400 border-slate-800 hover:text-white'
                        }`}
                        title="Add to side-by-side comparison"
                      >
                        {isSelectedForCompare ? '✓ In Compare' : '+ Compare'}
                      </button>
                    </div>

                    {/* Initial Essential Details Grid (Clean & Scannable - Groww Style) */}
                    <div className="grid grid-cols-2 gap-2.5 mt-3.5 pt-3 border-t border-slate-800/80 text-xs">
                      {/* Left Column */}
                      <div>
                        {statusFilter === 'open' ? (
                          <>
                            <span className="text-[10px] text-slate-500 block">Bidding Closes</span>
                            <span className={`font-bold text-xs ${ipo.closes_today ? 'text-amber-400 animate-pulse' : 'text-slate-200'}`}>
                              {ipo.closes_today ? '⚡ Closes Today!' : (ipo.close_date || 'Live')}
                            </span>
                          </>
                        ) : statusFilter === 'closed' ? (
                          <>
                            <span className="text-[10px] text-slate-500 block">Listing Date</span>
                            <span className="font-bold text-slate-200 text-xs">
                              {ipo.listing_date || ipo.close_date || 'Listed'}
                            </span>
                          </>
                        ) : (
                          <>
                            <span className="text-[10px] text-slate-500 block">Opening Date</span>
                            <span className="font-bold text-slate-200 text-xs">
                              {ipo.open_date || 'Announced'}
                            </span>
                          </>
                        )}

                        <div className="mt-2">
                          <span className="text-[10px] text-slate-500 block">Price Band</span>
                          <span className="font-semibold text-white text-xs">
                            {ipo.price_band}
                          </span>
                        </div>
                      </div>

                      {/* Right Column */}
                      <div className="text-right">
                        {statusFilter === 'closed' && listing ? (
                          <>
                            <span className="text-[10px] text-slate-500 block">Listing Return</span>
                            <span className={`font-extrabold text-xs ${listing.listing_gain_percent >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                              {listing.listing_gain_percent >= 0 ? '+' : ''}{listing.listing_gain_percent.toFixed(1)}% (₹{listing.profit_per_lot.toLocaleString('en-IN')})
                            </span>
                          </>
                        ) : (
                          <>
                            <span className="text-[10px] text-slate-500 block">Expected GMP</span>
                            <span className={`font-extrabold text-xs ${ipo.gmp_closing_day >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                              {ipo.gmp_closing_day >= 0 ? '+' : ''}₹{ipo.gmp_closing_day} ({ipo.gmp_closing_percent.toFixed(0)}%)
                            </span>
                          </>
                        )}

                        <div className="mt-2 text-right">
                          <span className="text-[10px] text-slate-500 block">Overall Subscription</span>
                          <span className="font-semibold text-slate-200 text-xs">
                            {ipo.subscription.final_day?.total
                              ? `${ipo.subscription.final_day.total}x`
                              : ipo.subscription.day2?.total
                              ? `${ipo.subscription.day2.total}x`
                              : ipo.subscription.day1?.total
                              ? `${ipo.subscription.day1.total}x`
                              : 'Live'}
                          </span>
                        </div>
                      </div>
                    </div>

                    {/* AI Suggestion Badge */}
                    <div className="mt-3">
                      {renderAISuggestion(ipo)}
                    </div>
                  </div>

                  {/* Card Bottom CTA (Click to see full details) */}
                  <div className="mt-3.5 pt-2.5 border-t border-slate-800/60 flex items-center justify-between text-xs text-slate-400">
                    <span className="text-[11px] text-slate-500 font-medium">
                      Lot: {ipo.lot_size} (₹{ipo.min_investment.toLocaleString('en-IN')})
                    </span>
                    <div className="flex items-center gap-1 font-bold text-emerald-400 group-hover:translate-x-0.5 transition-transform">
                      <span>{statusFilter === 'open' ? 'Apply / Details' : statusFilter === 'closed' ? 'Check Allotment' : 'View Details'}</span>
                      <ChevronRight className="w-3.5 h-3.5" />
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

