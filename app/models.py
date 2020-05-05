from app.app import app, db
import uuid

class Client(db.Model):

    """
    DATABASE TABLE TO STORE CLIENT INFORMATION

    Columns:
    id - Int
    Client Name - String
    Client Address - String
    """
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    def __init__(self, name=None, address=None):
        self.name = name
        self.address = address

class Product(db.Model):

    """
    DATABASE TABLE TO STORE PRODUCT INFORMATION

    Columns:
    id - Int
    Product Id - String
    Product Discription - String
    Price - Int
    """
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key = True)
    product_id = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)

    def __init__(self, product_id = None, description = None, price = None):
        self.product_id = product_id
        self.description = description
        self.price = price



class Invoice(db.Model):
    """
    DATABASE TABLE TO STORE INVOICE INFORMATION

    Columns:
    id - Int
    Client name - String
    issue_date - String
    Due date - String
    Amount Before Tax - Int
    Amount After Tax - Int
    Invoice ID - UUID
    """

    __tablename__ = 'invoice'

    id = db.Column(db.Integer, primary_key = True)
    client_name = db.Column(db.String)
    issue_date = db.Column(db.String)
    due_date = db.Column(db.String)
    amount_bt = db.Column(db.Integer)
    amount_at = db.Column(db.Integer)
    invoice_id = db.Column(db.String)

    def __init__(self, client_name=None, issue_date=None,
                due_date=None, amount_bt=None, amount_at=None):
        self.invoice_id = str(uuid.uuid4())
        self.client_name = client_name
        self.issue_date = issue_date
        self.due_date = due_date
        self.amount_bt = amount_bt
        self.amount_at = amount_at

class Item(db.Model):

    """
    DATABASE TABLE TO STORE SALE INFORMATION

    Columns:
    id - Int
    Item - String
    quantity - Int
    Item price - Int
    Total price - Int
    Invoice ID - Int, set up as ForeignKey to invoice table
    """
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key = True)
    item = db.Column(db.String)
    quantity = db.Column(db.Integer)
    item_price = db.Column(db.Integer)
    total_price = db.Column(db.Float)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))

    def __init__(self, product=None, item=None, quantity=None, item_price=None, total_price=None):
        self.item = item
        self.quantity = quantity
        self.item_price = item_price
        self.total_price = total_price
