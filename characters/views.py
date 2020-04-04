from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch
from .models import Character
from novellas.models import Novella
from app.views import custom_render

# Create your views here.

def index(request):
    characters = [character.to_dict() for character in Character.objects.all()]
    return custom_render(request, { 'characters': characters, 'template': 'characters/index.html' })

def detail(request, pk):
    character = get_object_or_404(Character.objects.prefetch_related(
        Prefetch(
            'novellas',
            queryset=Novella.objects.prefetch_related(Prefetch('tags', to_attr='tags_list')).filter(characters__id=pk),
            to_attr='novellas_list'
        )
    ), pk=pk)
    character_as_dict = character.to_dict()
    character_as_dict['novellas'] = [novella.to_dict(short=True) for novella in character.novellas_list]
    return custom_render(request, {'character': character_as_dict, 'template': 'characters/details.html', 'title': character.name })
