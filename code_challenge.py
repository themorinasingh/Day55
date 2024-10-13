from flask import Flask
app = Flask(__name__)
#####################################################
def make_bold(function):
    def wrapper_function():
        output = function()
        return "<b>" + output + "</b>"
    return wrapper_function

def make_italic(function):
    def wrapper_function():
        output = function()
        return "<em>" + output + "</em>"
    return wrapper_function



@app.route("/")
@make_bold
@make_italic
def greet():
    return "Lorem Ipsum"

if __name__=="__main__":
    app.run(debug=True)








