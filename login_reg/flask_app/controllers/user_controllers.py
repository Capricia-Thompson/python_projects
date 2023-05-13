from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.users_models import User
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)


@app.route('/')
def render_home():
    return render_template('index.html')


@app.route('/user/<int:user_id>')
def display_user(user_id):
    if 'user_id' not in session:
        return redirect('/')
    if session['user_id'] != user_id:
        return redirect('/')
    one_user = User.get_user_by_id(user_id)
    return render_template('dashboard.html', one_user=one_user)


@app.route('/register', methods=['POST'])
def register():
    if not User.valid_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'birthday': request.form['dob'],
        'password': pw_hash
    }
    new_user = User.create_user(data)
    session['user_id'] = new_user
    return redirect(f'/user/{new_user}')


@app.route('/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user = User.get_user_by_email(data)
    if not user:
        flash("Invalid Email/Password")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user.id
    return redirect(f'/user/{user.id}')


@app.route('/logout')
def logout():
    session.clear()
    print(session)
    return redirect('/')
