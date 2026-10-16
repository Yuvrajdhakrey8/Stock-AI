import { Capacitor } from '@capacitor/core';
import {
  AdMob,
  type BannerAdOptions,
  BannerAdSize,
  BannerAdPosition,
  type AdOptions,
} from '@capacitor-community/admob';

/**
 * AdMob Service for DhakreyStock AI Native Mobile App.
 * Uses official Google Test Ad Unit IDs by default to prevent account flags.
 * Replace with real AdMob Ad Unit IDs from https://admob.google.com when releasing to production.
 */
class AdService {
  private isInitialized = false;

  // Official Google Test IDs for Android
  private bannerAdId = 'ca-app-pub-3940256099942544/6300978111';
  private interstitialAdId = 'ca-app-pub-3940256099942544/1033173712';

  public async initialize(): Promise<void> {
    if (!Capacitor.isNativePlatform() || this.isInitialized) {
      return;
    }

    try {
      await AdMob.initialize({
        initializeForTesting: true,
      });
      this.isInitialized = true;
      console.log('AdMob successfully initialized on mobile platform.');

      // Automatically show bottom banner
      await this.showBottomBanner();
    } catch (error) {
      console.warn('AdMob initialization skipped or failed:', error);
    }
  }

  public async showBottomBanner(): Promise<void> {
    if (!Capacitor.isNativePlatform()) return;

    try {
      const options: BannerAdOptions = {
        adId: this.bannerAdId,
        adSize: BannerAdSize.ADAPTIVE_BANNER,
        position: BannerAdPosition.BOTTOM_CENTER,
        margin: 0,
        isTesting: true,
      };
      await AdMob.showBanner(options);
    } catch (error) {
      console.warn('Failed to display banner ad:', error);
    }
  }

  public async hideBanner(): Promise<void> {
    if (!Capacitor.isNativePlatform()) return;
    try {
      await AdMob.hideBanner();
    } catch (error) {
      console.warn('Failed to hide banner ad:', error);
    }
  }

  public async showInterstitial(): Promise<void> {
    if (!Capacitor.isNativePlatform()) return;

    try {
      const options: AdOptions = {
        adId: this.interstitialAdId,
        isTesting: true,
      };
      await AdMob.prepareInterstitial(options);
      await AdMob.showInterstitial();
    } catch (error) {
      console.warn('Failed to display interstitial ad:', error);
    }
  }
}

export const adService = new AdService();
