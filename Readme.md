College Management System – Python (Flask)
A web-based College Management System built using Python, Flask, SQLAlchemy, and SQLite.
It allows administrators to manage students, with the ability to add, view, and store student information securely.
🚀 Features
Module
Description
Student Management
Add, view and list students with unique roll number
Database Storage
All student data stored securely using SQLAlchemy ORM
Form Handling
WTForms for server-side validation
UI Templates
Jinja2 HTML templates
MVC Project Structure
Clean and scalable project layout
🛠️ Tech Stack
Category
Technology
Backend
Python 3, Flask
Database
SQLite (default)
ORM
SQLAlchemy
UI
HTML, Bootstrap, Jinja Templates
Deployment
Gunicorn + Procfile support (Heroku/Render)

clone the repository 
git clone https://github.com/<your-username>/college-management-system-python.git
cd college-management-system-python

Create a Virtual Environment

python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
Install Dependencies

pip install -r requirements.txt

Run the Application

python run.py
