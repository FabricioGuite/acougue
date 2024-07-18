from models.db import db
from models import Employee

class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer(), primary_key=True)
    employee_id = db.Column(db.Integer(), db.ForeignKey(Employee.id))
    payment_datetime = db.Column(db.DateTime(), nullable=False)
    payment_value = db.Column(db.Float(), nullable=True)

    def get_payments():
        return Payment.query.all()

    def save_payment(employee_id, payment_datetime, payment_value):
        payment = Payment(employee_id = employee_id, payment_datetime = payment_datetime, payment_value = payment_value)

        db.session.add(payment)
        db.session.commit()

        return payment.id
    
    def delete_payment(id):
        try:
            Payment.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False
