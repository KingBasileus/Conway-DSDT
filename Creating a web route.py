from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Testing"


@app.route("/maths")
def maths():
        return "THis page is about maths"

@app.route("/testing")
def testing():
        return "This page is abouth testing"

@app.route("/mathsv2")
def add_num():
      num1 = 1
      num2 = 2
      result = num1 + num2
      return "If you add both together you get: " + str(result)

if __name__ == "__main__":
    app.run(debug=True)