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

class Soins(db.Model):
    id_soin = db.Column(db.Integer, primary_key=True)
    nom_soin = db.Column(db.String)
    # On crée une variable qui fait la connexion "back_populates" de la class Soins_equides
    soin = relationship('Soins_equides', back_populates = 'soin_eq', lazy = True)

class Types_soins(db.Model):
    id_type_soin = db.Column(db.Integer, primary_key=True)
    nom_type_soin = db.Column(db.String)
    # On crée une variable qui fait la connexion "back_populates" de la class Soins_equides
    type_soin = relationship('Soins_equides', back_populates = 'type_soin_eq', lazy = True)


class Equides(db.Model):
    id_eq = db.Column(db.Integer, primary_key=True)
    nom_eq = db.Column(db.String(80))
    sexe_eq = db.Column(db.Integer)
    puce_eq = db.Column(db.Numeric)
    sire_eq = db.Column(db.String(10))
    race_eq = db.Column(db.Integer, db.ForeignKey('races_equides.id_race'))
    # On crée une variable qui fait la connexion "back_populates" de la class Races_equides
    race = relationship('Races_equides', back_populates = 'equides')


class Soins_equides(db.Model):

    id_soin_eq = db.Column(db.Integer, primary_key=True)
    id_eq_soin = db.Column(db.Integer)
    id_soin = db.Column(db.Integer, db.ForeignKey('soins.id_soin'))
    # On crée une variable qui fait la connexion "back_populates" de la class Soins
    soin_eq = relationship('Soins', back_populates = 'soin')
    # On crée une variable qui fait la connexion "back_populates" de la class Types_soins
    id_type_soin = db.Column(db.Integer, db.ForeignKey('types_soins.id_type_soin'))
    type_soin_eq = relationship('Types_soins', back_populates = 'type_soin')
    # On crée une variable qui fait la connexion "back_populates" de la class Types_soins
    #prestataire_soin_eq = relationship('Prestaires', back_populates = 'presta_soin')
    ref_soin = db.Column(db.String)


@app.route('/chevaux')
def CHEVAUX():
   return render_template('chevaux.html', equides = Equides.query.all())

@app.route('/equide/<equide_id>', methods=['GET', 'POST'])
def fiche_equide(equide_id):
    return render_template('fiche_equide.html', equide = Equides.query.filter_by(id_eq = equide_id).first(), races = Races_equides.query.all(), soins = Soins_equides.query.all())

class Users(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    login_user = db.Column(db.String(20))
    code_user = db.Column(db.String(64))


# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin' :
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('CHEVAUX'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)
