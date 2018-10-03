from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    data = [1, 2, 3]
    return render_template("index.html", data=data)

@app.route('/about')
def about():
    return 'about page'