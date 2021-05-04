#!/usr/bin/python3

from flask import Flask
from datetime import datetime
from waitress import serve
from paste.translogger import TransLogger
import logging

app = Flask(__name__)

logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)


@app.route('/')
def home():
    return "Welcome!"


@app.route('/now')
def now():
    return "{0}".format(datetime.utcnow())


@app.route('/ping')
def ping():
    return "pong"


if __name__ == '__main__':
    # app.run(debug=True)
    serve(TransLogger(app, setup_console_handler=True), port=8000)
