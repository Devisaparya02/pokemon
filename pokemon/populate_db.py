import requests
from pokemon.models import Pokemon, Type
Pokemon.objects.all().values("pokemon_id", "name")


def fetch_and_store_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=10"
    response = requests.get(url).json()

    for item in response["results"]:
        pokemon_data = requests.get(item["url"]).json()
        name = pokemon_data["name"]
        pokemon_id = pokemon_data["id"]
        height = pokemon_data["height"]
        weight = pokemon_data["weight"]

        pokemon, _ = Pokemon.objects.get_or_create(name=name, pokemon_id=pokemon_id, height=height, weight=weight)

        for type_info in pokemon_data["types"]:
            type_name = type_info["type"]["name"]
            type_obj, _ = Type.objects.get_or_create(name=type_name)
            pokemon.types.add(type_obj)

fetch_and_store_pokemon()
