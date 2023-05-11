from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


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


@app.route('/new_ninja')
def ninja_form():
    dojos = Dojo.get_all()
    return render_template('ninja.html', dojos=dojos)
