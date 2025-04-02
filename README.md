# pythonweb-hw-08

## Project Overview

This project is a **REST API for managing contacts**, built using the **FastAPI** framework. It provides functionality to store and manage contact information, including CRUD operations (Create, Read, Update, Delete). The API uses **SQLAlchemy** as the ORM for database interactions and **PostgreSQL** as the database.

The project also includes **Swagger documentation** for easy exploration of the API and uses **Pydantic** for data validation.

---

## Features

- **FastAPI Framework**: A modern, fast (high-performance) web framework for building APIs.
- **SQLAlchemy ORM**: Used for database modeling and interaction.
- **PostgreSQL Database**: A robust and reliable relational database.
- **CRUD Operations**: Full support for creating, reading, updating, and deleting contacts.
- **Date of Birth Support**: Ability to store and manage the date of birth for each contact.
- **Swagger Documentation**: Automatically generated API documentation available at `/docs`.
- **Pydantic Validation**: Ensures data integrity and validation for all API inputs.

---

## Requirements

- **Python**: 3.10 or higher
- **PostgreSQL**: Version 14 or higher
- **Dependencies**: Listed in `requirements.txt`

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Alexandrbig1/pythonweb-hw-08.git
   cd pythonweb-hw-08
   ```
2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Up the Database**:

- Ensure PostgreSQL is installed and running.
- Create a database named `contacts_db`:

```bash
CREATE DATABASE contacts_db;
```

- Update the `.env` file with your database credentials:

```bash
POSTGRES_DB=contacts_db
POSTGRES_USER=example_user
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

5. **Run Alembic Migrations**:
   ```bash
   alembic upgrade head
   ```
6. **Start the Application**:
   ```bash
   uvicorn main:app --reload
   ```

---

## API Endpoints

### Base URL

```bash
http://localhost:8000
```

### Endpoints

| Method | Endpoint         | Description              |
| ------ | ---------------- | ------------------------ |
| GET    | `/contacts`      | Retrieve all contacts    |
| GET    | `/contacts/{id}` | Retrieve a contact by ID |
| POST   | `/contacts`      | Create a new contact     |
| PUT    | `/contacts/{id}` | Update a contact by ID   |
| DELETE | `/contacts/{id}` | Delete a contact by ID   |

### Swagger Documentation

Access the Swagger UI for API documentation at:

```bash
http://localhost:8000/docs
```

---

## Project Structure

```markdown
pythonweb-hw-08/
├── migrations/ # Alembic migrations
├── src/
│ ├── conf/ # Configuration files
│ ├── database/ # Database session management
│ ├── entity/ # SQLAlchemy models
│ ├── repository/ # Database query logic
│ ├── routes/ # API routes
│ ├── schemas/ # Pydantic schemas
│ ├── services/ # Business logic and service layer
├── main.py # Application entry point
├── .env # Environment variables
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

---

## Technologies Used

- **FastAPI**: Web framework for building APIs.
- **SQLAlchemy**: ORM for database modeling and interaction.
- **PostgreSQL**: Relational database.
- **Pydantic**: Data validation and settings management.
- **Alembic**: Database migrations.
- **Uvicorn**: ASGI server for running the application.

---

## Future Improvements

- Add user authentication and authorization.
- Implement pagination for retrieving large contact lists.
- Add search and filtering capabilities for contacts.
- Deploy the application to a cloud platform (e.g., AWS, Heroku).
