from pokedex.pokemon.schema import TypeType
from .types import PokemonType, PokemonInputType
import strawberry
from typing import List

@strawberry.type
class PokemonType:
    pokemon_id: int
    name: str
    height: float
    weight: float
    types: List["TypeType"]  # Ensure it's a list


@strawberry.input
class PokemonInputType:
    pokemon_id: int  # Use snake_case
    name: str
    height: float
    weight: float
    type_ids: int = None  # Use snake_case



