FastAPI + PostgreSQL Project Template

This project is a minimal FastAPI setup prepared for interviews and real-world projects. It comes with a working PostgreSQL connection, SQLAlchemy ORM models, and Pydantic schemas for request/response validation.

📂 Project Structure
fastapi_project/
│── main.py
│── database.py
│── models.py
│── schemas.py
│── requirements.txt
│── .env

📌 File Overview
main.py

Entry point of the application.

Creates the FastAPI app and sets up routes.

Runs models.Base.metadata.create_all(bind=engine) to ensure tables exist in the database.

Defines a test route (/) to verify the app is working.

database.py

Handles PostgreSQL connection via SQLAlchemy.

Loads environment variables from .env.

Creates a SessionLocal for database access.

Exposes a get_db() dependency so routes can safely use DB sessions.

This file is the bridge between your API and the database.

models.py

Defines SQLAlchemy ORM models that map Python classes to PostgreSQL tables.

Example:

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


Under the hood, SQLAlchemy translates these classes into SQL table definitions.

schemas.py

Defines Pydantic models for request validation and response serialization.

Example:

class UserBase(BaseModel):
    name: str
    email: EmailStr


UserCreate is used for incoming requests.

User is used for responses (includes id).

orm_mode = True allows Pydantic to read directly from SQLAlchemy objects.

This file enforces data contracts between your API and its clients.

.env

Stores environment variables such as database credentials:

DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/yourdb


This keeps sensitive information out of your codebase.

requirements.txt

Lists the dependencies needed to run the project:

fastapi
uvicorn[standard]
sqlalchemy
psycopg2-binary
pydantic[email]
python-dotenv


fastapi → API framework

uvicorn → ASGI server

sqlalchemy → ORM

psycopg2-binary → PostgreSQL driver

pydantic[email] → validation (e.g. email fields)

python-dotenv → load .env file

⚙️ Getting Started
1. Install dependencies
pip install -r requirements.txt

2. Set up PostgreSQL

You have three options:

Local Install → Install PostgreSQL on your machine.

Docker (recommended) → Run Postgres in a container:

docker run --name fastapi-postgres \
    -e POSTGRES_PASSWORD=yourpassword \
    -e POSTGRES_DB=yourdb \
    -p 5432:5432 -d postgres


Hosted Service → Use Supabase, Render, or Railway.

3. Configure .env
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/yourdb

4. Run the application
uvicorn main:app --reload

5. Explore API docs

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

🔑 How It All Fits Together

Client request → main.py

Request body validated → schemas.py (Pydantic)

FastAPI uses DB session → database.py

SQLAlchemy ORM models → models.py map to Postgres

Postgres executes queries and returns results

Response serialized → schemas.py before returning to client

✅ Next Step

This template is minimal, but you can extend it by adding CRUD endpoints (e.g., for User) to demonstrate full API functionality during your interview.