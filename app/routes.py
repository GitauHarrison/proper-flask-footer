from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/about-me')
def about_me():
    return render_template('about_me.html')