from flask import Flask
import random
############################################################################
app = Flask(__name__)
############################################################################
@app.route("/")
def greeter():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>")
############################################################################
num_list = [num + 1 for num in range(0, 9) ]
random_number = random.choice(num_list)
path  = f"/{random_number}"
@app.route(path)
def you_found_me():
    return ("<h1>You Found Me</h1>"
            "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnNxYnNxM2MyZ2d3M3EyamI2ZmR1a2UzcWt2MnBmODlrd3kycDU1MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fFhZJSGbIzosqG1bty/giphy.gif'/>")

@app.route("/<int:number>")
def comparer(number):
    global random_number
    main_num = random_number
    if number > random_number:
        return ("<h1>Too High</h1>"
                "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNG5vYnNmMGN5d2Q1YzMwNWhmZXA4cXljN2Fzc3B2MzJ4cnhxbG81dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iacwXyWu2bYTS/giphy.gif' />")
    elif number < random_number:
        return ("<h1>Too Low</h1>"
                "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNG5vYnNmMGN5d2Q1YzMwNWhmZXA4cXljN2Fzc3B2MzJ4cnhxbG81dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iacwXyWu2bYTS/giphy.gif' />")




############################################################################
if __name__=="__main__":
    app.run(debug=True)