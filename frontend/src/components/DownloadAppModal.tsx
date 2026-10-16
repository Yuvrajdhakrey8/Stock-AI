import React, { useState, useEffect } from 'react';
import {
  Smartphone,
  Download,
  X,
  CheckCircle2,
  ShieldCheck,
  Zap,
  Sparkles,
  ArrowRight,
} from 'lucide-react';
import { Capacitor } from '@capacitor/core';

interface DownloadAppModalProps {
  forceOpen?: boolean;
  onClose?: () => void;
}

export const DownloadAppModal: React.FC<DownloadAppModalProps> = ({ forceOpen = false, onClose }) => {
  const [isVisible, setIsVisible] = useState<boolean>(false);
  const [deferredPrompt, setDeferredPrompt] = useState<any>(null);

  useEffect(() => {
    // If running inside the native Android app itself, never show the download prompt!
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
      // Ignore localStorage read errors
    }

    // Capture PWA install prompt if available
    const handleBeforeInstall = (e: Event) => {
      e.preventDefault();
      setDeferredPrompt(e);
    };
    window.addEventListener('beforeinstallprompt', handleBeforeInstall);

    // Show banner after 4 seconds of reading stocks
    const timer = setTimeout(() => {
      setIsVisible(true);
    }, 4000);

    return () => {
      clearTimeout(timer);
      window.removeEventListener('beforeinstallprompt', handleBeforeInstall);
    };
  }, [forceOpen]);

  const handleDismiss = () => {
    setIsVisible(false);
    try {
      // Don't show again for 3 days
      localStorage.setItem('dhakreystock_app_prompt_dismissed', (Date.now() + 3 * 24 * 60 * 60 * 1000).toString());
    } catch {
      // Ignore
    }
    if (onClose) onClose();
  };

  const handlePWAInstall = async () => {
    if (deferredPrompt) {
      deferredPrompt.prompt();
      const choiceResult = await deferredPrompt.userChoice;
      if (choiceResult.outcome === 'accepted') {
        setIsVisible(false);
      }
      setDeferredPrompt(null);
    } else {
      // Direct APK download link or GitHub release
      handleDirectDownload();
    }
  };

  const handleDirectDownload = () => {
    // Triggers direct download of the built Android APK file
    // Hosted statically or via release
    const link = document.createElement('a');
    link.href = '/dhakreystock-ai.apk';
    link.download = 'DhakreyStock-AI.apk';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  if (!isVisible) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-end sm:items-center justify-center p-3 sm:p-4 bg-black/60 backdrop-blur-sm animate-in fade-in duration-200">
      <div className="relative w-full max-w-lg bg-gradient-to-b from-slate-900 to-slate-950 border border-slate-700/80 rounded-3xl p-5 sm:p-6 shadow-2xl overflow-hidden">
        {/* Glowing Decorative Background Accent */}
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
              <Sparkles className="w-3 h-3" /> Android Mobile App
            </div>
            <h3 className="text-base sm:text-lg font-bold text-white tracking-tight">
              Download DhakreyStock AI App
            </h3>
          </div>
        </div>

        {/* Feature Highlights */}
        <div className="mt-4 p-3.5 rounded-2xl bg-slate-950/70 border border-slate-800 text-xs space-y-2">
          <div className="flex items-center gap-2 text-slate-300">
            <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
            <span><strong>Instant Stock Fair Value:</strong> DCF & Graham intrinsic price engine.</span>
          </div>
          <div className="flex items-center gap-2 text-slate-300">
            <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
            <span><strong>Live IPO GMP & Closes Today:</strong> Never miss closing day bidding.</span>
          </div>
          <div className="flex items-center gap-2 text-slate-300">
            <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
            <span><strong>Zero-Lag Native Experience:</strong> Fullscreen app without browser frame.</span>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="mt-5 space-y-2.5">
          <button
            onClick={deferredPrompt ? handlePWAInstall : handleDirectDownload}
            className="w-full py-3 px-4 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-extrabold text-xs sm:text-sm flex items-center justify-center gap-2 shadow-lg shadow-emerald-500/25 transition-all active:scale-[0.98]"
          >
            <Download className="w-4 h-4 shrink-0" />
            <span>{deferredPrompt ? 'Install App on Phone' : 'Download Android App (.APK)'}</span>
            <ArrowRight className="w-4 h-4 shrink-0" />
          </button>

          <div className="flex items-center justify-between text-[11px] text-slate-400 px-1">
            <span className="flex items-center gap-1 text-slate-500">
              <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" /> 100% Free & Verified
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
