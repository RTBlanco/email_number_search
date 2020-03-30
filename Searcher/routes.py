from Searcher import app
from flask import render_template, send_from_directory, url_for, request, redirect

@app.route('/')
def home():
    return render_template('home.html')