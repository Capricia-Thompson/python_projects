from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/play')
# def play():
#     return render_template("index.html", color="blue", times=3)


@app.route('/play/<x>/<color>')
def play(x, color):
    return render_template("index.html", color=color, times=int(x))


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
# import statements, maybe some other routes
