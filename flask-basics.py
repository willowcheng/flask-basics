from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name="Willow"):
    return "Hello from {}".format(name)


@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    return '{} + {} = {}'.format(num1, num2, num1 + num2)


app.run(debug=True, port=8000, host='127.0.0.1')
# @app.route('/')
# def hello_world():
# return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()
