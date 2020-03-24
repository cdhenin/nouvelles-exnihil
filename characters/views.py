from django.shortcuts import render, get_object_or_404
from .models import Character
from app.views import custom_render

# Create your views here.

def index(request):
    characters = [character.to_dict() for character in Character.objects.all()]
    return custom_render(request, { 'characters': characters, 'template': 'characters/index.html' })

def detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return custom_render(request, {'character': character.to_dict(), 'template': 'characters/details.html', 'title': character.name })
