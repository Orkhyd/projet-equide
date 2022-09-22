from flask import Flask, request, flash, url_for, redirect, render_template
from flask import Blueprint
from flask import current_app as app
from projet_equides import app
from models import Equides, Races_equides, Soins_equides, Deplacements, Evenements, Types_soins, Soins, Proprietaires, Prestataires 
from projet_equides import db

chevaux = Blueprint('chevaux', __name__)
proprietaires = Blueprint('proprietaires', __name__)

@chevaux.route('/equide', methods=['GET', 'POST'])
def infos_chevaux():
   races_equides = Races_equides.query.all()
   infos_equides = Equides.query.all()
   if request.method == 'GET':
      return render_template('chevaux.html', equides = infos_equides, races = races_equides)

   if request.method == 'POST':
      if 'form_add_equide' in request.form:
         add_equide = Equides(
            nom_eq = request.form['nom_eq'], 
            race_eq = request.form['race_eq'], 
            sexe_eq = request.form['sexe_eq'],
            puce_eq = request.form['puce_eq'],
            sire_eq = request.form['sire_eq'],
            pere_eq = request.form['pere_eq'],
            mere_eq = request.form['mere_eq'],
            pere_mere_eq = request.form['pere_mere_eq'],
            num_stu_book_eq = request.form['num_stu_book_eq'],
            )
         db.session.add(add_equide)
      db.session.commit() 
      return redirect(url_for('chevaux.infos_chevaux'))
   
@chevaux.route('/equide/<equide_id>', methods=['GET', 'POST'])
def fiche_equide(equide_id):

   if request.method == 'GET':
      equide_infos = Equides.query.filter_by(id_eq = equide_id).first()
      equide_deplacements = Deplacements.query.filter_by(id_eq_dep = equide_id)
      equide_evenements = Evenements.query.filter_by(id_eq_even = equide_id)
      races_equides = Races_equides.query.all()
      soins_equides = Soins_equides.query.filter_by(id_eq_soin = equide_id)
      types_de_soins = Types_soins.query.all()
      soins = Soins.query.all()
      prestataires_soins = Prestataires.query.all()

      return render_template('fiche_equide.html', equide = equide_infos, races = races_equides , soins = soins_equides, deplacements = equide_deplacements, evenements = equide_evenements, types_soins = types_de_soins, nv_soins =soins, prestataires = prestataires_soins)

   if request.method == 'POST':
      
      if 'form_add_soin' in request.form:
         add_soin = Soins_equides(id_eq_soin = equide_id, id_type_soin = request.form['type_nv_soin'], id_soin = request.form['nom_soin'], id_prestataire = request.form['prestataire'], ref_soin = request.form['ref_soin'],com_soin = request.form['com_soin'])
         db.session.add(add_soin)
      
      if 'form_add_deplacement' in request.form:
         add_deplacement = Deplacements(
            id_eq_dep = equide_id, 
            date_depart_dep = request.form['date_depart_dep'], 
            lieu_depart_dep = request.form['lieu_depart_dep'], 
            motif_depart_dep = request.form['motif_depart_dep'], 
            lieu_arrive_dep = request.form['lieu_arrive_dep'],
            date_arrive_dep = request.form['date_arrive_dep'],
            motif_arrive_dep = request.form['motif_arrive_dep'])
            
         db.session.add(add_deplacement)

      if 'form_add_evenement' in request.form:
         add_evenement = Evenements(
            id_eq_even = equide_id, 
            date_even = request.form['date_even'],
            titre_even = request.form['titre_even'],
            detail_even = request.form['detail_even'])

         db.session.add(add_evenement)

      db.session.commit() 
      return redirect(url_for('chevaux.fiche_equide', equide_id= equide_id))


@proprietaires.route('/proprietaires', methods=['GET', 'POST'])
def infos_proprietaires():
   infos_proprietaires = Proprietaires.query.all()
   if request.method == 'GET':
      return render_template('proprietaires.html', proprietaires = infos_proprietaires)

   if request.method == 'POST':
      if 'form_add_prop' in request.form:
         add_proprietaire = Proprietaires(
            nom_prop = request.form['nom_prop'],
            prenom_prop = request.form['prenom_prop'],
            siret_prop = request.form['siret_prop'],
            sire_prop = request.form['sire_prop'])

         db.session.add(add_proprietaire)

      db.session.commit() 
      return redirect(url_for('proprietaires.infos_proprietaires'))

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)

