from models.db import db
from models import Order

class Billing(db.Model):
    __tablename__ = 'billings'
    id = db.Column('id', db.Integer(), primary_key=True)
    value = db.Column(db.Float())
    billing_date = db.Column(db.DateTime())
    order_id = db.Column(db.Integer(), db.ForeignKey(Order.id))

    billing_forms = db.relationship('BillingForm', back_populates = "billings", secondary='billing_billing_forms')

    def get_data():
        return Billing.query.all()
    
    def save(value, billing_date, order_id):
        billings = Billing(value=float(value), billing_date = billing_date, order_id = order_id)

        db.session.add(billings)
        db.session.commit()

        return billings.id
    
    def delete_billing(id):
        try:
            Billing.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False