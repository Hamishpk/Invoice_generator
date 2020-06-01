# Invoice Generator

## Summary

A full stack application to generate Invoices. The user can add clients, products and create invoices. The invoices can be edited and viewed as a html.

## Technology

This is a Python application built with Flask, SQLAlchemy, SQLite DB, HTML and a little JQuery and AJAX.

I chose a SQLite database as it comes built in with Python, works well with SQLAlchemy and ideal for small applications. The database has 4 tables products, invoice, clients and items. Each sale item is connected to an invoice via a foreign key.

## Issues

Currently the application is a little messy whilst I play around with front end tools. As it stands you are able to add an invoice with multiple products and view that invoice. The edit invoice/item page need to be completed.

For now I have decided to focus on adding, editing and viewing invoices. The back end has functionality to store clients and products. These have not been added to the front end yet.

## Road map

1. Finish the edit invoice form
2. Add delete functions
3. Add entry validators to all forms
4. Add client and product functions + drop down menus on forms
5. Add styling to the invoices created
6. Include download to .pdf on all invoices

## Local installation

Install Python 3+

[Python Download](https://www.python.org/downloads/)

Install pip (Linux)

* `sudo apt install python3-pip`

Clone this repository

* `git clone https://github.com/Hamishpk/Invoice_generator.git`

* `cd invoice_generator`

Activate your virtualenv.

* `python3 -m venv <env name of your choice>`

Install packages from requirements.txt

* `pip install -r requirements.txt`


## Testing

Currently only manual testing has been completed on the application. Pytest to be added to each function.
