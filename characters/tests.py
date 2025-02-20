from rest_framework.test import APITestCase
from rest_framework import status
from .models import Character

class CharacterAPITest(APITestCase):
    def setUp(self):
        self.character = Character.objects.create(
            name="Harry Potter",
            house="Gryffindor",
            role="Student",
            wand="Holly, 11\", Phoenix Feather",
            patronus="Stag"
        )

    def test_get_characters(self):
        response = self.client.get('/api/characters/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_character(self):
        data = {
            "name": "Hermione Granger",
            "house": "Gryffindor",
            "role": "Student",
            "wand": "Vine wood, Dragon heartstring",
            "patronus": "Otter"
        }
        response = self.client.post('/api/characters/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_character_by_id(self):
        response = self.client.get(f'/api/characters/{self.character.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_character(self):
        data = {"name": "Harry Potter", "role": "Auror"}
        response = self.client.patch(f'/api/characters/{self.character.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.character.refresh_from_db()
        self.assertEqual(self.character.role, "Auror")

    def test_delete_character(self):
        response = self.client.delete(f'/api/characters/{self.character.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
