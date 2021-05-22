import flask
from flask import Flask
from flask import json
from flask import jsonify, request
import datetime  
import requests
from flask import render_template, redirect, url_for
import os
import sqlite3
from time import sleep
from sense_hat import SenseHat
sense = SenseHat()


app = Flask(__name__)

# @app.route('/success/ <name> / <r> / <g> / <b>')
# def success(name,r, g, b):
#    sense.show_message(name, text_colour=[int(r),int(g),int(b)]) 
#    return '<a href = "/all">All messages</a>'

# @app.route('/all')
# def all():
#    conn = sqlite3.connect('./static/data/data.db')
#    curs = conn.cursor()
#    messages = []
#    rows = curs.execute("SELECT * from messages")
#    for row in rows:
#       message = {'message' : row[0],'r' : row[1] ,'g' : row[2] ,'b' : row[3]}
#       messages.append(message)
#    conn.close()
#    return render_template('all.html', messages = messages)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      reminder = request.form['r']


      conn = sqlite3.connect('./static/data/todo.db')
      curs = conn.cursor()
      curs.execute('INSERT INTO reminders (reminder) VALUES(?)', (reminder,))
      messages = []
      rows = curs.execute("SELECT * from reminders")
      for row in rows:
         message = {'reminder' : row[0],'id' : row[1]}
         messages.append(message)
      conn.commit()
      conn.close()

      return render_template('index.html', messages = messages)
   else:

      reminder = request.args.get('r')


      conn = sqlite3.connect('./static/data/todo.db')
      curs = conn.cursor()
      curs.execute('INSERT INTO reminders (reminder) VALUES(?)', (reminder,))
      messages = []
      rows = curs.execute("SELECT * from reminders")
      for row in rows:
         message = {'reminder' : row[0],'id' : row[1]}
         messages.append(message)
      conn.commit()
      conn.close()


      return render_template('index.html', messages = messages)

@app.route('/', methods=['GET'])
def submit():
   conn = sqlite3.connect('./static/data/todo.db')
   curs = conn.cursor()
   messages = []
   rows = curs.execute("SELECT * from reminders")
   for row in rows:
      message = {'reminder' : row[0],'id' : row[1]}
      messages.append(message)
   conn.close()
   return render_template('index.html', messages = messages)

@app.route('/buttonPressed/<btn>')
def delete_task(btn):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    conn = sqlite3.connect('./static/data/todo.db')
    sql = 'DELETE FROM reminders WHERE id=?'
    curs = conn.cursor()
    curs.execute(sql, (btn,))
    messages = []
    rows = curs.execute("SELECT * from reminders")
    for row in rows:
      message = {'reminder' : row[0],'id' : row[1]}
      messages.append(message)

    conn.commit()
    conn.close()
    return render_template('index.html', messages = messages)

@app.route('/deleteAll')
def delete_all():
    conn = sqlite3.connect('./static/data/todo.db')
    sql = 'DELETE FROM reminders'
    curs = conn.cursor()
    curs.execute(sql)
    messages = []
    rows = curs.execute("SELECT * from reminders")
    for row in rows:
      message = {'reminder' : row[0],'id' : row[1]}
      messages.append(message)
    conn.commit()
    conn.close()
    return render_template('index.html', messages = messages)






if __name__ == '__main__':
    app.run(debug = True, host='127.0.0.1') 