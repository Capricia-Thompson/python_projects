from flask import Flask, render_template, redirect, request

from user import User

app = Flask(__name__)


@app.route('/')
def home():
    users = User.get_all()
    print(users)
    return render_template('read_all.html', all_users=users)


@app.route('/create')
def create():
    return render_template('/create.html')


@app.route('/add', methods=["POST"])
def add_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
