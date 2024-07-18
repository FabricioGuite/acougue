from flask import Blueprint, render_template,redirect,url_for, request, flash
from models import Sensor, Actuator,Microcontroller, Device, db
iot = Blueprint("iot", __name__, template_folder = './views/admin/', static_folder='./static/', root_path="./")

@iot.route("/")
def iot_index():
    return render_template("/iot/iot_index.html")

@iot.route("/register_sensor")
def register_sensor():
    return render_template("/iot/register_sensor.html")

@iot.route("/view_sensors")
def view_sensors():
    sensors = Sensor.get_sensors()
    return render_template("/iot/view_sensors.html", sensors = sensors)

@iot.route("/save_sensors", methods = ["POST"])
def save_sensors():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    measure = request.form.get("measure")
    voltage = request.form.get("voltage")
    is_active = True if request.form.get("is_active") == "on" else False

    Sensor.save_sensor(name, brand, model, description ,voltage, is_active, measure)

    return redirect(url_for('admin.iot.view_sensors'))

@iot.route("/update_sensor/<id>")
def update_sensor(id):
    sensor = db.session.query(Device, Sensor)\
                        .join(Sensor, Sensor.id == Device.id)\
                        .filter(Sensor.id == int(id)).first()
    
    return render_template("/iot/update_sensor.html", sensor = sensor)

@iot.route("/save_sensor_changes", methods = ["POST"])
def save_sensor_changes():
    data = request.form.copy()
    data["is_active"] = data.get("is_active") == "on"
    Sensor.update_sensor(data)
    return redirect(url_for("admin.iot.view_sensors"))

@iot.route("/delete_sensor/<id>")
def delete_sensor(id):
    if Sensor.delete_sensor(id):
        flash("Dispositivo Sensor Excluído com sucesso!!", "success")
    else:
        flash("Dispositivo Sensor não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.iot.view_sensors"))



@iot.route("/view_actuators")
def view_actuators():
    actuators = Actuator.get_actuators()
    return render_template("/iot/view_actuators.html", actuators = actuators)

@iot.route("/register_actuator")
def register_actuator():
    return render_template("/iot/register_actuator.html")

@iot.route("/save_actuators", methods = ["POST"])
def save_actuators():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    actuator_type= request.form.get("actuator_type")
    voltage = request.form.get("voltage")
    is_active = True if request.form.get("is_active") == "on" else False

    Actuator.save_actuator(name, brand, model, description ,voltage, is_active, actuator_type)

    return redirect(url_for('admin.iot.view_actuators'))





@iot.route("/view_microcontrollers")
def view_microcontrollers():
    microcontrollers = Microcontroller.get_microcontrollers()
    return render_template("/iot/view_microcontrollers.html", microcontrollers = microcontrollers)

@iot.route("/register_microcontroller")
def register_microcontroller():
    return render_template("/iot/register_microcontroller.html")

@iot.route("/save_microcontrollers", methods = ["POST"])
def save_microcontrollers():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    port = request.form.get("port")
    voltage = request.form.get("voltage")
    is_active = True if request.form.get("is_active") == "on" else False

    Microcontroller.save_microcontroller(name, brand, model, description ,voltage, is_active, port)

    return redirect(url_for('admin.iot.view_microcontrollers'))

@iot.route("/delete_actuator/<id>")
def delete_actuator(id):
    if Actuator.delete_actuator(id):
        flash("Dispositivo Atudor Excluído com sucesso!!", "success")
    else:
        flash("Dispositivo Atuador não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.iot.view_actuators"))

@iot.route("/delete_microcontroller/<id>")
def delete_microcontroller(id):
    if Microcontroller.delete_microcontroller(id):
        flash("Dispositivo microcontrolador Excluído com sucesso!!", "success")
    else:
        flash("Dispositivo microcontrolador não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.iot.view_microcontrollers"))

