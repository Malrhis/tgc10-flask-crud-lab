from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)
# database variable here is global
database = {}
with open('customers.json') as fp:
    database = json.load(fp)
print(database)


@app.route('/')
def home():
    return render_template('home.template.html')


@app.route('/customers')
def show_customers():
    return render_template('customers.template.html', customers=database)


@app.route('customers/add')
def show_add_customers():
    return render_template('add_customer.template.html')


@app.route('/customers/add')
def process_add_customer():
    print(request.form)
    return "data received"

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
