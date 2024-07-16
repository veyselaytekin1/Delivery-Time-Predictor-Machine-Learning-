from flask import Flask             # Import Flask module
from src.logger import logging      # Import custom logging module
from src.exception import CustomException  # Import custom exception class
import os
import sys                      # Import standard os and sys modules

app = Flask(__name__)               # Initialize Flask app


@app.route('/', methods=['GET', 'POST'])  # Define route for root URL
def index():  # Define the function to handle requests to the root URL
    try:
        # Raise an exception
        raise Exception('I am trying exception function but that is wrong')
    except Exception as e:
        # Handle the exception with custom exception class
        ML = CustomException(e, sys)
        logging.info(ML.error_message)  # Log the error message
        logging.info('We are testing our logging file')  # Log a test message

        return "Welcome Veysel"  # Return a welcome message



if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Run the Flask app on port 5001
