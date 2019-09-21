from flask import Flask, json, request
app = Flask(__name__)

@app.route('/', methods = ['POST'])
def test_route():
    return json.dumps(request.json)
