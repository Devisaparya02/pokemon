from django.test import TestCase

# Create your tests here.
from .models import Pokemon

class PokemonModelTest(TestCase):
    def test_create_pokemon(self):
        pokemon = Pokemon.objects.create(name="Pikachu", type="Electric", description="A mouse Pokémon.")
        self.assertEqual(pokemon.name, "Pikachu")