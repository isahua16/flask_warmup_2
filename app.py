from dbhelpers import run_statement
from apihelpers import check_data
from flask import Flask, request
import json
import uuid
app = Flask(__name__)
@app.post('/api/client')
def insert_client():
    error = check_data(request.json, ['username', 'email', 'password', 'image_url'])
    if(error != None):
        return error
    results = run_statement('call insert_client(?,?,?,?)', [request.json.get('username'), request.json.get('email'), request.json.get('password'), request.json.get('image_url')])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "Something is wrong"

@app.post('/api/login')
def insert_login():
    error = check_data(request.json, ['username', 'password'])
    if(error != None):
        return error
    token = uuid.uuid4().hex
    results = run_statement('call insert_login(?,?,?)', [request.json.get('username'), request.json.get('password'), token])
    if(type(results) == list and results[0][0] == 1):
        return "User logged in"
    else:
        return "Something went wrong"

app.run(debug=True)
