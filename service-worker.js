const CACHE_NAME = 'gembukai-v8-version-1.1.3';
const urlsToCache = [
  './',
  './index.html',
  './logo.png',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-512-maskable.png',
  './translations.json',
  './users.json',
  './data/exercises.json'
];

// Instalar el service worker y cachear los archivos
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('✅ Cache abierta');
        return cache.addAll(urlsToCache);
      })
      .catch(err => console.log('Error cacheando:', err))
  );
});

// Interceptar peticiones y servirlas desde la cache si es posible
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response;
        }
        return fetch(event.request);
      })
  );
});

// Actualizar la cache cuando cambie la versión
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.filter(cacheName => cacheName !== CACHE_NAME)
          .map(cacheName => caches.delete(cacheName))
      );
    })
  );
});
