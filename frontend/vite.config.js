import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'https://django-react-website.onrender.com/',
        changeOrigin: true,
      },
    },
  },
  build: {
    outDir: '../backend/staticfiles',
    emptyOutDir: true,
  },
})