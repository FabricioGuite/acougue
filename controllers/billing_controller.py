from flask import Blueprint, render_template,redirect,url_for,request, flash
from models import BillingForm,Billing,BillingBillingForms, Order, db

billing = Blueprint("billing", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@billing.route("/")
def billing_index():
    return render_template("/billing/billing_index.html")

@billing.route("/register_billing")
def register_billing():
    billing_forms = BillingForm.get_data()
    orders = Order.get_orders_info()
    return render_template("/billing/register_billing.html",  billing_forms = billing_forms, orders = orders)

@billing.route("/save_billing", methods = ["POST"])
def save_billing():
    value = request.form.get("value")
    billing_date = request.form.get("billing_date")
    billing_form_id = request.form.get("billing_form_id")
    order_id = request.form.get("order_id")

    id = Billing.save(value, billing_date, order_id)
    aux = BillingBillingForms(billing_id= id,value = value, billing_form_id = int(billing_form_id))

    db.session.add(aux)
    db.session.commit()

    return redirect(url_for("admin.billing.view_billing"))




@billing.route("/register_billing_forms")
def register_billing_forms():
    billing = Billing.get_data()
    return render_template("/billing/register_billing_forms.html", billing = billing)

@billing.route("/save_billing_forms", methods = ["POST"])
def save_billing_forms():
    name = request.form.get("name")
    description = request.form.get("description")

    id = BillingForm.save(name, description)
    db.session.commit()

    return redirect(url_for("admin.billing.view_billing_forms"))



@billing.route("/view_billing_forms")
def view_billing_forms():
    billing_forms = BillingForm.get_data()
    return render_template("/billing/view_billing_forms.html", billing_forms = billing_forms)

@billing.route("/view_billing")
def view_billing():
    billings = db.session.query(Billing.id,Billing.value, Billing.billing_date, BillingForm.name,Billing.order_id)\
        .join(BillingBillingForms, Billing.id == BillingBillingForms.billing_id)\
        .join(BillingForm, BillingBillingForms.billing_form_id == BillingForm.id)\
        .all()
    return render_template("/billing/view_billings.html", billings=billings)

@billing.route("/delete_billing/<id>")
def delete_billing(id):
    if Billing.delete_billing(id):
        flash("Cobrança Excluído com sucesso!!", "success")
    else:
        flash("Cobrança não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.billing.view_billing"))

@billing.route("/delete_billing_form/<id>")
def delete_billing_form(id):
    if BillingForm.delete_billing_form(id):
        flash("Forma de Cobrança Excluído com sucesso!!", "success")
    else:
        flash("Forma de Cobrança não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.billing.view_billing_forms"))