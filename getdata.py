import time
import os
import random
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "getdata.db"))

from flask import Flask,\
        render_template,\
        request,\
        redirect,\
        url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = database_file

db = SQLAlchemy(app)

def findMaxPrice():
    stArr = Stock.query.filter_by(deleted=0).all()
    print(stArr)
    arr = []
    for ii in stArr:
        arr.append(ii.price)
    return max(arr)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cmpid = db.Column(db.Integer)
    qty = db.Column(db.Integer)
    price = db.Column(db.Numeric(10,2))
    deleted = db.Column(db.Boolean)

# https://stackoverflow.com/questions/31928520/sqlalchemy-is-there-a-way-to-see-what-is-currently-in-the-session

@app.route('/')
def index():
    not_deleted = Stock.query.filter_by(deleted=False).all()
    deleted = Stock.query.filter_by(deleted=True).all()
    return render_template('getdata.html',not_del=not_deleted, deleted=deleted)
@app.route('/add', methods=['POST'])
def add():
    stock = Stock(qty=request.form['fqty'],price=request.form['fprice'],deleted=False)
    db.session.add(stock)
    print(stock)
    db.session.commit()
    return redirect(url_for('index'))
@app.route('/sell', methods=['POST'])
def sellit():
    qty_sell = int(request.form['sellqty'])
    while(qty_sell > 0):
        maxPrice = findMaxPrice()
        maxRecord = Stock.query.filter_by(price=maxPrice).first()
        print(maxRecord.qty)
        time.sleep(10)
        maxRecord.qty = int(maxRecord.qty)
        if(qty_sell < maxRecord.qty):
            # setting remaining qty
            maxRecord.qty =  maxRecord.qty - qty_sell
            qty_sell = 0
        else:
            # removing the record
            qty_sell = qty_sell - maxRecord.qty
            maxRecord.qty = 0
            maxRecord.deleted = 1
            #db.session.delete(maxRecord)
    print("--DIRTY--")
    print(db.session.dirty._members)
    db.session.commit()
    print("--DELETED--")
    print(db.session.deleted._members)
    time.sleep(10)
    return redirect(url_for('index'))
    #Use bottom entry for non-localhost
    #return redirect(request.referrer)


# @app.route('/complete/<id>')
# def complete(id):
#     stock = Stock.query.filter_by(id=int(id)).first()
#     stock.complete = True
#     db.session.commit()
#     return redirect(url_for('index'))
 
if __name__ == '__main__':
    app.run(debug=True)

