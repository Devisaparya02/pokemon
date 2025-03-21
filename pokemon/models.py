from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    name = models.CharField(max_length=100, unique=True)
    pokemon_id = models.IntegerField(unique=True)
    height = models.FloatField()
    weight = models.FloatField()
    types = models.ManyToManyField(Type, related_name="pokemons")

    def __str__(self):
        return self.name