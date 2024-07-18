from models.db import db

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(50))
    price = db.Column(db.Float)
    available_quantity = db.Column(db.Float)
    description = db.Column(db.String(50))
    
    orders = db.relationship('Order', backref='products')

    def get_products():
        return Product.query.all()

    def save_product(name, price , available_quantity, description):
        product = Product(name = name, price  = price , available_quantity = available_quantity, description = description)

        db.session.add(product)
        db.session.commit()

    def delete_product(id):
        try:
            Product.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False