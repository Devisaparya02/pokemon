import strawberry
from typing import Optional, List
from strawberry.types import Info
from .models import Pokemon, Type
from django.db.models import Q

@strawberry.type
class TypeType:
    id: strawberry.ID
    name: str

@strawberry.type  # Use strawberry.type directly
class PokemonType:
    id: int
    name: str
    height: float
    weight: float
    types: List[TypeType] = strawberry.field(default_factory=list)  # Ensure types is always a list

@strawberry.input
class PokemonInputType:
    name: str
    pokemon_id: int
    height: float
    weight: float
    type_ids: List[int]

@strawberry.input
class PokemonUpdateInput:
    name: Optional[str] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    type_ids: Optional[List[int]] = None

@strawberry.type
class Query:
    @strawberry.field
    def pokemon(self, info: Info, name: Optional[str] = None, id: Optional[int] = None) -> Optional[PokemonType]:
        if id:
            pokemon = Pokemon.objects.filter(pk=id).first()
        elif name:
            pokemon = Pokemon.objects.filter(name__iexact=name).first()
        else:
            return None

        if pokemon:
            return PokemonType(
                id=pokemon.id,
                name=pokemon.name,
                height=pokemon.height,
                weight=pokemon.weight,
                types=[TypeType(id=type.id, name=type.name) for type in pokemon.types.all()]
            )
        return None

    @strawberry.field
    def pokemons(self, info: Info, search: Optional[str] = None, type: Optional[str] = None) -> List[PokemonType]:
        queryset = Pokemon.objects.all()
        if search:
            queryset = queryset.filter(name__icontains=search)
        if type:
            queryset = queryset.filter(types__name__iexact=type)

        return [
            PokemonType(
                id=pokemon.id,
                name=pokemon.name,
                height=pokemon.height,
                weight=pokemon.weight,
                types=[TypeType(id=type.id, name=type.name) for type in pokemon.types.all()]
            ) for pokemon in queryset
        ]

    @strawberry.field
    def types(self, info: Info, search: Optional[str] = None) -> List[TypeType]:
        queryset = Type.objects.all()
        if search:
            queryset = queryset.filter(name__icontains=search)
        return [TypeType(id=type.id, name=type.name) for type in queryset]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_pokemon(self, pokemon: PokemonInputType) -> PokemonType:
        if Pokemon.objects.filter(pokemon_id=pokemon.pokemon_id).exists():
            raise Exception(f"Pokémon with ID {pokemon.pokemon_id} already exists.")

        new_pokemon = Pokemon.objects.create(
            pokemon_id=pokemon.pokemon_id,
            name=pokemon.name,
            height=pokemon.height,
            weight=pokemon.weight
        )

        if pokemon.type_ids:
            types = Type.objects.filter(id__in=pokemon.type_ids)
            new_pokemon.types.set(types)

        new_pokemon.save()

        return PokemonType(
            id=new_pokemon.id,
            name=new_pokemon.name,
            height=new_pokemon.height,
            weight=new_pokemon.weight,
            types=[TypeType(id=type.id, name=type.name) for type in new_pokemon.types.all()]
        )

    @strawberry.mutation
    def update_pokemon(self, pokemon_id: int, update: PokemonUpdateInput) -> PokemonType:
        pokemon = Pokemon.objects.filter(pokemon_id=pokemon_id).first()
        if not pokemon:
            raise Exception("Pokémon not found.")

        if update.name:
            pokemon.name = update.name
        if update.height:
            pokemon.height = update.height
        if update.weight:
            pokemon.weight = update.weight
        if update.type_ids:
            types = Type.objects.filter(id__in=update.type_ids)
            pokemon.types.set(types)

        pokemon.save()
        return PokemonType(
            id=pokemon.id,
            name=pokemon.name,
            height=pokemon.height,
            weight=pokemon.weight,
            types=[TypeType(id=type.id, name=type.name) for type in pokemon.types.all()]
        )

    @strawberry.mutation
    def delete_pokemon(self, id: int) -> bool:
        deleted, _ = Pokemon.objects.filter(pk=id).delete()
        return bool(deleted)

schema = strawberry.Schema(query=Query, mutation=Mutation)