from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("getstarted.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/dashboard/savelistname')
def savelistname():
    return render_template('savelistname.html')

@app.route('/dashboard/savelistname/additems')
def additems():
    return render_template('additems.html')