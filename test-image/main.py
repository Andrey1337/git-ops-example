from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello'


def main():
    app.run('0.0.0.0', '1337')


if __name__ == '__main__':
    main()
