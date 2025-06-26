from flask import Flask, request
import platform
import sys

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello, {name}!'

@app.route('/info')
def info():
    python_version = sys.version
    os_info = platform.platform()
    return f'Python Version: {python_version}<br>OS: {os_info}'

if __name__ == '__main__':
    app.run(debug=True)
