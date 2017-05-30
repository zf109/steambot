from config import Config as conf
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
# import sqlalchemy as db

# engine = create_engine(conf.SQL_ALCHEMY_URI, echo=True)
# Model = declarative_base()


from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config.from_object(conf)

db = SQLAlchemy(app)


class App(db.Model):
    __tablename__ = 'app_info'
    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer)
    name = db.Column(db.String(250))
    description = db.Column(db.String())
    price_info = db.relationship('Price', backref='price_info', uselist=False)


class Price(db.Model):
    __tablename__ = 'price_info'
    id = db.Column(db.Integer, primary_key=True)
    app_db_id = db.Column(db.Integer, db.ForeignKey('app_info.id'))
    price = db.Column(db.Float)
    discount = db.Column(db.Float)
    price_original = db.Column(db.Float)
    currency = db.Column(db.String(5))

