# Code-Execution-Engine-Prototype
Super Simple Remote Code Execution Engine Example

### Description:

Simple RCE. Built this primarily to figure out how to use the Docker API. In production would just Node.js for this but Python had better documentation for the Docker API.

- To make this fully secure we would need to containerise the API, as well as add 
- Would also implement proper unit testing for a `verify` endpoint rather than just manual checking (Hence: Prototype)

### Requirements:
- `docker`
- `docker-py`
- `Flask`

```pip install docker``` and install Docker Desktop

```pip install flask```

### Instructions

- Run Docker Desktop
- Run App.py
- POST Request @ `http://127.0.0.1:5000/run_py` with a `.py` file in the body to run the file and return result