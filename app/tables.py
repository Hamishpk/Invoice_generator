from flask_table import Table, Col, LinkCol

""" Table objects to display database tables on frontend"""

class Products(Table):
    id = Col('Id', show=False)
    product_id = Col('Product ID')
    description = Col('Description')
    price = Col('Price')

class Clients(Table):
    id = Col('Id', show=False)
    name = Col('Name')
    address = Col('Addess')

class Invoices(Table):
    id = Col('Id')
    client_name = Col('Client name')
    issue_date = Col('Issue date')
    due_date = Col('Due date')
    amount_bt = Col('Amount Before VAT')
    amount_at = Col('Amount After VAT')
    edit_invoice = LinkCol('Edit', 'edit_invoice', url_kwargs=dict(id='id'))
    view = LinkCol('View', 'view_invoice', url_kwargs=dict(id='id'))

class Items(Table):
    id = Col('Id', show=False)
    invoice_id = Col('Invoice_id   ')
    item = Col('Product_id   ')
    quantity = Col('Quantity   ')
    item_price = Col('Item Price (GBP)')
    total_price = Col('Total Price (GBP)')
    edit_item = LinkCol('Edit', 'edit_item', url_kwargs=dict(id='id'))

class ItemForInvoice(Table):
    id = Col('Id', show=False)
    item = Col('Product_id')
    quantity = Col('Quantity')
    item_price = Col('Item Price (GBP)')
    total_price = Col('Total Price (GBP)')
