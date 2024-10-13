from flask import Flask
app = Flask(__name__)

@app.route("/home")
def hello_world():
    return "Hello Worlds!"

@app.route("/name/<username>")
def welcome(username):
    return f"Hello {username}"

######################Debug mode#############################
@app.route("/<name>")
def greet(name):
    return f"{name + 444}"
#this code will get us the debug screen

path_to_suuccess = "Asli pehalwan ki pehchaan akhade mein nahi, zindagi mein hove hai ... taki jab zindagi tumhe patke toh tum phir khade ho ... aur aaisa daanv maro ki zindagi chitt ho jaye"

@app.route("/secret/<string:name>/<int:age>")
def secret(name, age):
    global path_to_suuccess
    quote = path_to_suuccess
    return f"Hi {name}, your age is {age} \n quote for you{quote}"


if __name__==("__main__"):
    app.run(debug=True)