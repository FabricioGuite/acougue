from flask import Blueprint, render_template,redirect,url_for, request, flash
from models import Order, Employee, Client, Product, User, db

order = Blueprint("order", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@order.route("/")
def order_index():
    return render_template("/order/order_index.html")

@order.route("/register_order")
def register_order():
    general = User.query.join(Employee, Employee.id == User.id).add_columns(Employee.id, User.username).all()
    product = Product.query.all()
    client = Client.query.all()
    return render_template("/order/register_order.html", general = general, product = product, client = client)

@order.route("/view_orders")
def view_orders():
    orders = Order.get_orders()
    return render_template("/order/view_orders.html", orders = orders)

@order.route("/save_orders", methods=['POST'])
def save_orders():
    employee_id = request.form.get("general")
    product_id = request.form.get("product")
    client_id = request.form.get("client")
    order_datetime = request.form.get("order_datetime")

    Order.save_order(employee_id, product_id, client_id, order_datetime)
    db.session.commit()

    return redirect(url_for('admin.order.view_orders'))

@order.route("/delete_order/<id>")
def delete_order(id):
    if Order.delete_order(id):
        flash("Pedido Excluído com sucesso!!", "success")
    else:
        flash("Pedido não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.order.view_orders"))