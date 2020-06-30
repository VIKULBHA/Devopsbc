from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Finally it ran'
@app.route('/about')
def about():
    return 'this is about page'

