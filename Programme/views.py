from flask import Flask, request, flash, url_for, redirect, render_template
from flask import Blueprint
from flask import current_app as app
from projet_equides import app
from models import Equides, Races_equides, Soins_equides, Deplacements, Evenements, Types_soins, Soins, Proprietaires, Transports, Prestataires,  Centres_detention
from projet_equides import db
from flask_login import current_user, login_required, logout_user, login_user
from flask_login import LoginManager
from forms import LoginForm
from models import User

a=User("emmanuel")
a.set_password("Azerty01")

chevaux = Blueprint('chevaux', __name__)
proprietaires = Blueprint('proprietaires', __name__)
transports = Blueprint('transports', __name__)
races = Blueprint('races', __name__)
prestataires = Blueprint('prestataires', __name__)
centres_detention = Blueprint('centres_detention', __name__)
#Déclare le blueprint login
login_bp = Blueprint('login', __name__,template_folder='templates',static_folder='static',url_prefix='/')

#Login manager pour l'identifiant
login = LoginManager()
login.init_app(app)

chevaux = Blueprint('chevaux', __name__, template_folder='templates', static_folder='static', url_prefix='/equide')
proprietaires = Blueprint('proprietaires', __name__, template_folder='templates', static_folder='static', url_prefix='/proprietaire')

ENDPOINT = []

@chevaux.route('/equide', methods=['GET', 'POST'])
@login_required
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
@login_required
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
         add_soin = Soins_equides(
            id_eq_soin = equide_id, 
            id_type_soin = request.form['type_nv_soin'], 
            id_soin = request.form['nom_soin'], 
            id_prestataire = request.form['prestataire'], 
            ref_soin = request.form['ref_soin'],
            com_soin = request.form['com_soin'])
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
@login_required
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

@transports.route('/transports', methods=['GET', 'POST'])
@login_required
def infos_transports():
   infos_transports = Transports.query.all()
   infos_deplacements = Deplacements.query.all()
   if request.method == 'GET':
      return render_template('transports.html', transports = infos_transports, deplacements = infos_deplacements)
   if request.method == 'POST':
      if 'form_add_transport' in request.form:
         add_transport = Transports()
         db.session.add(add_transport)
         db.session.commit() 
      return redirect(url_for('transports.infos_transports'))

@races.route('/races', methods=['GET', 'POST'])
@login_required
def infos_races():
   infos_races = Races_equides.query.all()
   if request.method == 'GET':
      return render_template('races.html', races = infos_races)

   if request.method == 'POST':
      if 'form_add_race' in request.form:
         add_race = Races_equides()
         db.session.add(addrace)
         db.session.commit() 
      return redirect(url_for('races.infos_races'))

@prestataires.route('/prestataires', methods=['GET', 'POST'])
@login_required
def infos_prestataires():
   infos_prestataires = Prestataires.query.all()
   if request.method == 'GET':
      return render_template('prestataires.html', prestataires = infos_prestataires)

   if request.method == 'POST':
      if 'form_add_race' in request.form:
         add_prestataire = Prestataires()
         db.session.add(add_prestataire)
         db.session.commit() 
      return redirect(url_for('prestataires.infos_prestataires'))

@centres_detention.route('/centres_detention', methods=['GET', 'POST'])
@login_required
def infos_centres_detention():
   infos_centres_detention = Centres_detention.query.all()
   if request.method == 'GET':
      return render_template('centres_detention.html', centres = infos_centres_detention)
#Besoin de cette fonction ne pas toucher pour le login
@login.user_loader
def load_user(id):
   return User.query.filter_by(id=id).first()


#Page introuvable redirige vers la page equide si connecter
@app.errorhandler(500)
@login_required
def page_not_found_2(exception):
   print(exception)
   return redirect(url_for('chevaux.infos_chevaux'))

@app.errorhandler(404)
@login_required
def page_not_found(exception):
   print(exception)
   return redirect(url_for('chevaux.infos_chevaux'))


#Si non connecter redirige vers la page de login
@login.unauthorized_handler
def login_needed():
   ENDPOINT.append(request.endpoint)
   return redirect(url_for('login.login'))

#Lien pour se logout
@login_bp.route('/logout', methods=['GET'])
@login_required
def logout():
   logout_user()
   return redirect(url_for('login.login'))

#page de login
@login_bp.route('/', methods=['GET', 'POST'])
def login():
   
   
   if request.method == 'POST':

      r = request.form.to_dict()
      form = LoginForm(r)
      user = User(form.login)

      #check password hash
      if user.check_password(r['password']):
         
         
         login_user(user, remember=True)

         ENDPOINT.append(request.endpoint)
         return redirect(url_for('chevaux.infos_chevaux'))

      else:
         ENDPOINT.append(request.endpoint)
         return render_template('login.html', title='Se connecter', login_err=True, login_needed=False)
   
   else:
      
      if ENDPOINT != []:
         if not(current_user.is_authenticated) and 'login.login' != ENDPOINT[-1]:
            ENDPOINT.append(request.endpoint)
            return render_template('login.html', title='Se connecter', login_err=False, login_needed=True)
      ENDPOINT.append(request.endpoint)
      return render_template('login.html', title='Se connecter', login_err=False, login_needed=False)


if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)

