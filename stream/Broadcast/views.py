from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Broadcast

def diffusion_en_direct(request):
    return render(request, 'diffusion_en_direct.html')
"""
def diffusion(request):
    diffusions = Broadcast.objects.all()
    context = {
        'diffusions': diffusions
    }
    return render(request, 'liste_diffusions.html', context)"""

def detail_diffusion(request, diffusion_id):
    diffusion = get_object_or_404(Broadcast, pk=diffusion_id)
    context = {
        'diffusion': diffusion
    }
    return render(request, 'detail_diffusion.html', context)