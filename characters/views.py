from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Character
from .serializers import CharacterSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    # Enable filtering & search
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['house', 'role']  # Allow filtering by house & role
    search_fields = ['name']  # Allow searching by character name
