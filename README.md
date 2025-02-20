1. Clone the Repository
bash

git clone https://github.com/your-username/pokemon-pokedex.git
cd pokemon-pokedex
2. Create a Virtual Environment
bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash

pip install -r requirements.txt
4. Run Migrations
bash

python manage.py makemigrations
python manage.py migrate
5. Populate the Database
bash

python manage.py populate_pokemon
6. Run the Development Server
bash

python manage.py runserver
Now, visit:
GraphQL Playground: http://127.0.0.1:8000/graphql

Usage
Query Pokémon by Name
graphql

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
Add a Pokémon
graphql

mutation {
  addPokemon(pokemon: { name: "charizard", height: 17, weight: 905, base_experience: 240, types: ["fire", "flying"] }) {
    name
    height
    weight
  }
}
Delete a Pokémon
graphql


mutation {
  deletePokemon(id: 25)  # Deletes Pikachu
}
Running Tests
To run unit tests for the API:

bash

pytest


bash

pytest --cov=pokedex
