from flask import Flask

app = Flask(__name__)

@app.route("/home")
def hello_world():
    return "Hello World!"

@app.route("/")
def welcome():
    print("as")
    return "Welcome To The Club"
app.run()

###############Practice and Warmup#############