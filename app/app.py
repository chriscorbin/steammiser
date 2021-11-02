from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landing.html')


@app.route('/new_pricewatch/')
def new_pricewatch():
    # get data from the sent form 

    # transmit to a aws cloud function

    # redirect to a success screen
    
    pass