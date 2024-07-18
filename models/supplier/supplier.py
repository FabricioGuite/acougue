from models.db import db
from models import Employee

class Supplier(db.Model):
    __tablename__ = "supplier"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    grade = db.Column(db.Float)
    employee_id = db.Column(db.Integer(), db.ForeignKey(Employee.id, ondelete='CASCADE'), nullable=False)
    

    def get_suppliers():
        return Supplier.query.all()

    def save_supplier(name, description, grade, employee_id):
        supplier = Supplier(name = name,description = description, grade = grade, employee_id = employee_id)

        db.session.add(supplier)
        db.session.commit()

    def delete_supplier(id):
        try:
            Supplier.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False