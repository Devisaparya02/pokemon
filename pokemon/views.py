from django.shortcuts import render

# Create your views here.
from .models import Pokemon

def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokedex/pokemon_list.html', {'pokemons': pokemons})