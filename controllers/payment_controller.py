from flask import Blueprint, render_template,redirect,url_for, request, flash
from models import Payment, Employee, User, db

payment = Blueprint("payment", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@payment.route("/")
def payment_index():
    return render_template("/payment/payment_index.html")

@payment.route("/register_payment")
def register_payment():
    general = User.query.join(Employee, Employee.id == User.id).add_columns(Employee.id, User.username).all()
    return render_template("/payment/register_payment.html", general = general)

@payment.route("/view_payments")
def view_payments():
    payments = Payment.get_payments()
    return render_template("/payment/view_payments.html", payments = payments)

@payment.route("/save_payments", methods=['POST'])
def save_payments():
    employee_id = request.form.get("general")
    payment_datetime = request.form.get("payment_datetime")
    payment_value = request.form.get("payment_value")

    Payment.save_payment(employee_id, payment_datetime, payment_value)
    db.session.commit()

    return redirect(url_for('admin.payment.view_payments'))

@payment.route("/delete_payment/<id>")
def delete_payment(id):
    if Payment.delete_payment(id):
        flash("Pagamento Excluído com sucesso!!", "success")
    else:
        flash("Pagamento não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.payment.view_payments"))