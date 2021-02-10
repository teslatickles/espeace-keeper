from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/light/on', methods=['POST'])
def lightOn():
    print(request.data)
    return str(request.data)

@app.route('/accel', methods=['POST', 'GET'])
def accel():
    if request.method == 'POST':
       print(request.data + "\n")
       return str(request.data)

@app.route('/gyro', methods=['POST', 'GET'])
def gyro():
    if request.method == 'POST':
       print(request.data + "\n")
       return str(request.data)

@app.route('/magneto', methods=['POST', 'GET'])
def magneto():
    if request.method == 'POST':
       print(request.data + "\n")
       return str(request.data)

@app.route('/temp', methods=['POST', 'GET'])
def temp():
    if request.method == 'POST':
       print(request.data + "\n")
       return str(request.data)


app.run(host='0.0.0.0', port=8090)
