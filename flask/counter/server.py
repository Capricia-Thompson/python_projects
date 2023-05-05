from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "password"


@app.route('/')
def render_home():
    if 'counter' in session:
        pass
    else:
        session['counter'] = 0
    return render_template("index.html")


@app.route('/clicked', methods=['POST'])
def add_to_count():
    session['counter'] += 1
    return redirect('/')


@app.route('/reset')
def clear():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
