from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    data = [1, 2, 3]
    data_dict = [{"x": 3} , {"x": 5}, {"x": 1}]
    return render_template("index.html", data=data_dict)

@app.route('/about')
def about():
    return 'about page'