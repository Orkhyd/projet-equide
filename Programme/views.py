from flask import Flask, request, flash, url_for, redirect, render_template
from flask import Blueprint
from flask import current_app as app
from todolist import app
from models import Equides, Races_equides, Soins_equides, Deplacements, Evenements, Types_soins, Soins, Prestataires
from todolist import db

chevaux = Blueprint('chevaux', __name__)

@chevaux.route('/equide')
def infos_chevaux():
   infos_equides = Equides.query.all()
   return render_template('chevaux.html', equides = infos_equides)

@chevaux.route('/equide/<equide_id>', methods=['GET', 'POST'])
def fiche_equide(equide_id):

    equide_infos = Equides.query.filter_by(id_eq = equide_id).first()
    equide_deplacements = Deplacements.query.filter_by(id_eq_dep = equide_id)
    equide_evenements = Evenements.query.filter_by(id_eq_even = equide_id)
    races_equides = Races_equides.query.all()
    soins_equides = Soins_equides.query.filter_by(id_eq_soin = equide_id)
    types_de_soins = Types_soins.query.all()
    soins = Soins.query.all()
    prestataires_soins = Prestataires.query.all()

    return render_template('fiche_equide.html', equide = equide_infos, races = races_equides , soins = soins_equides, deplacements = equide_deplacements, evenements = equide_evenements, types_soins = types_de_soins, nv_soins =soins, prestataires = prestataires_soins)

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)

