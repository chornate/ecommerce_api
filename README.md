# E-commerce API

This repository contains the source code for an E-commerce API designed to manage product listings, user authentication, and order handling for a video games platform. The API is built using Django and Django REST Framework (DRF).

## Features

- **User Authentication**: Secure user registration and login using JWTs.
- **Product Management**: CRUD operations for products.
- **Search Functionality**: Advanced product search with filters.
- **Order Management**: Placing and managing customer orders.
- **Secure API**: Role-based permissions and token-based authentication.

## Technologies Used

- **Backend Framework**: Django, Django REST Framework
- **Authentication**: Simple JWT for token-based authentication
- **Database**: PostgreSQL (can be switched to SQLite for development)
- **Testing**: Built-in Django testing tools

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/chornate/ecommerce_api.git
   cd ecommerce_api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser for accessing the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Endpoints

### Authentication
- **POST** `/api/auth/register/`: Register a new user.
- **POST** `/api/auth/login/`: Log in to get access and refresh tokens.

### Products
- **GET** `/api/products/`: List all products.
- **POST** `/api/products/`: Create a new product (admin only).
- **GET** `/api/products/<id>/`: Retrieve a specific product.
- **PUT** `/api/products/<id>/`: Update a product (admin only).
- **DELETE** `/api/products/<id>/`: Delete a product (admin only).

### Orders
- **GET** `/api/orders/`: List all orders (admin only).
- **POST** `/api/orders/`: Place a new order.
- **GET** `/api/orders/<id>/`: Retrieve details of a specific order.
