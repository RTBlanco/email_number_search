from Searcher import app
from Searcher.search import scraper
from flask import render_template, send_from_directory, url_for, request, redirect

@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        phone, email = scraper(str(url))
        if len(phone) > 0 or len(email) > 0:
            return render_template('home.html', phones=phone, emails=email, data=True)
        else:            
            return render_template('home.html',data=False, url=url)
    return render_template('home.html', data=None)