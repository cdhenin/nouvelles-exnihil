from django.shortcuts import render, get_object_or_404
from .models import Novella
from app.views import custom_render

# Create your views here.

def index(request, *kwargs):
    tag_ids = request.GET.get('tag')
    if (tag_ids):    
        novellas = [novella.to_dict() for novella in Novella.objects.filter(tags__id__in=tag_ids).order_by('-created_at')]
    else:
        novellas = [novella.to_dict() for novella in Novella.objects.order_by('-created_at')]

    return custom_render(request, {
        'novellas': novellas, 
        'template': 'novellas/index.html', 
    })

def detail(request, pk):
    novella = get_object_or_404(Novella, pk=pk)
    return custom_render(request, {
        'novella': novella.to_dict(), 
        'title': novella.title, 
        'template': 'novellas/details.html'
    })
