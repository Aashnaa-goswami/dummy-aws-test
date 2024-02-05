from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World!"

@app.route('/dojo')
def dojo():
  return "Dojo!"

#  this line added in feature-1
