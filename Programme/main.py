from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://team:*Azerty01*@localhost/projet_equides'
db = SQLAlchemy(app)
db.create_all()

class Equides(db.Model):
    id_eq = db.Column(db.Integer, primary_key=True)
    nom_eq = db.Column(db.String(80))
    race_eq = db.Column(db.String(120))
    sexe_eq = db.Column(db.Boolean)
    puce_eq = db.Column(db.Numeric)
    sire_eq = db.Column(db.String(10))

    def __init__(self, nom_eq, race_eq, sexe_eq, puce_eq):
         self.nom_eq = nom_eq
         self.race_eq = race_eq
         self.sexe_eq = sexe_eq
         self.puce_eq = puce_eq

equides = Equides.query.all()


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/chevaux')
def show_all():
   return render_template('chevaux.html', equides = Equides.query.all() )

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)