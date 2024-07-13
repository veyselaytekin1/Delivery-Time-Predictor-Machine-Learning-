from flask import Flask
from src.logger import logging
from src.exception import CustomException
import os, sys

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])


def index():

    try:
        raise Exception('I am trying exception function')
    except Exception as e:

        a_variable = CustomException(e, sys) # we gave thise name in the original function
        logging.info('We are testing our logging file')

        return "Welcome Veysel"

if __name__== '__main__':
    app.run(debug=True, port=5000) # 5000