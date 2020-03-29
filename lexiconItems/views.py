from django.shortcuts import render
from .models import LexiconItem
from app.views import custom_render

# Create your views here.
def index(request):
    items = [item.to_dict() for item in LexiconItem.objects.order_by('-name')]
    return custom_render(request, {
        'items': items,
        'title': 'Lexique',
        'template': 'lexicon/index.html'
    })