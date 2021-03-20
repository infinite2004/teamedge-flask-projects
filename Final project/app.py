from flask import Flask, render_template,request,url_for,redirect
from sense_hat import SenseHat

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
    return 'welcome %s' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))

@app.route('/', methods=['GET'])
def submit():
    return  render_template('post.html')

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.213')