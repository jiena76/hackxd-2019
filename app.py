from flask import Flask, json, request
app = Flask(__name__)

@app.route('/', methods = ['POST'])
def test_route():
  # print(request.form["url"])
  return request.json

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8000, debug=True)
