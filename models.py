from app import db

class Stock(db.Model):
    id = db.Columm(db.Integer,primary_key=True)
    name = db.Column(db.Text,unique=True)
    symbol = db.Column(db.String(8),unique=True,nullable=False)
#    lots = db.relationship("Lot
