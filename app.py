from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World!"

@app.route('/test')
def test():
  return "Test!"

@app.route('/dojo')
def dojo():
  return "Dojo!"

#  this line added in feature-1
