from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://team:*Azerty01*@localhost/projet_equides'
db = SQLAlchemy(app)
db.create_all()

class Equides(db.Model):
    id_eq = db.Column(db.Integer, primary_key=True)
    nom_eq = db.Column(db.String(80), unique=True, nullable=False)
    race_eq = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, nom_eq, race_eq):
        self.nom_eq = nom_eq
        self.race_eq = race_eq

equides = Equides.query.all()

for equide in equides:

   print(equide.race_eq.nom_race)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/chevaux')
def show_all():
   return render_template('chevaux.html', equides = Equides.query.all() )

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)