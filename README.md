
markdown
Copy
Edit
# Python Advanced Project

## 📌 Overview

This project is a **Flask-based web application** that simulates an online book management system.  
It supports user registration and login, and provides a simple API to manage books, including creation, retrieval, update, and deletion (CRUD operations).  
The app also implements authentication using JWT and utilizes advanced Python concepts like custom decorators and object-oriented design.

---

## ⚙️ Installation & Execution

### Prerequisites
- Python 3.10+
- `pip` package manager

### 1. Clone the repository
```bash
git clone https://github.com/MiriShulman/python-advanced-project.git
cd python-advanced-project
2. Create a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the app
bash
Copy
Edit
python main.py
The API will be available at http://127.0.0.1:5000/

📁 Project Structure
bash
Copy
Edit
python-advanced-project/
│
├── main.py                # Entry point – initializes and runs the Flask app
├── auth.py                # Handles user authentication and JWT logic
├── book.py                # Book model and business logic
├── user.py                # User model and user-related endpoints
├── decorator.py           # Custom route decorators (e.g., JWT validation)
├── utils.py               # Utility functions for token handling, error messages, etc.
├── requirements.txt       # List of required Python packages
└── README.md              # Project documentation
🌐 API Endpoints
🔐 Authentication
POST /register
Register a new user.
Body:

json
Copy
Edit
{
  "username": "your_name",
  "password": "your_password"
}
POST /login
Logs in a user and returns a JWT token.
Body:

json
Copy
Edit
{
  "username": "your_name",
  "password": "your_password"
}
📚 Book Management (Requires JWT Token in Authorization header)
GET /books
Retrieve all books.
Headers:

makefile
Copy
Edit
Authorization: Bearer <your_token>
GET /books/<book_id>
Retrieve a single book by ID.

POST /books
Create a new book.
Body:

json
Copy
Edit
{
  "title": "Book Title",
  "author": "Author Name",
  "year": 2023
}
PUT /books/<book_id>
Update an existing book.
Body:

json
Copy
Edit
{
  "title": "Updated Title",
  "author": "Updated Author",
  "year": 2024
}
DELETE /books/<book_id>
Delete a book by ID.

✅ Features
RESTful API structure

JWT Authentication

Modular code using classes and decorators

Input validation and error handling

