from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello'


@app.route('/test')
def hello_world():
    return 'Test'


def main():
    app.run('0.0.0.0', '8080')


if __name__ == '__main__':
    main()
