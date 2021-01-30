from flask import Flask, render_template,json,jsonify,request,current_app as app
from datetime import date
import requests
import os 

app = Flask(__name__)

@app.route('/holidays')
def index():
    

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.213')