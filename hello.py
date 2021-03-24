from flask import Flask
myapp = Flask(__name__)

@myapp.route("/")
def hello():
    return "My Flask app, Deployed on my azure app service on linux"