import os

code = os.environ['id']

print(code)
exec(open(f'b.py').read())