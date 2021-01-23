from flask import Flask, render_template, request, redirect, url_for
import os
import json
import random

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


@app.route('/customers/add')
def show_add_customers():
    return render_template('add_customer.template.html')


@app.route('/customers/add', methods=["POST"])
def process_add_customer():
    print(request.form)
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    can_send_marketing_materials = request.form.get('can_send')
    # generate a random number as our customer_id
    # but usually, we will get the database to generate for us
    customer_id = random.randint(1, 1000000) + 5

    new_customer = {}
    new_customer['id'] = customer_id
    new_customer['first_name'] = first_name
    new_customer['last_name'] = last_name
    new_customer['email'] = email
    new_customer['send_marketing_material'] = can_send_marketing_materials == "on"

    database.append(new_customer)

    # save the entire list into the json file. write the file
    with open('customers.json', 'w') as fp:
        json.dump(database, fp)

    return "data received"


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
