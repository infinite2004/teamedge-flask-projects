from flask import Flask, render_template,request,url_for,redirect
from sense_hat import SenseHat

sense = SenseHat()
  
app = Flask(__name__)

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