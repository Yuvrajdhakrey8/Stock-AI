import { Capacitor } from '@capacitor/core';

/**
 * DhakreyStock AI - Frontend Configuration
 * Default AWS API Gateway endpoint for production cloud & mobile app.
 */
const AWS_API_GATEWAY_URL = 'https://uwztv3c9l6.execute-api.ap-south-1.amazonaws.com';

function resolveApiBaseUrl(): string {
  // If explicitly provided via environment variable at build/run time
  if (import.meta.env.VITE_API_BASE_URL) {
    return import.meta.env.VITE_API_BASE_URL.replace(/\/$/, '');
  }

  // Inside Capacitor Native App (Android/iOS)
  if (Capacitor.isNativePlatform()) {
    return AWS_API_GATEWAY_URL;
  }

  // In local browser development (Vite dev server at localhost:5173 uses Vite proxy to local backend)
  if (typeof window !== 'undefined' && window.location.hostname === 'localhost' && window.location.port === '5173') {
    return '';
  }

  // Fallback for native/packaged apps or direct cloud deployment
  return AWS_API_GATEWAY_URL;
}

export const API_BASE_URL: string = resolveApiBaseUrl();
