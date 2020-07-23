from flask import Flask, request
import os
import docker_controller

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "Hello World"


@app.route('/run_py', methods=['POST'])
def run_file():
    f = request.files['File']

    result = docker_controller.run_container(f)

    return result

app.run()