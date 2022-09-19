from flask import Flask, request, flash, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')