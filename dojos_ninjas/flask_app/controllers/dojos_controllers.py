from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo


@app.route('/')
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('index.html', dojos=dojos)


@app.route('/dojo/<int:dojo_id>')
def dojo_details(dojo_id):
    data = {'id': dojo_id}
    one_dojo = Dojo.get_ninjas_from_dojo(data)
    return render_template('dojo.html', one_dojo=one_dojo)


@app.route('/add_dojo', methods=['POST'])
def add_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.create(data)
    return redirect('/')
