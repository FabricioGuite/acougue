from models.db import db

class BillingForm(db.Model):
    __tablename__ = "billing_forms"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))

    billings = db.relationship('Billing', back_populates = "billing_forms", secondary='billing_billing_forms')

    def get_data():
        return BillingForm.query.all()

    def save(name, description):
        billing = BillingForm(name = name, description = description)

        db.session.add(billing)
        db.session.commit()

        return billing.id
    
    def delete_billing_form(id):
        try:
            BillingForm.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False