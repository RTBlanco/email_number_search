import smtplib, ssl
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
        user_email = request.form.get('email')
        message = f"Subject:{request.form.get('subject')} \n\nName: {request.form.get('name')}\nEmail: {request.form.get('email')}\nMessage: {request.form.get('message')}" 

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', port=465, context=context) as server:
            server.login('emailphonesearch@gmail.com', 'testtest1Q')
            server.sendmail(user_email,'emailphonesearch@gmail.com' , message)

    return render_template('contact.html')