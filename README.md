
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

POST    /api/products/products/     (admin only)

PUT     /api/products/products/<id>/   (admin only)

DELETE  /api/products/products/<id>/   (admin only)

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
---

# 🟦 WEEK 4 — Orders & Payment Simulation

## 📌 Overview

Week 4 focuses on implementing the **Order Management and Payment Simulation** features of the E-commerce Backend API.
This week completes the **core shopping workflow**, allowing users to convert cart items into orders, track order history, and simulate payments.

By the end of this week, the backend supports the full flow:

**Browse Products → Add to Cart → Create Order → Pay for Order**

## ✅ Objectives Achieved

* Implemented **Order** and **OrderItem** models
* Created API endpoints to:

  * Create orders from cart items
  * View user order history
  * View order details
  * Simulate payment processing
* Linked orders to authenticated users
* Automatically cleared cart after order creation
* Implemented order status transitions:

  * PENDING → PAID → DELIVERED
* Registered orders in Django Admin for management

## 🗂️ Folder Structure (Week 4)

orders/
├── admin.py
├── apps.py
├── models.py
├── serializers.py
├── urls.py
├── views.py
└── migrations/

## 🧱 Models Implemented

### Order

* User (ForeignKey)
* Total price
* Status (PENDING, PAID, DELIVERED)
* Created date

### OrderItem

* Order (ForeignKey)
* Product (ForeignKey)
* Quantity

Each order can contain **multiple order items**, and each order belongs to a **single user**.

## 🔐 Authentication

All order-related endpoints require **JWT or token-based authentication**.

Unauthenticated users **cannot**:

* Create orders
* View order history
* Make payments

## 🌐 API Endpoints (Week 4)

### 🛒 Create Order from Cart

POST /api/orders/create/

* Converts cart items into an order
* Clears the cart after successful creation
* Default status: PENDING

### 📦 View Order History

GET /api/orders/

* Returns all orders for the logged-in user

### 🔍 View Order Details

GET /api/orders/<id>/

* Returns detailed information about a specific order
* Includes order items and product details

### 💳 Payment Simulation

POST /api/orders/<id>/pay/


* Simulates payment processing
* Updates order status from PENDING to PAID
* No real payment gateway integration (as per project requirements)

## 🧪 Testing

### Recommended Testing Tools

* Browser (GET requests)
* Postman / Thunder Client
* Django Admin Panel

### Test Flow

1. Add products to cart
2. Create order from cart
3. Verify order appears in order history
4. Pay for order
5. Confirm order status updates to PAID

## 🛠️ Database Migration

Migrations were created and applied for the new models:

python manage.py makemigrations
python manage.py migrate

## 👨‍💻 Admin Panel

Orders and OrderItems are fully manageable via:

/admin/

Admin users can:

* View all orders
* Track order status
* Inspect order items

## 🚀 Outcome

Week 4 completes the **transactional backbone** of the e-commerce system.
The backend now supports:

✔ Cart to Order conversion
✔ Order tracking
✔ Payment simulation
✔ Secure, user-specific order access






