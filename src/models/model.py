from flask_sqlalchemy import SQLAlchemy
from flask import *
from flask_migrate import Migrate
from flask_login import UserMixin,LoginManager

app=Flask(__name__, template_folder='c:/Users/HP/Documents/Exam_Flask/src/templates/')
app.config.from_pyfile('../../config.py')
login_manager = LoginManager(app)
db=SQLAlchemy(app)
migrate = Migrate(app, db) 

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password =db.Column(db.String(50))
    
class Event(db.Model):
    __tablename__='events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    date = db.Column(db.DateTime)
    duration=db.Column(db.Float) # in hours
    description=db.Column(db.Text)
    event_type_id = db.Column(db.Integer, db.ForeignKey('categories_events.id'))
    event_type=db.relationship('CategorieEvent', backref='events')
    salle_id = db.Column(db.Integer, db.ForeignKey('salles.id'))
    salle=db.relationship('Salle', backref='events')
    tour_id=db.Column(db.Integer, db.ForeignKey('tours.id'),nullable=True)
    tour=db.relationship("Tour", backref='events')
    nb_places_availables=db.Column(db.Integer)
    image=db.Column(db.String(350))
    note = db.Column(db.Float)
    etat=db.Column(db.String(50))
    
class Tour(db.Model):
    __tablename__='tours'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    description=db.Column(db.Text)
    image=db.Column(db.String(350),nullable=True)
    
    
class CategorieEvent(db.Model):
    __tablename__='categories_events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Salle(db.Model):
    __tablename__='salles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    capacite = db.Column(db.Integer)
    salle_type_id = db.Column(db.Integer, db.ForeignKey('categories_salle.id'))
    salle_type=db.relationship('CategorieSalle', backref='salles')
    adresse=db.Column(db.String(100))
    
   
class CategorieSalle(db.Model):
    __tablename__='categories_salle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    
class Place(db.Model):
    __tablename__="places"
    id = db.Column(db.Integer, primary_key=True)
    numero=db.Column(db.Integer,nullable =False)
    salle_id= db.Column(db.Integer, db.ForeignKey('salles.id'))
    salle=db.relationship('Salle', backref='places')
    place_type_id=db.Column(db.Integer, db.ForeignKey('categories_place.id'))
    place_type=db.relationship('CategoriePlace', backref='places')
    etat_place = db.Column(db.String(100))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    event=db.relationship('Event', backref='places')
    prix=db.Column(db.Float) 
    
class CategoriePlace(db.Model):
    __tablename__='categories_place'
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    
class Paiement(db.Model):
    __tablename__ = "paiements"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    montant = db.Column(db.Float, nullable=False)
    mode_paiement = db.Column(db.String(255), nullable=False)
    date_paiement = db.Column(db.DateTime, nullable=False)
    statut = db.Column(db.String(255), nullable=False, default="en attente")

    def __repr__(self):
        return f"<Paiement(id={self.id}, montant={self.montant}, mode_paiement={self.mode_paiement}, date_paiement={self.date_paiement}, statut={self.statut})>"

class CartItem(db.Model):
    __tablename__ = 'cart_items'
    id = db.Column(db.Integer, primary_key=True)
    ticket_type = db.Column(db.String(80))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    total_price = db.Column(db.Float)
       
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
def getUserByName(password,username):
    return User.query.filter_by(username,password).first()
    
    
with app.app_context():
    db.create_all()