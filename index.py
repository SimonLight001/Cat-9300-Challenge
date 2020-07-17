from flask import Flask
import requests
import pysnmp

app = Flask(__name__)

print("--- Starting teams bot ---")

data = {'roomId':'room','text':'Tesing123'}

@app.route("/")
def hello():
    r = requests.post('http://webexapis.com/v1/messages', data=data)
    return r.text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)
