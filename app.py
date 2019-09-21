from flask import Flask, json, request
from backend import text_processing
app = Flask(__name__)

@app.route('/', methods = ['POST'])
def test_route():

  print(request.json)
  # text_processing.train_model('data/name_data.csv',  request.json["url"])
  # text_processing.train_model('data/email_data.csv', request.json["url"])
  return json.dumps(request.json)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8000, debug=True)