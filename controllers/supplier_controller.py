from flask import Blueprint, render_template,redirect,url_for, request, flash
from models import Supplier, Employee,User, db

supplier = Blueprint("supplier", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@supplier.route("/")
def supplier_index():
    return render_template("/supplier/supplier_index.html")

@supplier.route("/register_supplier")
def register_supplier():
    general = User.query.join(Employee, Employee.id == User.id).add_columns(Employee.id, User.username).all()
    return render_template("/supplier/register_supplier.html", general = general)

@supplier.route("/view_suppliers")
def view_suppliers():
    suppliers = Supplier.get_suppliers()
    return render_template("/supplier/view_suppliers.html", suppliers = suppliers)

@supplier.route("/save_suppliers", methods = ["POST"])
def save_suppliers():
    name = request.form.get("name")
    description = request.form.get("description")
    grade = request.form.get("grade")
    employee_id = request.form.get("general")

    Supplier.save_supplier(name, description, grade, employee_id)

    return redirect(url_for('admin.supplier.view_suppliers'))

@supplier.route("/delete_supplier/<id>")
def delete_supplier(id):
    if Supplier.delete_supplier(id):
        flash("Fornecedor Excluído com sucesso!!", "success")
    else:
        flash("Fornecedor não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.supplier.view_suppliers"))