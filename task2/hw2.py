import csv
import pandas
import random
import string
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/password")
def generate_password():
    symbols = string.ascii_letters + string.digits + string.punctuation
    element = random.randrange(10, 20)
    '''password'''
    password = ''.join(random.choices(symbols, k=element))
    print(password)
    return password
generate_password()


@app.route("/averege")
def calculate_average():
    with open('hw2.csv') as f:
        reader = csv.reader(f)
        head = next(reader)
        '''get average height and get average weight'''
        hights = []
        counter = 0
        weights = []
        counterw = 1
        for i in reader:
            hight = (i[1])
            weight = (i[2])
            hights.append(float(hight))
            weights.append(float(weight))
            counter += 1
            counterw += 1

    return f"<p>Average values of hight are {((sum(hights)))/(counter)} iches <br>\n" \
           f" Average values of weight are {((sum(weights)))/(counterw)} pounds</p>"
print(calculate_average())


app.run(port=5001)