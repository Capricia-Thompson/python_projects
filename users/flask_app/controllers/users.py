from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User


@app.route('/')
def go_home():
    return redirect('/users')


@app.route('/users')
def home():
    users = User.get_all()
    print(users)
    return render_template('read_all.html', all_users=users)


@app.route('/new')
def create():
    return render_template('/create.html')


@app.route('/users/<int:user_id>')
def display_user(user_id):
    user = User.get_one(user_id)
    return render_template('/display.html', user=user)


@app.route('/users/edit/<int:user_id>')
def editor(user_id):
    user = User.get_one(user_id)
    return render_template('/editor.html', user=user)


@app.route('/update', methods=['POST'])
def update():
    User.update(request.form)
    user_id = request.form['id']
    return redirect(f'/users/{user_id}')


@app.route('/add', methods=["POST"])
def add_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    user_id = User.save(data)
    return redirect(f'/users/{user_id}')


@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    User.delete(user_id)
    return redirect('/users')
