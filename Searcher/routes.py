from Searcher import app
from Searcher.scraper import Scraper
from flask import render_template, send_from_directory, url_for, request, redirect

@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        info = Scraper(str(url))
        if len(info.numbers()) > 0 or len(info.emails()) > 0:
            return render_template('home.html', phones=info.numbers(), emails=info.emails(), data=True)
        else:            
            return render_template('home.html',data=False, url=url)
    return render_template('home.html', data=None)
    

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        # TODO:send you self an email 
        print(request.form.get('name'))
        print(request.form.get('email'))
        print(request.form.get('subject'))
        print(request.form.get('message'))
    return render_template('contact.html')