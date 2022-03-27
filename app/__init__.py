from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = "5f352379324c22463451387a0aec5d2f"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost/agendavacinacao"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app.models import tables
from app.controllers import cadastro, consulta