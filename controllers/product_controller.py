from flask import Blueprint, render_template,redirect,url_for, request, flash
from models import Product,db

product = Blueprint("product", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@product.route("/")
def products_index():
    return render_template("/product/product_index.html")

@product.route("/register_product")
def register_product():
    return render_template("/product/register_product.html")

@product.route("/view_products")
def view_products():
    products = Product.get_products()
    return render_template("/product/view_products.html", products = products)

@product.route("/save_products", methods = ["POST"])
def save_products():
    name = request.form.get("name")
    price = request.form.get("price")
    available_quantity = request.form.get("available_quantity")
    description = request.form.get("description")

    Product.save_product(name, price, available_quantity, description)

    return redirect(url_for('admin.product.view_products'))

@product.route("/delete_product/<id>")
def delete_product(id):
    if Product.delete_product(id):
        flash("Produto Excluído com sucesso!!", "success")
    else:
        flash("Produto não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.product.view_products"))