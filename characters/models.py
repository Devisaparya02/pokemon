from django.db import models

class Character(models.Model):
    HOUSES = [
        ('Gryffindor', 'Gryffindor'),
        ('Hufflepuff', 'Hufflepuff'),
        ('Ravenclaw', 'Ravenclaw'),
        ('Slytherin', 'Slytherin'),
        ('Unknown', 'Unknown'),
    ]

    ROLES = [
        ('Student', 'Student'),
        ('Professor', 'Professor'),
        ('Auror', 'Auror'),
        ('Death Eater', 'Death Eater'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100, unique=True)
    house = models.CharField(max_length=20, choices=HOUSES, default='Unknown')
    role = models.CharField(max_length=20, choices=ROLES, default='Other')
    wand = models.CharField(max_length=100, blank=True, null=True)
    patronus = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
