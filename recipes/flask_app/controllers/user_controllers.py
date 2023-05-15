from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user_models import User
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['fname'],
        'last_name': request.form['lname'],
        'email': request.form['email'],
        'password': pw_hash
    }
    if User.get_user_by_email(request.form):
        flash("Email already in use.")
        return redirect('/')
    if not User.valid_user(request.form):
        return redirect('/')
    new_user = User.create_user(data)
    session['user_id'] = new_user
    session['user_name'] = request.form['fname']
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
    session['user_name'] = user.first_name
    return redirect(f'/user/{user.id}')


@app.route('/logout')
def logout():
    session.clear()
    print(session)
    return redirect('/')
