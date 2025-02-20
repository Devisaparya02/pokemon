Harry Potter Character API

This is a Django REST API for managing Harry Potter characters, allowing CRUD operations (Create, Read, Update, Delete).



Features
 List all characters
 Filter by house & role
 Search for characters by name
 Create new characters
 Update and delete characters

 Installation Guide
 A) Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/harry-potter-api.git
cd harry-potter-api
 B) Create a Virtual Environment
bash
python -m venv venv
Activate the Virtual Environment
Windows:
bash

venv\Scripts\activate
Mac/Linux:
bash

source venv/bin/activate
 D) Install Dependencies
bash

pip install -r requirements.txt
 Run the Project
 A) Apply Database Migrations
bash

python manage.py makemigrations
python manage.py migrate
 B) Create a Superuser (Optional)
bash

python manage.py createsuperuser


 C) Start the Django Server
bash

python manage.py runserver
 The server will start at:
http://127.0.0.1:8000/

 API Endpoints
Method	Endpoint	Description
GET	/api/characters/	Get all characters
GET	/api/characters/?house=Gryffindor	Filter characters by house
GET	/api/characters/?search=Harry	Search for characters
POST	/api/characters/	Add a new character
GET	/api/characters/1/	Get details of a character by ID
PUT	/api/characters/1/	Update a character by ID
DELETE	/api/characters/1/	Delete a character by ID
 Test the API Using cURL
 A) List All Characters
bash

curl -X GET http://127.0.0.1:8000/api/characters/
 B) Create a New Character
bash

curl -X POST http://127.0.0.1:8000/api/characters/ \
     -H "Content-Type: application/json" \
     -d '{
        "name": "Hermione Granger",
        "house": "Gryffindor",
        "role": "Student",
        "wand": "Vine wood, Dragon heartstring",
        "patronus": "Otter"
     }'
 C) Update a Character
bash

curl -X PUT http://127.0.0.1:8000/api/characters/1/ \
     -H "Content-Type: application/json" \
     -d '{
        "name": "Hermione Granger",
        "house": "Gryffindor",
        "role": "Professor",
        "wand": "Vine wood, Dragon heartstring",
        "patronus": "Otter"
     }'
 D) Delete a Character
bash

curl -X DELETE http://127.0.0.1:8000/api/characters/1/
 Test the API Using Postman
Open Postman
Set Method (GET, POST, PUT, DELETE)
Enter URL (http://127.0.0.1:8000/api/characters/)
Go to "Body" → Select "raw" → Choose "JSON"
Enter request data (for POST & PUT)
Click "Send"
 Running Unit Tests
To test API functionality, run:

bash

python manage.py test
