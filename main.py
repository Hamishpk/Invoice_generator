from app.app import app, db
from app.__init__ import init_db, db_session
from app.tables import Products, Invoices, Items, ItemForInvoice
from app.forms import ProductForm, ClientForm, ItemForm
from app.forms import InvoiceForm, PopulateInvoice
from flask import flash, render_template, request, redirect, jsonify, url_for
from app.models import Product, Client, Invoice, Item
import uuid


init_db(db)

@app.route('/')
def index():
    """Displays home screen invoice table"""
    qry_invoices = db_session.query(Invoice)
    results = qry_invoices.all()
    table = Invoices(results)

    return render_template('index.html', table = table)


@app.route('/add_invoice', methods=['GET', 'POST'])
def new_invoice():
    """
    Loads form to create new invoice.
    -----
    CURRENTLY NEEDS MODIFYING ONCE FRONT END IS COMPLETE
    -----
    """
    invoice_id = str(uuid.uuid4())

    return render_template('add_invoice.html', invoice_id = invoice_id)

@app.route('/save_invoice', methods=['POST'])
def save_invoice():
    invoice = Invoice()
    invoice.invoice_id = request.form['invoice_id']
    invoice.client_name = request.form['client_name']
    invoice.issue_date = request.form['issue_date']
    invoice.due_date = request.form['due_date']
    total = 0
    qry = db_session.query(Item).filter(Item.invoice_id == invoice.invoice_id)
    results = qry.all()
    for i in results:
        total += i.total_price
    invoice.amount_bt = total
    invoice.amount_at = round(float(invoice.amount_bt) * 1.2, 2)

    db_session.add(invoice)
    db_session.commit()
    return redirect(url_for('index'))

@app.route('/process', methods=['GET', 'POST'])
def process():
    """
    Adds new item to the product table.
    -----
    Invoice ID is taken from the html and multiple Items
    can be created for that invoice.

    """
    item = Item()
    invoice_id = request.form['invoice_id']
    product = request.form['product']
    quantity = request.form['quantity']
    #### To add ####
    #if statement to check price is none and if so pull stock price from db
    item_price = request.form['price']
    total_price = round(float(quantity)*float(item_price))
    item.invoice_id = invoice_id
    item.item = product
    item.quantity = quantity
    item.item_price = item_price
    item.total_price = total_price
    db_session.add(item)
    db_session.commit()

    qry = db_session.query(Item).filter(Item.invoice_id == invoice_id)
    results = qry.all()
    print(invoice_id)
    table = Items(results)

    return jsonify(my_table = table.__html__())

def save_invoice_changes(invoice, form, new=False):

    """
    Helper function to update information to database.
    -----
    Parameters: Type
    invoice - Invoice
    form - Invoiceform
    new - Boolean
    -----
    Commits or updates line in invoice table
    -----
    Returns - Nothing
    """

    invoice.client_name = form.client_name.data
    invoice.issue_date = form.issue_date.data
    invoice.due_date = form.due_date.data
    qry = db_session.query(Item).filter(Item.invoice_id == invoice.invoice_id)
    total = 0
    for i in qry:
        total += i.total_price
    invoice.amount_bt = total
    invoice.amount_at = round(float(invoice.amount_bt) * 1.2, 2)

    if new:
        db_session.add(invoice)

    db_session.commit()


@app.route('/edit_invoice/<int:id>', methods=['GET', 'POST'])
def edit_invoice(id):
    """
    Routes to edit invoice page
    -----
    Parameters: Type
    id: Int
    """
    qry = db_session.query(Invoice).filter(
                Invoice.id==id)
    invoice = qry.first()
    invoice_id = invoice.invoice_id

    qry1 = db_session.query(Item).filter(Item.invoice_id == invoice_id)
    y = qry1.all()
    table = Items(y)

    if invoice:
        form = InvoiceForm(formdata=request.form, obj=invoice)
        if request.method == 'POST' and form.validate():
            save_invoice_changes(invoice, form)
            return redirect('/')

    return render_template('edit_invoice.html', form=form, table = table)

@app.route('/edit_item/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    """
    Routes to edit invoice page
    -----
    Parameters: Type
    id: Int
    """
    qry = db_session.query(Item).filter(Item.id==id)
    item = qry.first()

    if item:
        form = ItemForm(formdata=request.form, obj=item)
        if request.method == 'POST' and form.validate():
            save_item_changes(item, form)
            return redirect('/')
    else:
        return 'Error loading #{id}'.format(id=id)

    return render_template('edit_item.html', form=form)

def save_item_changes(item, form, new=False):

    """
    Helper function to update information to database.
    -----
    Parameters: Type
    item - Item
    form - Itemform
    new - Boolean
    -----
    Commits or updates line in item table
    -----
    Returns - Nothing
    """
    item.item = form.item.data
    item.quantity = form.quantity.data
    item.item_price = form.item_price.data
    item.total_price = round(float(form.item_price.data) * float(form.quantity.data), 2)

    if new:
        db_session.add(item)

    db_session.commit()

@app.route('/view_invoice<int:id>', methods=['GET'])
def view_invoice(id):
    """
    Creates invoice html and displayes on screen
    """
    qry = db_session.query(Invoice).filter(Invoice.id==id)
    invoice = qry.first()
    client_name = invoice.client_name
    invoice_id = invoice.invoice_id
    issue_date = invoice.issue_date
    due_date = invoice.due_date
    amount_bt = invoice.amount_bt
    amount_at = invoice.amount_at

    product_qry = db_session.query(Item).filter(
                    Item.invoice_id == invoice.invoice_id)
    table = ItemForInvoice(product_qry)

    return render_template('invoice.html', table=table,
                            client_name = client_name,
                            invoice_id = invoice_id,
                            issue_date = issue_date,
                            due_date = due_date,
                            amount_bt = amount_bt,
                            amount_at = amount_at,)



if __name__ == "__main__":
    app.run(debug=True)
