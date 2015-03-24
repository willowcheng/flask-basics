from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index(name="Willow"):
    name = request.args.get('name', name)
    return "Hello from {}".format(name)

app.run(debug=True, port=8000, host='127.0.0.1')
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()
