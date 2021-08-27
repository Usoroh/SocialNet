from flask import Flask

app = Flask(__name__)

@app.route("/ars")
def hello_world():
    return "<p>Здарова, азиат!</p>"