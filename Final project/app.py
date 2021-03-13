from flask import Flask, render_template 
  
app = Flask(__name__)

@app.route('/')
def index():
    return  render_template('post.html')


if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.213')