# Dependencies
from flask import Flask
app = Flask(__name__)


# The source
from .scr.help import print_help


# The app
@app.route('/')
def hello_world():
    return print_help()