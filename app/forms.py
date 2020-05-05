from wtforms import Form, StringField, SelectField, SubmitField

"""Form classes to collect inputs from HTML"""

class ProductForm(Form):
    product_id = StringField('product_id')
    description = StringField('description')
    price = StringField('price')

class ClientForm(Form):
    name = StringField('name')
    address = StringField('address')

class InvoiceForm(Form):
    clients = [('Acme Inc', 'Acme Inc'),
                ('ABC Ltd', 'ABC Ltd'),
                ('AIIViews Ltd', 'AIIViews Ltd'),
                ('Barton Smith Ltd', 'Barton Smith Ltd')]


    client_name = SelectField(choices = clients)
    issue_date = StringField('issue_date')
    due_date = StringField('due_date')

class PopulateInvoice(Form):

    def __init__(self, client_name = None, address = None
                ,invoice_id = None, issue_date = None,
                due_date = None, amount_bt = None,
                amount_at = None):
        self.client_name = client_name
        self.address = address
        self.invoice_id = invoice_id
        self.issue_date = issue_date
        self.due_date = due_date
        self.amount_bt = amount_at
        self.amount_at = amount_bt

    client_name = ''
    address = ''
    invoice_id = ''
    issue_date = ''
    due_date = ''
    amount_bt = ''
    amount_at = ''


class ItemForm(Form):

    items = [('L452N', 'L452N'),
            ('L454N', 'L454N'),
            ('PU150', 'PU150'),
            ('PU300', 'PU300'),
            ('T423', 'T423'),
            ('PA344', 'PA344')]

    item = SelectField(choices = items)
    quantity = StringField('quantity')
    item_price = StringField('price')
    total_price = float()
    invoice_id = ''
