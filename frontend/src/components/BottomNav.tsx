import React from 'react';
import { TrendingUp, SlidersHorizontal, Flame, Bookmark } from 'lucide-react';

export type NavTabType = 'explore' | 'screener' | 'ipo' | 'watchlist';

interface BottomNavProps {
  activeTab: NavTabType;
  setActiveTab: (tab: NavTabType) => void;
  openIpoCount?: number;
  watchlistCount: number;
  currentSymbol: string | null;
  onBackFromStock?: () => void;
}

export const BottomNav: React.FC<BottomNavProps> = ({
  activeTab,
  setActiveTab,
  openIpoCount = 0,
  watchlistCount = 0,
  currentSymbol,
  onBackFromStock,
}) => {
  const handleTabClick = (tab: NavTabType) => {
    // If user is inside a stock detail and taps any tab, clear stock view
    if (currentSymbol && onBackFromStock) {
      onBackFromStock();
    }
    setActiveTab(tab);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <nav
      className="md:hidden fixed bottom-0 left-0 right-0 z-40 bg-slate-950/95 backdrop-blur-md border-t border-slate-800/80 shadow-2xl pb-[max(env(safe-area-inset-bottom),6px)]"
      aria-label="Mobile Navigation"
    >
      <div className="grid grid-cols-4 h-14 items-center px-1">
        {/* Tab 1: Explore / Stocks */}
        <button
          onClick={() => handleTabClick('explore')}
          className={`flex flex-col items-center justify-center py-1 transition-colors select-none cursor-pointer ${
            activeTab === 'explore'
              ? 'text-teal-400 font-semibold'
              : 'text-slate-400 hover:text-slate-200'
          }`}
        >
          <TrendingUp className="w-5 h-5 transition-transform active:scale-90" />
          <span className="text-[10px] mt-1 tracking-tight">Explore</span>
          {activeTab === 'explore' && (
            <span className="w-1 h-1 rounded-full bg-teal-400 mt-0.5" />
          )}
        </button>

        {/* Tab 2: Screener */}
        <button
          onClick={() => handleTabClick('screener')}
          className={`flex flex-col items-center justify-center py-1 transition-colors select-none cursor-pointer ${
            activeTab === 'screener'
              ? 'text-teal-400 font-semibold'
              : 'text-slate-400 hover:text-slate-200'
          }`}
        >
          <SlidersHorizontal className="w-5 h-5 transition-transform active:scale-90" />
          <span className="text-[10px] mt-1 tracking-tight">Screener</span>
          {activeTab === 'screener' && (
            <span className="w-1 h-1 rounded-full bg-teal-400 mt-0.5" />
          )}
        </button>

        {/* Tab 3: IPO Radar */}
        <button
          onClick={() => handleTabClick('ipo')}
          className={`relative flex flex-col items-center justify-center py-1 transition-colors select-none cursor-pointer ${
            activeTab === 'ipo'
              ? 'text-teal-400 font-semibold'
              : 'text-slate-400 hover:text-slate-200'
          }`}
        >
          <div className="relative">
            <Flame className="w-5 h-5 transition-transform active:scale-90" />
            {openIpoCount > 0 && (
              <span className="absolute -top-1 -right-2 bg-rose-500 text-white text-[9px] font-bold px-1 rounded-full min-w-[14px] text-center">
                {openIpoCount}
              </span>
            )}
          </div>
          <span className="text-[10px] mt-1 tracking-tight">IPO Radar</span>
          {activeTab === 'ipo' && (
            <span className="w-1 h-1 rounded-full bg-teal-400 mt-0.5" />
          )}
        </button>

        {/* Tab 4: Watchlist */}
        <button
          onClick={() => handleTabClick('watchlist')}
          className={`relative flex flex-col items-center justify-center py-1 transition-colors select-none cursor-pointer ${
            activeTab === 'watchlist'
              ? 'text-teal-400 font-semibold'
              : 'text-slate-400 hover:text-slate-200'
          }`}
        >
          <div className="relative">
            <Bookmark className="w-5 h-5 transition-transform active:scale-90" />
            {watchlistCount > 0 && (
              <span className="absolute -top-1 -right-2 bg-slate-700 text-slate-100 text-[9px] font-bold px-1 rounded-full min-w-[14px] text-center border border-slate-600">
                {watchlistCount}
              </span>
            )}
          </div>
          <span className="text-[10px] mt-1 tracking-tight">Watchlist</span>
          {activeTab === 'watchlist' && (
            <span className="w-1 h-1 rounded-full bg-teal-400 mt-0.5" />
          )}
        </button>
      </div>
    </nav>
  );
};
