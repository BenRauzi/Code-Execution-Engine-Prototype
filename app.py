from flask import Flask, request
import os
import docker_controller

import unittest

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "Hello World"


@app.route('/run_py', methods=['POST'])
def run_py():
    f = request.files['File']

    result = docker_controller.run_container(f) #run code and return result

    return result

@app.route('/verify_py', methods=['POST']) #write a function that returns "Hello World"
def verify_py():
    f = request.files['File']

    result = docker_controller.run_container(f)
    result = result.decode("utf-8").strip()

    if result == "Hello World": #we would load this dynamically and use unit testing rather than plain testing
        return str(result).strip() + "\n_________________________________________\n" + "1 Test Passed"
    else:
        return str(result).strip() + "\n_________________________________________\n" + "1 Test Failed"

app.run()