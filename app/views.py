from app import app,custom_email_sender
from flask import render_template, redirect


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/Send')
def send_email():
    custom_email_sender.send_email(email='artkryvonis@gmail.com',message_string='Hello')
    return render_template('index.html',sended=True)
