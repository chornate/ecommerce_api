# Video Game E-commerce API

This is a video game e-commerce API built with Django and Django REST framework. It includes features for user authentication, product management, order processing, product reviews, and wishlists.

## Features

- **User Authentication**: Register and login users.
- **Product Management**: Create, update, delete, and list video games.
- **Order Processing**: Create and manage orders.
- **Product Reviews**: Allow users to submit reviews and ratings for video games.
- **Wishlist**: Allow users to add video games to a wishlist.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/videogame_ecommerce_api.git
    cd videogame_ecommerce_api
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

## API Endpoints

### Authentication

- `POST /auth/register/`: Register a new user.
- `POST /auth/login/`: Login a user and obtain a token.

### Video Games

- `GET /products/`: List all video games.
- `POST /products/`: Create a new video game.
- `GET /products/{id}/`: Retrieve a video game by ID.
- `PUT /products/{id}/`: Update a video game by ID.
- `DELETE /products/{id}/`: Delete a video game by ID.

### Orders

- `GET /orders/`: List all orders.
- `POST /orders/`: Create a new order.
- `GET /orders/{id}/`: Retrieve an order by ID.
- `PUT /orders/{id}/`: Update an order by ID.
- `DELETE /orders/{id}/`: Delete an order by ID.

### Product Reviews

- `GET /reviews/`: List all reviews.
- `POST /reviews/`: Create a new review.

### Wishlist

- `GET /wishlist/`: List all wishlist items.
- `POST /wishlist/`: Add a video game to the wishlist.
- `DELETE /wishlist/{id}/`: Remove a video game from the wishlist.

## Deployment

The API is deployed and accessible at: [https://chornate.pythonanywhere.com/api/](https://chornate.pythonanywhere.com/api/)

