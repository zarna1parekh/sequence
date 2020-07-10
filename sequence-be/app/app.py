from flask import Flask
from board_setup import board_setup_blueprint

app = Flask(__name__)
app.register_blueprint(board_setup_blueprint)


@app.route('/')
def hello_world():
    return 'Welcome to teh Sequence Game!'


if __name__ == '__main__':
    app.run()
