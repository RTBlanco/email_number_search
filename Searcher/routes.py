from Searcher import app
from Searcher.search import scraper
from flask import render_template, send_from_directory, url_for, request, redirect

@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
    url = request.form.get('url')
    phone, email = scraper(str(url))
    if len(phone) > 0:
        for number in phone:
            print(number)
    else:
        print('Nothing')

    if len(email) > 0: 
        for mail in email:
            print(mail)
    else:
        print('Nothing')
    return render_template('home.html')