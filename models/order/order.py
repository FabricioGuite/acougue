from models.db import db
from models import Employee
from models import Client
from models import Product

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer(), primary_key=True)
    employee_id = db.Column(db.Integer(), db.ForeignKey(Employee.id, ondelete='CASCADE'), nullable=False)
    product_id = db.Column(db.Integer(), db.ForeignKey(Product.id), nullable=False)
    client_id = db.Column(db.Integer(), db.ForeignKey(Client.id), nullable=True)
    order_datetime = db.Column(db.DateTime, nullable = False)

    billing = db.relationship('Billing', backref='orders')
    def get_orders():
        return Order.query.all()
        
    def get_orders_info():
        return Order.query.join(Client, Client.id == Order.client_id).add_columns(Order.id,Client.username).all()

    def save_order(employee_id, product_id, client_id, order_datetime):
        order = Order(employee_id = employee_id, product_id = product_id, client_id = client_id, order_datetime = order_datetime)

        db.session.add(order)
        db.session.commit()

        return order.id
    
    def delete_order(id):
        try:
            Order.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False