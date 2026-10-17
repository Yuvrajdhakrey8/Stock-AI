import React, { useState, useEffect } from 'react';
import {
  Smartphone,
  Download,
  X,
  CheckCircle2,
  ShieldCheck,
  Sparkles,
  ArrowRight,
  ExternalLink,
} from 'lucide-react';
import { Capacitor } from '@capacitor/core';

interface DownloadAppModalProps {
  forceOpen?: boolean;
  onClose?: () => void;
}

export const DownloadAppModal: React.FC<DownloadAppModalProps> = ({ forceOpen = false, onClose }) => {
  const [isVisible, setIsVisible] = useState<boolean>(false);

  useEffect(() => {
    // If running inside native Android app, never show download prompt
    if (Capacitor.isNativePlatform()) {
      return;
    }

    if (forceOpen) {
      setIsVisible(true);
      return;
    }

    // Check if dismissed recently (within last 3 days)
    try {
      const dismissedUntil = localStorage.getItem('dhakreystock_app_prompt_dismissed');
      if (dismissedUntil && Date.now() < parseInt(dismissedUntil, 10)) {
        return;
      }
    } catch {
      // Ignore
    }

    const timer = setTimeout(() => {
      setIsVisible(true);
    }, 4000);

    return () => clearTimeout(timer);
  }, [forceOpen]);

  const handleDismiss = () => {
    setIsVisible(false);
    try {
      localStorage.setItem('dhakreystock_app_prompt_dismissed', (Date.now() + 3 * 24 * 60 * 60 * 1000).toString());
    } catch {
      // Ignore
    }
    if (onClose) onClose();
  };

  const handleAPKDownload = () => {
    // Link directly to the GitHub Actions compiled release APK
    const apkUrl = 'https://github.com/Yuvrajdhakrey8/Stock-AI/releases/download/mobile-latest/DhakreyStock-AI.apk';
    window.location.href = apkUrl;
  };

  if (!isVisible) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-end sm:items-center justify-center p-3 sm:p-4 bg-black/65 backdrop-blur-sm animate-in fade-in duration-200">
      <div className="relative w-full max-w-lg bg-gradient-to-b from-slate-900 to-slate-950 border border-slate-700/80 rounded-3xl p-5 sm:p-6 shadow-2xl overflow-hidden">
        {/* Decorative Ambient Glow */}
        <div className="absolute top-0 right-0 -mr-16 -mt-16 w-48 h-48 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="absolute bottom-0 left-0 -ml-16 -mb-16 w-48 h-48 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none" />

        {/* Close Button */}
        <button
          onClick={handleDismiss}
          className="absolute top-4 right-4 p-1.5 rounded-full text-slate-400 hover:text-white bg-slate-800/60 hover:bg-slate-800 border border-slate-700/60 transition-colors"
          title="Dismiss"
        >
          <X className="w-4 h-4" />
        </button>

        {/* Header with App Icon */}
        <div className="flex items-center gap-3.5 pr-8">
          <div className="w-12 h-12 rounded-2xl bg-gradient-to-tr from-emerald-500 to-teal-400 flex items-center justify-center shadow-lg shadow-emerald-500/20 shrink-0">
            <Smartphone className="w-6 h-6 text-slate-950" />
          </div>
          <div>
            <div className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-[10px] font-bold text-emerald-400 uppercase tracking-wider mb-0.5">
              <Sparkles className="w-3 h-3" /> Android APK
            </div>
            <h3 className="text-base sm:text-lg font-bold text-white tracking-tight">
              Download Stocks Suggestions - Dhakrey App
            </h3>
          </div>
        </div>

        {/* Feature Highlights */}
        <div className="mt-4 p-3.5 rounded-2xl bg-slate-950/70 border border-slate-800 text-xs space-y-2">
          <div className="flex items-center gap-2 text-slate-300">
            <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
            <span><strong>Instant Stock Fair Value:</strong> DCF & Graham intrinsic valuation models.</span>
          </div>
          <div className="flex items-center gap-2 text-slate-300">
            <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
            <span><strong>Live IPO GMP & Subscriptions:</strong> Real-time Indian equity IPO tracking.</span>
          </div>
          <div className="flex items-center gap-2 text-slate-300">
            <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
            <span><strong>Native Android Performance:</strong> Smooth full-screen experience on your phone.</span>
          </div>
        </div>

        {/* Action Button */}
        <div className="mt-5 space-y-2.5">
          <button
            onClick={handleAPKDownload}
            className="w-full py-3.5 px-4 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-extrabold text-xs sm:text-sm flex items-center justify-center gap-2 shadow-lg shadow-emerald-500/25 transition-all active:scale-[0.98]"
          >
            <Download className="w-4 h-4 shrink-0" />
            <span>Download Android App (.APK)</span>
            <ArrowRight className="w-4 h-4 shrink-0" />
          </button>

          <div className="flex items-center justify-between text-[11px] text-slate-400 px-1 pt-1">
            <span className="flex items-center gap-1 text-slate-500">
              <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" /> Free & Safe for Android
            </span>
            <button
              onClick={handleDismiss}
              className="hover:text-slate-300 transition-colors"
            >
              Continue in Browser
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
