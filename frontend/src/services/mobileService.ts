import { Capacitor } from '@capacitor/core';
import { StatusBar, Style } from '@capacitor/status-bar';
import { App as CapApp } from '@capacitor/app';

type BackButtonHandler = () => boolean; // Returns true if back action was handled, false otherwise

class MobileService {
  private backHandlers: BackButtonHandler[] = [];
  private isInitialized = false;

  public async initialize(): Promise<void> {
    if (!Capacitor.isNativePlatform() || this.isInitialized) {
      return;
    }

    this.isInitialized = true;

    // 1. Configure Android Status Bar to match dark fintech aesthetic
    try {
      await StatusBar.setStyle({ style: Style.Dark });
      await StatusBar.setBackgroundColor({ color: '#090d16' });
      await StatusBar.setOverlaysWebView({ overlay: false });
    } catch (err) {
      console.warn('StatusBar customization not supported or skipped:', err);
    }

    // 2. Hardware / Gesture Back Button Handling for Android
    try {
      await CapApp.addListener('backButton', ({ canGoBack }) => {
        // Run handlers in reverse order (LIFO: topmost modal/state gets first chance to close)
        for (let i = this.backHandlers.length - 1; i >= 0; i--) {
          const handler = this.backHandlers[i];
          const handled = handler();
          if (handled) {
            return;
          }
        }

        // If no modal or custom handler intercepted and web history can go back
        if (canGoBack) {
          window.history.back();
        } else {
          // At the root screen, exit cleanly
          CapApp.exitApp();
        }
      });
    } catch (err) {
      console.warn('Capacitor App backButton listener registration error:', err);
    }
  }

  /**
   * Register a back button handler. Returns an unsubscribe function.
   */
  public registerBackHandler(handler: BackButtonHandler): () => void {
    this.backHandlers.push(handler);
    return () => {
      this.backHandlers = this.backHandlers.filter((h) => h !== handler);
    };
  }

  public isNative(): boolean {
    return Capacitor.isNativePlatform();
  }
}

export const mobileService = new MobileService();
