# 🎬 StreamFlix — Full Stack Netflix Clone

A full-stack streaming platform built with Django REST Framework and React. Features JWT authentication, movie browsing, search, and a personal "My List" feature.

## 🚀 Tech Stack
- **Backend:** Python, Django, Django REST Framework, JWT (SimpleJWT)
- **Database:** SQLite (PostgreSQL-ready)
- **Frontend:** React, Bootstrap, Axios
- **Tools:** Git, VS Code

## ✨ Features
- 🔐 **JWT Authentication** (Login/Register)
- 🎥 **Movie Catalog** (Browse 8 seeded movies with posters)
- 🔍 **Live Search** (Filter movies by title)
- ❤️ **My List** (Save favorites — tied to user account)
- 🎨 **Netflix-style UI** (Dark theme, responsive grid)

## 🛠️ How to Run Locally

### 1. Backend (Django)
```bash
cd streamflix
python -m venv venv
# Activate venv:
# Windows: .\venv\Scripts\Activate
# Mac/Linux: source venv/bin/activate

pip install -r requirements.txt  # (or install manually)
python manage.py migrate
python manage.py seed
python manage.py runserver
