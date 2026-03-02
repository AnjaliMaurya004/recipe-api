#  Recipe API -- FastAPI Project

A fully functional RESTful Recipe API built using FastAPI, featuring JWT
authentication, CRUD operations, and SQLite database integration.

This project demonstrates backend development skills including
authentication, database management, API design, and clean project
structuring.

------------------------------------------------------------------------

##  Features

-   User Registration & Login\
-   JWT Authentication\
-   Password Hashing (bcrypt)\
-   Create, Read, Update, Delete Recipes\
-   Search Recipes by Name\
-   SQLite Database Integration\
-   Pydantic Data Validation\
-   Interactive API Docs (Swagger & ReDoc)\
-   Static Image Support

------------------------------------------------------------------------

##  Tech Stack

-   FastAPI\
-   SQLAlchemy\
-   SQLite\
-   Pydantic\
-   JWT (python-jose)\
-   Passlib (bcrypt)\
-   Uvicorn

------------------------------------------------------------------------


##  Installation & Setup

### 1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/recipe-api.git\
cd recipe-api

### 2. Create Virtual Environment

python -m venv .venv

### 3. Activate Virtual Environment (Windows PowerShell)

..venv`\Scripts`{=tex}`\Activate`{=tex}.ps1

### 4. Install Dependencies

pip install -r requirements.txt

### 5. Create .env File

SECRET_KEY=your_secret_key_here\
ALGORITHM=HS256\
ACCESS_TOKEN_EXPIRE_MINUTES=30

### 6. Run the Server

uvicorn app.main:app --reload

Server runs at:

http://127.0.0.1:8000

------------------------------------------------------------------------

##  API Documentation

Swagger UI → http://127.0.0.1:8000/docs\
ReDoc → http://127.0.0.1:8000/redoc

------------------------------------------------------------------------

##  Authentication Flow

1.  Register a user\
2.  Login to get JWT token\
3.  Click "Authorize" in Swagger UI\
4.  Access protected recipe endpoints

------------------------------------------------------------------------

##  Learning Outcomes

-   REST API Design\
-   Authentication & Authorization\
-   Secure Password Storage\
-   Database ORM Usage\
-   Environment Configuration\
-   Clean Code Architecture

------------------------------------------------------------------------

## Author

Anjali Maurya\
Computer Science Student \| Backend Developer

------------------------------------------------------------------------
 If you found this project useful, consider giving it a star!
