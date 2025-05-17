import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  // Root directory of the Vite project
  root: '.',

  // Base path for assets (use '/static/' for Django, '/' for standalone)
  base: '/static/',

  // Build configuration
  build: {
    // Output directory (relative to root), aligns with Django's staticfiles
    outDir: '../backend/staticfiles/frontend',
    // Subdirectory for assets like images and fonts
    assetsDir: 'assets',
    // Generate manifest.json for Django to map hashed assets
    manifest: true,
    // Clear output directory before building
    emptyOutDir: true,
    // Optimize for production (minification, etc.)
    minify: 'esbuild',
  },

  // Development server configuration
  server: {
    // Port for Vite dev server (Render uses 10000 in production, but this is for dev)
    port: 5173,
    // Proxy API and admin requests to Django backend during development
    proxy: {
      '/api': {
        target: 'https://django-react-website.onrender.com/',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '/api'),
      },
      '/admin': {
        target: 'https://django-react-website.onrender.com/',
        changeOrigin: true,
      },
    },
  },

  // Plugins for React and other features
  plugins: [
    react(),
    // Add other plugins as needed (e.g., vite-plugin-svgr for SVG imports)
  ],

  // Resolve aliases for cleaner imports
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './frontend/src'),
    },
  },

  // Define environment variables or constants
  define: {
    'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV || 'development'),
  },

  // CSS preprocessor settings (e.g., for SCSS or Tailwind)
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@import "@/styles/variables.scss";`,
      },
    },
  },
});