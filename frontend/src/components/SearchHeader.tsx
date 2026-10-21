import React, { useState, useEffect, useRef } from 'react';
import { Search, Building2, ChevronRight, Sparkles, Loader2, X } from 'lucide-react';
import type { StockSearchResult } from '../types';
import { CompanyLogo } from './CompanyLogo';
import { API_BASE_URL } from '../config';

interface SearchHeaderProps {
  onSelectStock: (symbol: string) => void;
  currentSymbol?: string;
}

const POPULAR_STOCKS = [
  { symbol: 'RELIANCE.NS', name: 'Reliance' },
  { symbol: 'TCS.NS', name: 'TCS' },
  { symbol: 'HDFCBANK.NS', name: 'HDFC Bank' },
  { symbol: 'TATAMOTORS.NS', name: 'Tata Motors' },
  { symbol: 'INFY.NS', name: 'Infosys' },
  { symbol: 'ETERNAL.NS', name: 'Zomato (Eternal)' },
  { symbol: 'ITC.NS', name: 'ITC' },
  { symbol: 'SBIN.NS', name: 'SBI' },
  { symbol: 'HAL.NS', name: 'HAL' },
];

export const SearchHeader: React.FC<SearchHeaderProps> = ({ onSelectStock, currentSymbol }) => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<StockSearchResult[]>([]);
  const [isOpen, setIsOpen] = useState(false);
  const [loading, setLoading] = useState(false);
  const [selectedIndex, setSelectedIndex] = useState<number>(-1);
  const dropdownRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  // Debounced search with snappier 150ms timeout
  useEffect(() => {
    if (!query.trim()) {
      setResults([]);
      setIsOpen(false);
      setSelectedIndex(-1);
      return;
    }

    setIsOpen(true);
    const timer = setTimeout(async () => {
      setLoading(true);
      try {
        const res = await fetch(`${API_BASE_URL}/api/search?q=${encodeURIComponent(query.trim())}`);
        if (res.ok) {
          const data = await res.json();
          setResults(data.results || []);
          setSelectedIndex(-1);
        }
      } catch (err) {
        console.error('Search error:', err);
      } finally {
        setLoading(false);
      }
    }, 150);

    return () => clearTimeout(timer);
  }, [query]);

  // Click outside listener
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target as Node)) {
        setIsOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const handleSelect = (symbol: string) => {
    onSelectStock(symbol);
    setIsOpen(false);
    setQuery('');
    setSelectedIndex(-1);
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (!isOpen || results.length === 0) return;

    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setSelectedIndex((prev) => (prev < results.length - 1 ? prev + 1 : 0));
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      setSelectedIndex((prev) => (prev > 0 ? prev - 1 : results.length - 1));
    } else if (e.key === 'Escape') {
      setIsOpen(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (results.length > 0) {
      const chosen = selectedIndex >= 0 && selectedIndex < results.length ? results[selectedIndex] : results[0];
      handleSelect(chosen.symbol);
      return;
    }

    const cleanQ = query.trim();
    if (!cleanQ) return;

    // Fast-path resolution before falling back
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE_URL}/api/search?q=${encodeURIComponent(cleanQ)}`);
      if (res.ok) {
        const data = await res.json();
        if (data.results && data.results.length > 0) {
          handleSelect(data.results[0].symbol);
          return;
        }
      }
    } catch {
      // Fallback
    } finally {
      setLoading(false);
    }

    let sym = cleanQ.toUpperCase();
    if (!sym.includes('.')) {
      sym = `${sym}.NS`;
    }
    handleSelect(sym);
  };

  return (
    <div className="w-full relative" ref={dropdownRef}>
      {/* Search Input Box */}
      <form onSubmit={handleSubmit} className="relative">
        <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-slate-400">
          {loading ? (
            <Loader2 className="w-5 h-5 animate-spin text-emerald-400" />
          ) : (
            <Search className="w-5 h-5" />
          )}
        </div>
        <input
          ref={inputRef}
          type="search"
          enterKeyHint="search"
          autoCapitalize="characters"
          autoCorrect="off"
          spellCheck="false"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={handleKeyDown}
          onFocus={() => {
            if (query.trim()) setIsOpen(true);
          }}
          placeholder="Search Indian stocks (e.g. Muthoot Finance, Tata Motors, RELIANCE, TCS)..."
          className="w-full pl-11 pr-10 py-3 sm:py-3.5 bg-slate-900/90 border border-slate-700/80 rounded-2xl text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 focus:border-emerald-500 transition-all text-xs sm:text-sm shadow-inner shadow-black/20"
        />
        {query && (
          <button
            type="button"
            onClick={() => {
              setQuery('');
              setResults([]);
              setIsOpen(false);
            }}
            className="absolute inset-y-0 right-0 pr-3.5 flex items-center text-slate-400 hover:text-slate-200"
          >
            <X className="w-4 h-4" />
          </button>
        )}
      </form>

      {/* Autocomplete Dropdown */}
      {isOpen && query.trim() && (
        <div className="absolute left-0 right-0 mt-2 bg-slate-900 border border-slate-700/80 rounded-2xl shadow-2xl z-[100] overflow-hidden divide-y divide-slate-800 max-h-80 sm:max-h-96 overflow-y-auto">
          {loading && results.length === 0 ? (
            <div className="p-4 text-center text-slate-400 text-xs sm:text-sm flex items-center justify-center gap-2">
              <Loader2 className="w-4 h-4 animate-spin text-emerald-400" />
              <span>Searching listed Indian stocks across NSE & BSE...</span>
            </div>
          ) : results.length > 0 ? (
            <>
              <div className="px-3.5 py-2 bg-slate-950/80 text-[10px] sm:text-[11px] font-semibold text-slate-400 uppercase tracking-wider flex justify-between items-center">
                <span>Matching Indian Equities (NSE & BSE)</span>
                <span>{results.length} results</span>
              </div>
              {results.map((item, idx) => (
                <div
                  key={item.symbol}
                  onClick={() => handleSelect(item.symbol)}
                  className={`px-3.5 sm:px-4 py-2.5 sm:py-3 cursor-pointer flex items-center justify-between transition-colors group active:bg-slate-800 ${
                    selectedIndex === idx ? 'bg-slate-800 ring-1 ring-emerald-500/30' : 'hover:bg-slate-800/80'
                  }`}
                >
                  <div className="flex items-center gap-2.5 sm:gap-3 min-w-0">
                    <CompanyLogo
                      name={item.name}
                      symbol={item.symbol}
                      size="sm"
                      className="rounded-lg shrink-0"
                    />
                    <div className="min-w-0">
                      <div className="flex items-center gap-1.5 sm:gap-2 flex-wrap">
                        <span className="font-semibold text-slate-100 group-hover:text-emerald-400 transition-colors text-xs sm:text-sm truncate">
                          {item.name}
                        </span>
                        <span className="text-[9px] sm:text-[10px] font-bold px-1.5 py-0.2 rounded bg-emerald-950 text-emerald-400 border border-emerald-800/60 shrink-0">
                          {item.exchange || 'NSE'}
                        </span>
                        {item.index && (
                          <span className="text-[9px] sm:text-[10px] font-medium px-1.5 py-0.2 rounded bg-slate-800 text-slate-300 shrink-0">
                            {item.index}
                          </span>
                        )}
                      </div>
                      <div className="text-[11px] sm:text-xs text-slate-400 flex items-center gap-1.5 sm:gap-2 mt-0.5">
                        <span className="font-mono text-slate-300 font-medium">{item.symbol}</span>
                        <span>•</span>
                        <span className="truncate">{item.sector}</span>
                      </div>
                    </div>
                  </div>
                  <ChevronRight className="w-4 h-4 text-slate-500 group-hover:text-emerald-400 group-hover:translate-x-0.5 transition-all shrink-0 ml-2" />
                </div>
              ))}
            </>
          ) : (
            <div className="p-4 text-center text-slate-400 text-xs sm:text-sm">
              No matching stocks found for <span className="text-white font-semibold">"{query}"</span>. Press Enter to search on exchange.
            </div>
          )}
        </div>
      )}

      {/* Popular Fast Chips */}
      <div className="flex items-center gap-1.5 sm:gap-2 mt-2.5 sm:mt-3 overflow-x-auto pb-1 scrollbar-none text-xs -mx-1 px-1">
        <span className="text-slate-400 flex items-center gap-1 font-medium whitespace-nowrap shrink-0 text-[11px] sm:text-xs">
          <Sparkles className="w-3.5 h-3.5 text-amber-400 shrink-0" />
          Quick Picks:
        </span>
        {POPULAR_STOCKS.map((stock) => {
          const isActive = currentSymbol === stock.symbol;
          return (
            <button
              key={stock.symbol}
              onClick={() => onSelectStock(stock.symbol)}
              className={`px-2.5 sm:px-3 py-1 rounded-lg border whitespace-nowrap transition-all font-medium text-[11px] sm:text-xs shrink-0 active:scale-95 ${
                isActive
                  ? 'bg-emerald-500/20 text-emerald-400 border-emerald-500/60 font-semibold'
                  : 'bg-slate-900/60 border-slate-800 text-slate-300 hover:border-slate-700 hover:text-white'
              }`}
            >
              {stock.name}
            </button>
          );
        })}
      </div>
    </div>
  );
};
