from sqlalchemy.orm import relationship
from projet_equides import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Races_equides(db.Model):
    id_race = db.Column(db.Integer, primary_key=True)
    nom_race = db.Column(db.String)
    # On crée une variable qui fait la connexion "back_populates" de la class Equides
    equides_races = relationship('Equides', back_populates = 'race', lazy = True)

class Soins(db.Model):
    id_soin = db.Column(db.Integer, primary_key=True)
    nom_soin = db.Column(db.String)
    # On crée une variable qui fait la connexion "back_populates" de la class Soins_equides
    soin = relationship('Soins_equides', back_populates = 'soin_eq', lazy = True)


class Prestataires(db.Model):
    id_presta = db.Column(db.Integer, primary_key=True)
    nom_presta = db.Column(db.String)
    # On crée une variable qui fait la connexion "back_populates" de la class Soins_equides
    presta_soin = relationship('Soins_equides', back_populates = 'prestataire_soin_eq', lazy = True)

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
    pere_eq = db.Column(db.String)
    mere_eq = db.Column(db.String)
    pere_mere_eq = db.Column(db.String)
    num_stu_book_eq = db.Column(db.String)
    
    
    race_eq = db.Column(db.Integer, db.ForeignKey('races_equides.id_race'))
    # On crée une variable qui fait la connexion "back_populates" de la class Races_equides
    race = relationship('Races_equides', back_populates = 'equides_races')


class Soins_equides(db.Model):

    id_soin_eq = db.Column(db.Integer, primary_key=True)
    id_eq_soin = db.Column(db.Integer)
    date_soin = db.Column(db.DateTime)
    id_soin = db.Column(db.Integer, db.ForeignKey('soins.id_soin'))
    # On crée une variable qui fait la connexion "back_populates" de la class Soins
    soin_eq = relationship('Soins', back_populates = 'soin')
    # On crée une variable qui fait la connexion "back_populates" de la class Types_soins
    id_type_soin = db.Column(db.Integer, db.ForeignKey('types_soins.id_type_soin'))
    type_soin_eq = relationship('Types_soins', back_populates = 'type_soin')
    id_prestataire = db.Column(db.Integer, db.ForeignKey('prestataires.id_presta'))
    # On crée une variable qui fait la connexion "back_populates" de la class Types_soins
    prestataire_soin_eq = relationship('Prestataires', back_populates = 'presta_soin')
    ref_soin = db.Column(db.String)
    com_soin = db.Column(db.String)

class Deplacements(db.Model):

    id_dep = db.Column(db.Integer, primary_key=True)
    id_eq_dep = db.Column(db.Integer)
    date_depart_dep = db.Column(db.DateTime)
    date_arrive_dep = db.Column(db.DateTime)
    lieu_depart_dep = db.Column(db.String)
    lieu_arrive_dep = db.Column(db.String)
    motif_depart_dep = db.Column(db.String)
    motif_arrive_dep = db.Column(db.String)

class Evenements(db.Model):
    id_even = db.Column(db.Integer, primary_key=True)
    id_eq_even = db.Column(db.Integer)
    date_even = db.Column(db.Date)
    titre_even = db.Column(db.String)
    detail_even = db.Column(db.Text)

class Proprietaires(db.Model):
    id_prop = db.Column(db.Integer, primary_key=True)
    nom_prop = db.Column(db.String)
    prenom_prop = db.Column(db.String)
    sire_prop = db.Column(db.String)
    siret_prop = db.Column(db.String)


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login_user = db.Column(db.String)
    code_user = db.Column(db.String)
    id_centre_user = db.Column(db.Integer)
    
    
    def __init__(self, login):

        
        self.login_user = login
        self.id = self.get_id()
        query = self.query.filter_by(login_user=self.login_user).first()
        if query is not None:
            self.code_user = query.code_user
        else:
            self.code_user = None

    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def set_password(self, password):
        if self.is_authenticated:
            user = self.query.filter_by(login_user=self.login_user).first()
            user.code_user = generate_password_hash(password)
            db.session.commit()
        else:
            raise Exception("Must be connected to change password")

    def check_password(self, password):
        if self.code_user is None:
            return False
        else:
            return check_password_hash(self.code_user, password)

    def get_id(self):
        try:
            return self.query.filter_by(login_user=self.login_user).first().id
        except:
            return None


