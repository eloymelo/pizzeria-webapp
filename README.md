# Pizzeria - Web Application

This is the main web application for the Pizzeria project, built with Python and the Django framework. The goal of this repository is to practice and demonstrate web development skills. This is a work in progress.

## Project Ecosystem

This is one of three related repositories for the Pizzeria project:
* **[pizzeria-cli](https://github.com/eloymelo/pizzeria-cli):** The foundational Python logic in a command-line interface.
* **[pizzeria-database](https://github.com/eloymelo/pizzeria-database):** The SQL scripts for designing the database schema.
* **pizzeria-webapp (This one):** The final web application built with Django.

## Current Status

* Users can view a list of pizzas and the toppings for each pizza.
* A form allows for adding new toppings to a pizza's definition via the web interface.
* The Django admin site is fully configured for data management.
* The app currently uses Django's default **SQLite** database. It has **not** yet been integrated with the schema from the `pizzeria-database` project.

## Future Plans
* Implement a full ordering system.
* Add a user registration and authentication system.
* Integrate a PostgreSQL database based on the designed schema.

## Technologies Used
* Python
* Django
* Bootstrap