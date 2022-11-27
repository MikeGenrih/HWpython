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
    count_of_symbols_password = random.randrange(10, 20)
    password = ''.join(random.choices(symbols, k=count_of_symbols_password ))

    return password



@app.route("/averege")
def calculate_average():
    with open('hw2.csv') as f:
        reader = csv.reader(f)
        head = next(reader)
        list_hights = []
        counter_element_high = 0
        list_weights = []
        counter_element_weight = 0
        for row in reader:
            hight = (row[1])
            weight = (row[2])
            list_hights.append(float(hight))
            list_weights.append(float(weight))
            counter_element_high += 1
            counter_element_weight += 1

    return f"<p>Average values of hight are {((sum(list_hights)))/(counter_element_high)} iches <br>\n" \
           f" Average values of weight are {((sum(list_weights)))/(counter_element_weight)} pounds</p>"



app.run(port=5001)