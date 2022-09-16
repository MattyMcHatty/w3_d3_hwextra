from app import app
from flask import render_template
from models.orders_to_fulfill import orders

@app.route('/orders')
def index():
    return render_template('index.html', orders=orders)

@app.route('/orders/<order_number>')
def customer_order(order_number):
    return render_template('order.html', order=orders[int(order_number)])