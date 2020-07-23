# Code-Execution-Engine-Prototype
Super Simple Remote Code Execution Engine Example

### Description:

Simple RCE. Built this primarily to figure out how to use the Docker API. In production would just Node.js for this but Python had better documentation for the Docker API.

- To make this fully secure we would need to containerise the API, as well as add dynamic limitations e.g. using `RestrictedPython`
- Would also implement proper unit testing for a `verify` endpoint rather than just manual checking (Hence: Prototype)

### Requirements:
- `docker`
- `docker-py`
- `Flask`

### Installation 
- ```pip install docker```
- ```pip install flask```
- Install Docker Desktop

### Instructions

- Run Docker Desktop
- BUILD the Docker Image - `docker build pyimage -t pyimage` in the command line
- Run App.py
- POST Request @ `http://127.0.0.1:5000/run_py` with a `.py` file in the body to run the file and return result