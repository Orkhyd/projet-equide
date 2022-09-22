from sqlalchemy.orm import relationship
from projet_equides import db


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
    
    dep_eq = relationship('Deplacements', back_populates = 'eq_dep', lazy = True)
    
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
    id_eq_dep = db.Column(db.Integer, db.ForeignKey('equides.id_eq'))
     # On crée une variable qui fait la connexion "back_populates" de la class Types_soins
    eq_dep = relationship('Equides', back_populates = 'dep_eq')
    date_depart_dep = db.Column(db.DateTime)
    date_arrive_dep = db.Column(db.DateTime)
    lieu_depart_dep = db.Column(db.String)
    lieu_arrive_dep = db.Column(db.String)
    motif_depart_dep = db.Column(db.String)
    motif_arrive_dep = db.Column(db.String)


    id_transport = db.Column(db.Integer, db.ForeignKey('transports.id_voyage'))
    # On crée une variable qui fait la connexion "back_populates" de la class Types_soins
    transport_dep = relationship('Transports', back_populates = 'dep_transport')

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

class Transports(db.Model):
    id_voyage = db.Column(db.Integer, primary_key=True)
    lieu_desinf_vhl_dep = db.Column(db.String)
    type_de_tranport = db.Column(db.String)
    date_desinf_vhl_dep = db.Column(db.Date)
    # On crée une variable qui fait la connexion "back_populates" de la class Soins_equides
    dep_transport = relationship('Deplacements', back_populates = 'transport_dep', lazy = True)