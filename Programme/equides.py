from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://team:*Azerty01*@localhost/projet_equides'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATION' ] = True
db = SQLAlchemy(app)

class Races_equides(db.Model):
    id_race = db.Column(db.Integer, primary_key=True)
    nom_race = db.Column(db.String)

    # On crée une variable qui fait la connexion "back_populates" de la class Equides

    equides = relationship('Equides', back_populates = 'race', lazy = True)


class Equides(db.Model):
    id_eq = db.Column(db.Integer, primary_key=True)
    nom_eq = db.Column(db.String(80))
    sexe_eq = db.Column(db.Integer)
    puce_eq = db.Column(db.Numeric)
    sire_eq = db.Column(db.String(10))
    race_eq = db.Column(db.Integer, db.ForeignKey('races_equides.id_race'))

    # On crée une variable qui fait la connexion "back_populates" de la class Races_equides
    race = relationship('Races_equides', back_populates = 'equides')



equides = Equides.query.all()

for equide in equides:
    print(equide.sexe_eq)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/chevaux')
def show_all():
   return render_template('chevaux.html', equides = Equides.query.all() )

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)