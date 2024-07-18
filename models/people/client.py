from models.db import db

class Client(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(1024), nullable=False)
    cpf = db.Column(db.String(11))
    created_at = db.Column(db.Date())

    orders =  db.relationship('Order', backref='clients')

    def get_clients():
        return Client.query.all()

    def save_client(username, email, password, cpf, created_at):
        client = Client(username = username, email = email, password = password, cpf = cpf, created_at = created_at)

        db.session.add(client)
        db.session.commit()

        return client.id
    
    def delete_client(id):
        try:
            Client.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False
