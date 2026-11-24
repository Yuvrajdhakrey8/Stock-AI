import type { RecentSearchItem } from '../types';

const STORAGE_KEY = 'stockly_recent_searches';
const MAX_RECENT = 8;

export const getRecentSearches = (): RecentSearchItem[] => {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return [];
    const parsed = JSON.parse(raw);
    if (Array.isArray(parsed)) {
      return parsed;
    }
    return [];
  } catch {
    return [];
  }
};

export const saveRecentSearch = (stock: {
  symbol: string;
  name?: string;
  sector?: string;
  current_price?: number;
  change_percent?: number;
}): RecentSearchItem[] => {
  if (!stock || !stock.symbol) return getRecentSearches();

  try {
    const current = getRecentSearches();
    const cleanSym = stock.symbol.trim().toUpperCase();
    const cleanName = stock.name || cleanSym.replace('.NS', '').replace('.BO', '');

    // Deduplicate
    const filtered = current.filter((item) => item.symbol.toUpperCase() !== cleanSym);

    const newItem: RecentSearchItem = {
      symbol: cleanSym,
      name: cleanName,
      sector: stock.sector,
      current_price: stock.current_price,
      change_percent: stock.change_percent,
      timestamp: Date.now(),
    };

    const updated = [newItem, ...filtered].slice(0, MAX_RECENT);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(updated));

    // Dispatch custom event so all views update reactively
    window.dispatchEvent(new Event('stockly_recent_searches_updated'));

    return updated;
  } catch {
    return getRecentSearches();
  }
};

export const removeRecentSearch = (symbol: string): RecentSearchItem[] => {
  try {
    const current = getRecentSearches();
    const updated = current.filter((item) => item.symbol.toUpperCase() !== symbol.toUpperCase());
    localStorage.setItem(STORAGE_KEY, JSON.stringify(updated));
    window.dispatchEvent(new Event('stockly_recent_searches_updated'));
    return updated;
  } catch {
    return getRecentSearches();
  }
};

export const clearRecentSearches = (): void => {
  try {
    localStorage.removeItem(STORAGE_KEY);
    window.dispatchEvent(new Event('stockly_recent_searches_updated'));
  } catch {
    // Ignore
  }
};
