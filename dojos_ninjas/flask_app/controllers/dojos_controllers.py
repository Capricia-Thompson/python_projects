from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('index.html', dojos=dojos)


@app.route('/new_ninja')
def ninja_form():
    dojos = Dojo.get_all()
    return render_template('ninja.html', dojos=dojos)


@app.route('/dojo/<int:dojo_id>')
def dojo_details(dojo_id):
    dojo = Dojo.get_one(dojo_id)
    ninjas = Ninja.get_all_dojo_ninjas(dojo_id)
    print(ninjas)
    return render_template('dojo.html', ninjas=ninjas, dojo=dojo)


@app.route('/add_ninja', methods=['POST'])
def add_ninja():
    data = {
        'dojo_id': request.form['dojo'],
        'first_name': request.form['fname'],
        'last_name': request.form['lname'],
        'age': request.form['age']
    }
    Ninja.create(data)
    dojo_id = data['dojo_id']
    return redirect(f'/dojo/{dojo_id}')


@app.route('/add_dojo', methods=['POST'])
def add_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.create(data)
    return redirect('/')
