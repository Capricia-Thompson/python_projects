from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "password"


@app.route('/')
def render_home():
    return render_template("form.html")


@app.route('/process', methods=['POST'])
def submit():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/display')


@app.route('/result')
def display():
    return render_template('display.html')


if __name__ == "__main__":
    app.run(debug=True)
