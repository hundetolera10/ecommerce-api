
# 🛍️ E-Commerce Backend API

**ALX Backend Software Engineering – Capstone Project**

## 📌 Project Overview

This project is a fully functional **E-Commerce Backend API** built using **Django** and **Django REST Framework (DRF)**.
It supports product browsing, category management, shopping cart functionality, and user authentication.
The project follows **RESTful API principles** and uses **Django ORM** for all database operations.

## 🧑‍🎓 Student Information

* **Name:** Hunde Tolera
* **Program:** ALX Backend Software Engineering
* **Project Type:** Capstone
* **Backend Framework:** Django + Django REST Framework

## 🛠️ Technologies Used

* Python
* Django
* Django REST Framework
* SQLite (development)
* Git & GitHub
* Postman (API testing)

## 📁 Project Folder Structure

ecommerce-backend/
│
├── manage.py
├── README.md
├── db.sqlite3
│
├── ecommerce_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── products/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── cart/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── orders/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
└── venv/

# 📆 Development Progress by Week

## ✅ WEEK 1 – Project Setup & Architecture

### Objectives Achieved

* Created Django project and virtual environment
* Installed Django REST Framework
* Created core apps:

  * accounts
  * products
  * cart
  * orders
* Configured REST Framework settings
* Set up main API routing
* Initialized database and migrations
* Created superuser
* Tested project startup successfully

### Key Files (Week 1)

* settings.py – Installed apps & DRF configuration
* urls.py– Global API routing
* App skeletons with proper structure



## ✅ WEEK 2 – Products & Categories Module

### Features Implemented

* Category model
* Product model
* Product–Category relationship
* CRUD APIs for categories
* CRUD APIs for products
* Admin-only product/category creation
* Public product & category listing
* Django Admin integration

### Models

* **Category**

  * name
  * description

* **Product**

  * name
  * description
  * price
  * stock
  * category
  * created_at

### API Endpoints


GET     /api/products/
GET     /api/products/<id>/
POST    /api/products/        (admin only)
PUT     /api/products/<id>/   (admin only)
DELETE  /api/products/<id>/   (admin only)

GET     /api/products/categories/
POST    /api/products/categories/   (admin only)

## ✅ WEEK 3 – Cart & CartItem System

### Features Implemented

* Cart model (one cart per user)
* CartItem model
* Automatically create cart per user
* Add product to cart
* Remove product from cart
* Update item quantity
* View cart contents
* Secure cart endpoints (authenticated users only)

### Models

* **Cart**

  * user (OneToOne)

* **CartItem**

  * cart
  * product
  * quantity

### API Endpoints

GET     /api/cart/
POST    /api/cart/add/
POST    /api/cart/remove/
POST    /api/cart/update/

## 🔐 Authentication

* Token-based authentication using Django REST Framework
* Admin users can manage products and categories
* Regular users can manage their own carts

## ▶️ How to Run the Project Locally

# Clone the repository
git clone <your-repo-url>
cd ecommerce-backend

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows

# Install dependencies
pip install django djangorestframework

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

## 🧪 Testing

* Django REST Framework Browsable API
* Browser testing
* Postman (recommended)




