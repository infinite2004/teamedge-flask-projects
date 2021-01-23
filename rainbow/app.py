from flask import Flask, render_template,json,jsonify,request,current_app as app
from datetime import date
import requests
import os 

app = Flask(__name__)

@app.route('/')
def index():
    return'welcome abdul to your rainbow project'

@app.route('/red')
def red():
    placeholder = 'RED'
    return render_template('red.html',placeholder=placeholder)

@app.route('/orange')
def orange():
    placeholder = 'Orange'
    return render_template('orange.html',placeholder=placeholder)
@app.route('/yellow')
def yellow():
    placeholder = 'Yellow'
    return render_template('yellow.html',placeholder=placeholder)
@app.route('/green')
def green():
    placeholder = 'Green'
    return render_template('green.html',placeholder=placeholder)
@app.route('/blue')
def blue():
    placeholder = 'Blue'
    return render_template('blue.html',placeholder=placeholder)
@app.route('/indigo')
def indigo():
    placeholder = 'indigo'
    return render_template('indigo.html',placeholder=placeholder)
@app.route('/violet')
def violet():
    placeholder = 'VIOLET'
    return render_template('violet.html',placeholder=placeholder)
if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.213')