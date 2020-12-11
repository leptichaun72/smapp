from app import db

class Broker(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25),unique=True,nullable=False)
    date_created = db.Column(db.DateTime(timezone=True),nullable=False)

#class Stock(db.Model):
#    id = db.Columm(db.Integer,primary_key=True)
#    name = db.Column(db.Text,unique=True)
#    symbol = db.Column(db.String(8),unique=True,nullable=False)
#    lots = db.relationship("Lot
