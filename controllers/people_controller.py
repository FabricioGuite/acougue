from flask import Blueprint, render_template,redirect,url_for, request, flash

from models import Employee, Client,db

people = Blueprint("people", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@people.route("/")
def people_index():
    return render_template("/people/people_index.html")

@people.route("/register_employee")
def register_employee():
    return render_template("/people/register_employee.html")

@people.route("/view_employees")
def view_employees():
    employees = Employee.get_employees()
    return render_template("/people/view_employees.html", employees = employees)

@people.route("/save_employees", methods = ["POST"])
def save_employees():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    cpf = request.form.get("cpf")
    created_at = request.form.get("created_at")

    Employee.save_employee(username, email, password, cpf , created_at)

    return redirect(url_for('admin.people.view_employees'))

@people.route("/register_client")
def register_client():
    return render_template("/people/register_client.html")

@people.route("/view_clients")
def view_clients():
    clients = Client.get_clients()
    return render_template("/people/view_clients.html", clients = clients)

@people.route("/save_clients", methods = ["POST"])
def save_clients():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    cpf = request.form.get("cpf")
    created_at = request.form.get("created_at")

    Client.save_client(username, email, password, cpf , created_at)

    return redirect(url_for('admin.people.view_clients'))

@people.route("/delete_employee/<id>")
def delete_employee(id):
    if Employee.delete_employee(id):
        flash("Funcionario Excluído com sucesso!!", "success")
    else:
        flash("Funcionario não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.people.view_employees"))

@people.route("/delete_client/<id>")
def delete_client(id):
    if Client.delete_client(id):
        flash("Cliente Excluído com sucesso!!", "success")
    else:
        flash("Cliente não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.people.view_clients"))