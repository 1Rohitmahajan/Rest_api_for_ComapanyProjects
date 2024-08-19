# Client Projects Manager

This project is a Django application for managing clients and projects. It utilizes Django REST Framework for building APIs and PostgreSQL as the database backend.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Contributing](#contributing)

## Prerequisites
Before you start, ensure you have the following installed:

- Python 3.x
- 
- PostgreSQL
- 
- pip (Python package installer)


1. **Clone the Repository**

 Open your terminal and run the following command to clone the repository to your local machine:

 git clone https://github.com/1Rohitmahajan/Rest_api_for_ComapanyProjects.git

 git clone  https://github.com/1Rohitmahajan/Rest_api_for_ComapanyProjects.git

***Setup***
1. Create a Virtual Environment

python -m venv venv

2. Activate the Virtual Environment

On Windows:
.\venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

4. Install Dependencies

pip install -r requirements.txt

Run Migrations

python manage.py makemigrations

python manage.py migrate



14. Create Superuser
python manage.py createsuperuser



15. Run the Development Server

python manage.py runserver


************************************
Screenshots
Admin Interface: ![image](https://github.com/user-attachments/assets/162bd756-c3ed-48df-8ebf-4f72c70a6046)
![image](https://github.com/user-attachments/assets/b9fbb866-34f6-4030-a6c7-8feacaf5e195)


Client List: ![all clients list](https://github.com/user-attachments/assets/47613e72-3f7e-48c0-a5a6-e7be67b6b06b)

Project List: ![get all project list](https://github.com/user-attachments/assets/2271a1a9-6ea2-47cc-afd5-5a8a07323077)

![create new project with id](https://github.com/user-attachments/assets/33eed02b-d270-4c52-8ea6-2ec7b4a9c2bb)

![put method](https://github.com/user-attachments/assets/38dfa5e6-30c8-43b0-832b-fd9e6c8ed565)

![get method](https://github.com/user-attachments/assets/43f5ae4b-0131-4e38-b49b-50d045890ed1)
![create new project with id](https://github.com/user-attachments/assets/ccbaaa23-7d1a-4fd9-aae9-720021c44075)
![delete client](https://github.com/user-attachments/assets/ce70009a-94b6-46a3-b99f-2aab3cd1e698)










Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements.

API Endpoints

List all clients

GET /api/clients/

Create a new client

POST /api/clients/

Retrieve, update, or delete a client

GET /api/clients/<id>/

PUT /api/clients/<id>/

PATCH /api/clients/<id>/

DELETE /api/clients/<id>/

Create a new project for a client

POST /api/clients/<client_id>/projects/

List all projects assigned to the logged-in user


GET /api/projects/





6. Configure the Database
Update client_projects_manager/settings.py with PostgreSQL configuration:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'newDBRohit_Manager',
        'USER': 'postgres',
        'PASSWORD': 'Rohit@#****',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}





7. Add Installed Apps

   
Add the following to client_projects_manager/settings.py:
INSTALLED_APPS = [

    'rest_framework',
    'coreApp',
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
]
