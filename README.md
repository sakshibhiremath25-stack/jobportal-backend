# Job Portal Backend

## 🚀 Project Description
This is a Job Portal Backend built using Django Rest Framework.

It provides APIs for:
- User Authentication
- Job Creation
- Job Application
- Application Status Management

---

## 🛠 Technologies Used
- Python
- Django
- Django REST Framework
- SQLite
- Simple JWT Authentication

---

## ⚙ Installation Steps

### 1. Clone Repository
git clone <your-repo-link>
cd JobPortelApplication-Backend

### 2. Create Virtual Environment
python -m venv env
env\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run Migrations
python manage.py makemigrations
python manage.py migrate

### 5. Run Server
python manage.py runserver
Server runs at:


---

## 🔐 Authentication
Login API:
POST /api/token/

Use token in headers:
Authorization: Bearer <access_token>

---

## 👨‍💻 Developed By
Your Name:
Sakshi Hiremath