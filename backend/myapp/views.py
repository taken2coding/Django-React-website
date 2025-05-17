import json
import os
from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'frontend/index.html'  # Relative to STATIC_ROOT


def index(request):
    # Load Vite's manifest.json for production
    manifest = {}
    manifest_path = os.path.join(settings.STATIC_ROOT, 'frontend', 'manifest.json')
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
    return render(request, 'index.html', {'manifest': manifest})

