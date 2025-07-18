# Pizzeria - Web Application

This is the web application version of the Pizzeria project, built with Python and the Django framework. It provides a web interface for users to view different pizzas and the toppings available for each one.

## Project Ecosystem

This application is part of a larger project-driven learning exercise. The related components are:

* **[pizzeria-cli](https://github.com/eloymelo/pizzeria-cli):** The original command-line application containing the core Python logic.
* **[pizzeria-database](https://github.com/eloymelo/pizzeria-database):** The SQL scripts used to design the database schema.

## Current Features

* Displays a list of all available pizzas on the main page.
* Provides a detail page for each pizza, listing its current toppings.
* Includes a functional web form to add new toppings to a specific pizza.
* The Django admin site is configured for managing all data.
* Styled with the Bootstrap framework for a clean, responsive layout.

## How to Run (for Development)

1.  Clone this repository to your local machine.
2.  Create and activate a virtual environment.
3.  Install the project's dependencies: `pip install -r requirements.txt`
4.  Apply the database migrations: `python3 manage.py migrate`
5.  Create a superuser account: `python3 manage.py createsuperuser`
6.  Run the development server: `python3 manage.py runserver`
7.  Access the site at `http://localhost:8000/`.

## Technologies Used

* Python
* Django
* Bootstrap3