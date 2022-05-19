import os

for file in os.listdir('./txt'):
    with open(f'./txt/{file}', 'r') as f:
        print(f.read())