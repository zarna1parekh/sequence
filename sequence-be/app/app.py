from flask import Flask
from endpoints import endpoints_blueprint

app = Flask(__name__)
app.register_blueprint(endpoints_blueprint)


@app.route('/')
def hello_world():
    return 'Welcome to the Sequence Game!'


if __name__ == '__main__':
    app.run()
