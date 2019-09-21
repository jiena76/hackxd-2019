from flask import Flask, json, request, jsonify
from backend import text_processing
app = Flask(__name__)

@app.route('/', methods = ['POST'])
def test_route():
  print("----------------------------------------------------")
  print(request.json["url"])
  print("----------------------------------------------------")

  name_collected = text_processing.predict_collection('./backend/data/name_data.csv',  request.json["url"])
  email_collected = text_processing.predict_collection('./backend/data/email_data.csv', request.json["url"])
  return_data = {
    "name": name_collected,
    "email": email_collected
  }

  return jsonify(return_data)

if __name__ == '__main__':
  text_processing.download_packages()
  app.run(host="0.0.0.0", port=8000, debug=True)
