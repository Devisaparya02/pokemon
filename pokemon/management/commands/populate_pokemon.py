import requests
from django.core.management.base import BaseCommand
from pokemon.models import Pokemon, Type

class Command(BaseCommand):
    help = 'Populate the database with Pokémon data from PokeAPI'

    def handle(self, *args, **kwargs):
        url = "https://pokeapi.co/api/v2/pokemon?limit=10"  # Fetch the first 10 Pokémon
        response = requests.get(url).json()

        for item in response["results"]:
            pokemon_data = requests.get(item["url"]).json()
            name = pokemon_data["name"]
            pokemon_id = pokemon_data["id"]
            height = pokemon_data["height"]
            weight = pokemon_data["weight"]

            # Create or update the Pokémon
            pokemon, created = Pokemon.objects.get_or_create(
                pokemon_id=pokemon_id,
                defaults={
                    "name": name,
                    "height": height,
                    "weight": weight,
                }
            )

            # Add types to the Pokémon
            for type_info in pokemon_data["types"]:
                type_name = type_info["type"]["name"]
                type_obj, _ = Type.objects.get_or_create(name=type_name)
                pokemon.types.add(type_obj)

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added Pokémon: {name} (ID: {pokemon_id})'))
            else:
                self.stdout.write(self.style.WARNING(f'Pokémon already exists: {name} (ID: {pokemon_id})'))