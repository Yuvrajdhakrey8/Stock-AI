import { X, Trash2, Bookmark } from 'lucide-react';

export interface WatchlistEntry {
  symbol: string;
  name: string;
  exchange: string;
  current_price: number;
  verdict: string;
}

interface WatchlistDrawerProps {
  isOpen: boolean;
  onClose: () => void;
  watchlist: WatchlistEntry[];
  onSelectStock: (symbol: string) => void;
  onRemoveFromWatchlist: (symbol: string) => void;
}

export const WatchlistDrawer: React.FC<WatchlistDrawerProps> = ({
  isOpen,
  onClose,
  watchlist,
  onSelectStock,
  onRemoveFromWatchlist,
}) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex justify-end">
      {/* Backdrop */}
      <div className="fixed inset-0 bg-black/60 backdrop-blur-sm" onClick={onClose} />

      {/* Drawer content */}
      <div className="relative w-full max-w-md bg-slate-900 border-l border-slate-800 h-full p-6 flex flex-col shadow-2xl z-10">
        {/* Header */}
        <div className="flex items-center justify-between pb-4 border-b border-slate-800">
          <div className="flex items-center gap-2">
            <Bookmark className="w-5 h-5 text-amber-400" />
            <h3 className="text-lg font-bold text-white">Your Watchlist</h3>
            <span className="text-xs bg-slate-800 text-slate-300 px-2 py-0.5 rounded-full font-semibold">
              {watchlist.length}
            </span>
          </div>
          <button
            onClick={onClose}
            className="p-2 rounded-xl text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* List of Stocks */}
        <div className="flex-1 overflow-y-auto divide-y divide-slate-800/80 py-2">
          {watchlist.length === 0 ? (
            <div className="h-64 flex flex-col items-center justify-center text-center text-slate-500 space-y-2">
              <Bookmark className="w-10 h-10 text-slate-600 stroke-1" />
              <p className="text-sm">Your watchlist is currently empty.</p>
              <p className="text-xs text-slate-600">
                Click the "Watchlist" button on any stock to track it here.
              </p>
            </div>
          ) : (
            watchlist.map((item) => (
              <div
                key={item.symbol}
                onClick={() => {
                  onSelectStock(item.symbol);
                  onClose();
                }}
                className="py-3.5 px-2 hover:bg-slate-800/50 rounded-xl cursor-pointer flex items-center justify-between group transition-colors"
              >
                <div>
                  <div className="font-semibold text-white group-hover:text-emerald-400 text-sm transition-colors">
                    {item.name}
                  </div>
                  <div className="flex items-center gap-2 text-xs text-slate-400 mt-0.5">
                    <span className="font-mono text-slate-300 font-medium">{item.symbol}</span>
                    <span>•</span>
                    <span className="text-[10px] px-1.5 py-0.2 rounded bg-slate-800 text-slate-300 font-bold">
                      {item.exchange}
                    </span>
                  </div>
                </div>

                <div className="flex items-center gap-3">
                  <div className="text-right">
                    <div className="font-bold text-white text-xs">
                      ₹{item.current_price?.toLocaleString('en-IN', { minimumFractionDigits: 2 })}
                    </div>
                    <span
                      className={`text-[10px] font-bold px-1.5 py-0.5 rounded ${
                        item.verdict === 'BEST BUY'
                          ? 'bg-emerald-500/20 text-emerald-400'
                          : item.verdict === 'CURRENTLY EXPENSIVE'
                          ? 'bg-rose-500/20 text-rose-400'
                          : 'bg-amber-500/20 text-amber-400'
                      }`}
                    >
                      {item.verdict}
                    </span>
                  </div>

                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      onRemoveFromWatchlist(item.symbol);
                    }}
                    className="p-1.5 text-slate-500 hover:text-rose-400 rounded-lg hover:bg-slate-800 transition-colors"
                    title="Remove from Watchlist"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
};
