import strawberry
from typing import Optional, List
from strawberry.types import Info
from .models import Pokemon, Type
from django.db.models import Q


@strawberry.type
class TypeType:
    id: strawberry.ID
    name: str


@strawberry.type
class PokemonType:
    id: int
    name: str
    height: float
    weight: float
    types: List[TypeType] = strawberry.field(default_factory=list)


@strawberry.input
class PokemonInputType:
    name: str
    pokemonId: int  # Use camelCase
    height: float
    weight: float
    typeIds: List[int]  # Use camelCase


@strawberry.input
class PokemonUpdateInput:
    name: Optional[str] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    typeIds: Optional[List[int]] = None  # Use camelCase


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
        if Pokemon.objects.filter(pokemon_id=pokemon.pokemonId).exists():
            raise Exception(f"Pokémon with ID {pokemon.pokemonId} already exists.")

        new_pokemon = Pokemon.objects.create(
            pokemon_id=pokemon.pokemonId,
            name=pokemon.name,
            height=pokemon.height,
            weight=pokemon.weight
        )

        if pokemon.typeIds:
            types = Type.objects.filter(id__in=pokemon.typeIds)
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
    def update_pokemon(self, id: int, update: PokemonUpdateInput) -> PokemonType:
        pokemon = Pokemon.objects.filter(pk=id).first()
        if not pokemon:
            raise Exception("Pokémon not found.")

        if update.name:
            pokemon.name = update.name
        if update.height:
            pokemon.height = update.height
        if update.weight:
            pokemon.weight = update.weight
        if update.typeIds:
            types = Type.objects.filter(id__in=update.typeIds)
            pokemon.types.set(types)

        pokemon.save()
        return PokemonType(
            id=pokemon.id,
            name=pokemon.name,
            height=pokemon.height,
            weight=pokemon.weight,
            types=[TypeType(id=type.id, name=type.name) for type in pokemon.types.all()]
        )


schema = strawberry.Schema(query=Query, mutation=Mutation)