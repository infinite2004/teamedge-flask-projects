from flask import Flask, render_template,request,url_for,redirect
from sense_hat import SenseHat 
import sqlite3

sense = SenseHat()
  
app = Flask(__name__)

r = (255, 0, 0 )# RED color, stored in an another data structure called a tuple.
k = (0, 0, 0) # black means zero amounts of red, green and blue
w =(255,255,255)
g =(0,255,0)
y =(0,0,225)
n =(255,128,128)
o =(255,128,0)


rmon1 =[ 
o, y, y, y, y, y, y, o,
o, o, n, y, y, n, o, o,
y, k, k, y, y, w, k, y,
y, w, k, y, y, k, k, y,
y, y, y, k, k, y, y, y,
n, n, n, y, y, n, n, n,
n, n, n, y, y, n, n, n,
n, n, n, y, y, n, n, n,
]   

sense.set_pixels(rmon1)

@app.route('/success/<name>')
def success(name):
    sense.show_message(name)
    #return 'welcome %s' % name
    return '<a href = "/all">All messages</a>'

@app.route('/all')
def all():
    #connect to DB
    conn = sqlite3.connect('./static/data/senseDisplay.db')
    curs = conn.cursor()
    users = []
    rows = curs.execute("SELECT * from users")
    for row in rows:
        name = {'name': row[0]}
        users.append(name)
    conn.close()
    return render_template('all.html', users = users)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        # name = request.form['name']
    
        conn = sqlite3.connect('./static/data/senseDisplay.db') 
        curs = conn.cursor()
        curs.execute('INSERT INTO users (name) VALUES((?))',(user,))
        conn.commit()
        conn.close()

        return redirect(url_for('success',name = user))
       
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))
       
@app.route('/', methods=['GET'])
def submit():
    return  render_template('post.html')

   
    
   

 



if __name__ == '__main__':
    app.run(debug=True,port=5000,host='127.0.0.1')