from flask import Flask

# Это уже знакомое callable WSGI-приложение
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to Skypro!'


@app.get('/users')
def users_get():
    return 'GET /users'


@app.post('/users')
def users_post():
    return 'POST /users'
