from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

if __name__ == "__main__" :
    app.run(host="localhost",port=10000,debug=True)