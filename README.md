# Invoice Generator

## Summary

A full stack application to generate Invoices. The user can add clients, products and create invoices. The invoices can be edited and viewed as a html.

## Technology

This is a Python application built with Flask, SQLAlchemy, SQLite DB, HTML and a little JQuery and AJAX.

I chose a SQLite database as it comes built in with Python, works well with SQLAlchemy and ideal for small applications. The database has 4 tables products, invoice, clients and items. Each sale item is connected to an invoice via a foreign key.

## Issues

Currently the application has one major bug in the front end of the add invoice form. Originally I planned to have the front end built entirely from HTML using Jinja2 however the add invoice form requires single page submissions of invoices. Because of this I decided to use JQuery and AJAX to build a more robust front end, which I’m currently in the process of doing.

## Road map

1. Finish the add invoice form
2. Add delete functions to all tables
3. Add entry validators to all forms
4. Add styling to the invoices created
5. Include download to .pdf on all invoices

## Local installation

Install Python 3+

[Python Download](https://www.python.org/downloads/)

Install pip (Linux)

* `code` sudo apt install python3-pip

Clone this repository

* `code` git clone https://github.com/Hamishpk/Invoice_generator.git

* `code` cd invoice_generator

Activate your virtualenv.

* `code` python3 -m venv <env name of your choice>

Install packages from requirements.txt

* `code` pip install -r requirements.txt


## Testing

Currently only manual testing has been completed on the application. Pytest to be added to each function.
