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
    

@app.route('/About')
def about():
    return render_template('about.html')

@app.route('/Services')
def services():
    return render_template('services.html')

@app.route('/Contact')
def contact():
    return render_template('contact.html')