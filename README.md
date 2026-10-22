# StreamFlix (Netflix Clone)

This is a full-stack Netflix clone I built to practice connecting a React frontend with a Django REST API. 

## Features
- JWT Authentication (Login)
- Browse movies with posters
- Live search (filters by title)
- "My List" feature (saves movies to the user's profile)
- Dark Netflix-style UI

## Tech Stack
**Backend:** Django, Django REST Framework, SimpleJWT, SQLite
**Frontend:** React, Axios, Bootstrap
**Tools:** Git, VS Code

## How to run this locally

You will need two terminals open (one for backend, one for frontend).

### 1. Backend Setup
Open your terminal in the root folder (`streamflix`):

```bash
# Create and activate virtual environment
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers

# Setup database
python manage.py migrate

# Add the sample movies
python manage.py seed

# Start the server (runs on port 8000)
python manage.py runserver
