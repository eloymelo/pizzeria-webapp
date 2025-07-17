# Pizzeria - Web Application

This is the web application version of the Pizzeria project, built with Python and the Django framework. It provides an interface for users to view pizzas and their toppings.

This repository contains the application logic. The database schema and SQL practice queries are maintained in the separate [`pizzeria-database`](https://github.com/eloymelo/pizzeria-database) repository.

## Current Status

The project is in the initial setup phase.
* The core Django project and `pizzas` app have been created.
* Database models for `Pizza` and `Topping` have been defined.
* The Django admin site has been configured to manage pizzas and toppings.

## How to Run (for Development)

1.  Clone this repository to your local machine.
2.  Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  Install the project's dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4.  Apply the database migrations:
    ```sh
    python3 manage.py migrate
    ```
5.  Create a superuser account to access the admin site:
    ```sh
    python3 manage.py createsuperuser
    ```
6.  Run the development server:
    ```sh
    python3 manage.py runserver
    ```
7.  Access the site at `http://localhost:8000` and the admin panel at `http://localhost:8000/admin/`.

## Technologies Used

* Python
* Django