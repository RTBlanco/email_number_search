from Searcher import app
from flask import render_template, send_from_directory, url_for, request, redirect

@app.route('/')
def home():
    return "<h1> this is a test</h1>"