// Minimal service worker for DhakreyStock AI PWA installation
const CACHE_NAME = 'dhakreystock-cache-v1';

self.addEventListener('install', (event) => {
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', (event) => {
  // Let browser handle network requests
});
