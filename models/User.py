from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)  # Nuevo campo
    email = db.Column(db.String(50), unique=True, nullable=False)
    
    def __init__(self, name, lastname, email):  
        self.name = name
        self.lastname = lastname
        self.email = email
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,  # Incluir en la respuesta
            "email": self.email,
        }
