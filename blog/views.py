from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    
    message = "This is get request"
    if request.method == "POST":
        message = "This is post"
    return render_template("index.html", message=message)

@app.route('/about')
def about():
    return 'about page'