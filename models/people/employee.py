from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer(), db.ForeignKey(User.id), primary_key=True) # primary keys are required by SQLAlchemy
    cpf = db.Column(db.String(11))
    created_at = db.Column(db.Date())

    payments = db.relationship('Payment', backref='employees')
    orders = db.relationship('Order', backref='employees')

    def get_employees():
            employees = Employee.query.join(User, User.id == Employee.id)\
                        .add_columns(Employee.id, User.username, User.email, User.password,
                                    Employee.cpf, Employee.created_at).all()
            
            return employees
    
    def save_employee(username, email, password, cpf, created_at):
        user = User(username=username, email=email,password=generate_password_hash(password, method='sha256'))
    
        employee = Employee(id=user.id, cpf=cpf, created_at = created_at)
        
        user.employees.append(employee)
        db.session.add(user)
        db.session.commit()

        return employee.id
    
    def delete_employee(id):
        try:
            Employee.query.filter_by(id=id).delete()
            User.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False