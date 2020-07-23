import os

uuid = os.environ['id']

file = open(f"{uuid}.py", "r").read()
exec(file) #INCREDIBLY simple execution of file. This needs to be improved