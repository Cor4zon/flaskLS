from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'New version of my web application!'


if __name__ == '__main__':
    app.run()
