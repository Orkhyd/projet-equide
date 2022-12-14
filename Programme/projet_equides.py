from flask import Flask, Blueprint ,request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://team:*Azerty01*@localhost/projet_equides'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATION' ] = True
db = SQLAlchemy(app)


from .views import chevaux
app.register_blueprint(chevaux)

from .views import proprietaires
app.register_blueprint(proprietaires)