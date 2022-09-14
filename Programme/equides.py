from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://team:*Azerty01*@localhost/projet_equides'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATION' ] = False
db = SQLAlchemy(app)


class Equides(db.Model):
    id_eq = db.Column(db.Integer, primary_key=True)
    nom_eq = db.Column(db.String(80))
    sexe_eq = db.Column(db.Boolean)
    puce_eq = db.Column(db.Numeric)
    sire_eq = db.Column(db.String(10))
    race_eq = db.relationship('Race', backref='races_equides')

    def __init__(self, nom_eq, race_eq, sexe_eq, puce_eq):
         self.nom_eq = nom_eq
         self.sexe_eq = sexe_eq
         self.puce_eq = puce_eq



class Race(db.Model):
    id_race = db.Column(db.Integer, db.ForeignKey('equides.race_eq'), primary_key=True)
    nom_race = db.Column(db.String)


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