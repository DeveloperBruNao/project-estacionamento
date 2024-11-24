from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Carro(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    placa = db.Column(db.String(7),unique=True,nullable=False)
    modelo = db.Column(db.String(50),nullable=False)
    vaga = db.Column(db.Integer,unique=True,nullable=False)