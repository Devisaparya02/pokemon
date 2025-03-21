# Pokémon Pokedex API

This is a Django GraphQL API for managing Pokémon, allowing various operations such as querying Pokémon details, adding new Pokémon, and deleting them.

## Features
- Query Pokémon by name
- List Pokémon with details like height, weight, and types
- Add new Pokémon
- Delete Pokémon by ID

## Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/pokemon-pokedex.git
cd pokemon-pokedex
```

2. Create a Virtual Environment
   ```
    python -m venv venv
   ```
3. Activate the Virtual Environment
   On Windows:
   ```
   venv\Scripts\activate
   ```
   On Mac/Linux:
   ```
   source venv/bin/activate
   ```
4. Install Dependencies
   
   ```
   pip install -r requirements.txt
   ```
5. Apply Database Migrations
   ````
   python manage.py makemigrations
   python manage.py migrate
   ```
 6. Populate the Database
    ```
    python manage.py populate_pokemon    
    ```
7. Start the Django Development Server
   ```
   python manage.py runserver
   ```
8.Access the GraphQL Playground
Visit GraphQL Playground to interact with the API.

Usage
Query Pokémon by Name

```
query {
  pokemon(name: "pikachu") {
    name
    height
    weight
    types {
      name
    }
  }
}
````
Add a Pokémon

```
mutation {
  addPokemon(pokemon: {
    name: "charizard",
    height: 17,
    weight: 905,
    type_ids: [1, 2]  # Replace with actual type IDs
  }) {
    name
    height
    weight
  }
}
```
Delete a Pokémon
```
mutation {
  deletePokemon(id: 25)  # Deletes Pikachu
}
```
Running Tests
```
pytest
```

    

