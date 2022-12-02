import csv
import requests
from faker import Faker
from http import HTTPStatus
from flask import Flask, request, Response
from currency_symbols import CurrencySymbols
from webargs.flaskparser import use_kwargs
from webargs import fields, validate


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/students")
@use_kwargs(
    {
        'amount': fields.Int(
            missing=13,
            validate=[validate.Range(min=1, max=1000)]
        )
    },
    location='query'
)
def generate_students(amount):

    student_info = Faker("uk")

    students_data = []
    for i in range(amount):
        student_list = [student_info.first_name(),
                        student_info.last_name(),
                        student_info.email(),
                        student_info.password(),
                        student_info.date_of_birth().isoformat()
                        ]

        students_data.append(student_list)

    with open('students.csv', 'w') as f:
        data = csv.writer(f)
        data.writerow(students_data)

    return '<br>'.join(str(students_data) for students_data in students_data)


@app.route("/bitcoin")
def get_bitcoin_value():
    currency = request.args.get('currency', 'USD')
    coefficient_count = request.args.get('count', 1)
    coefficient_count = int(coefficient_count)
    url = f'https://bitpay.com/api/rates/{currency}'
    value = requests.get(url, {})

    if value.status_code != HTTPStatus.OK:

        return Response('ERROR: Try again', status=value.status_code)

    value = value.json()

    return f'Bitcoin {CurrencySymbols.get_symbol("BTC")} ' \
           f' worths {value["rate"] * coefficient_count} ' \
           f'{CurrencySymbols.get_symbol(currency)} '


app.run(port=5000, debug=True)