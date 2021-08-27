from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Здарова, азиат!</p><div><a href='/login'>Войди на сайт</a></div>"

@app.route("/login")
def login():
    return "<p>Здесь будет авторизация</p><div><a href='/register'>Новенький? Зарегайся</a></div>"

@app.route("/register")
def register():
    return "<p>Здесь будет регистрация</p><div><a href='/login'>Уже зареган? Войди на сайт</a>"

@app.route("/<name>")
def hello(name):
    return f"Cтраницы {escape(name)} не существует!"
   

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
