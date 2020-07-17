from flask import Flask

app = Flask(__name__)

print("--- Starting teams bot ---")

@app.route("/")
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)
