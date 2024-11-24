from flask import Flask,render_template,request,redirect
from models import db,Carro
from config import Config

app  = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)