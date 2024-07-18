from models import db, Device

class Actuator(db.Model):
    __tablename__ = "actuators"
    id = db.Column("id", db.Integer, db.ForeignKey(Device.id), primary_key=True)
    actuator_type = db.Column(db.String(20))

    activations = db.relationship("Activation", backref="actuators", lazy=True)

    def get_actuators():
        actuators = Actuator.query.join(Device, Device.id == Actuator.id)\
                    .add_columns(Actuator.id, Device.name, Device.brand, Device.model, 
                                 Device.voltage, Device.description,  Device.is_active, Actuator.actuator_type).all()
        
        return actuators
    
    def save_actuator(name, brand, model, description, voltage, is_active, actuator_type):
        device = Device(name=name, brand=brand, model=model, 
                            description=description, voltage=voltage, is_active=is_active)
    
        actuator = Actuator(id=device.id, actuator_type=actuator_type)
        
        device.actuators.append(actuator)
        db.session.add(device)
        db.session.commit()

    def delete_actuator(id):
        try:
            Actuator.query.filter_by(id=id).delete()
            Device.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False

    def delete_actuator_by_actuator_type(actuator_type):
        Actuator.query.filter_by(actuator_type=actuator_type).delete()
        db.session.commit()

    def update_actuator(data):
        Device.query.filter_by(id=data['id'])\
                .update(dict(name=data['name'], brand=data['brand'], model=data['model'], 
                        voltage=data['voltage'], description=data['description'], 
                        is_active=data['is_active']))
        
        Actuator.query.filter_by(id=data['id'])\
                        .update(dict(actuator_type=data['actuator_type']))
        db.session.commit()