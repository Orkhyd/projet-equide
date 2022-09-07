from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/chevaux', methods=('GET', 'POST'))
def create():
    return render_template('chevaux.html')
