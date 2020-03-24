from django.shortcuts import render
from novellas.models import Novella
from characters.models import Character

# Create your views here.

def custom_render(request, params={}, template='base.html'):
    if not params.get('title'):
        params['title'] = 'Nouvelles Exnihil'
    return render(request, template, params)

def index(request):
    novellas = [novella.to_dict() for novella in Novella.objects.order_by('-created_at')[:5]]
    characters = [character.to_dict() for character in Character.objects.all()[:5]]
    return custom_render(request, {
        'last_novellas': novellas,
        'main_characters': characters,
        'template': 'home/index.html'
    })
