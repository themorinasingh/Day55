from flask import Flask

app = Flask(__name__)

#rendering one heading
@app.route("/")
def greet():
    return "<h1>Jai Bajrang Bali Ji</h1>"

#using css mid tags
@app.route("/home")
def greet_2():
    return '<H1 style="text-align: center">Jai Shri Ram Ji</H2>'

#using multiple lines of html
@app.route("/lib")
def greet_3():
    return ('<H1 style="text-align:center;color:lightgrey">Lorem Ipsum</H1>'
            '<p>Lorem ipsum bacon</p>'
            '<p>Lorem Ipsum Bacon</p>')

#adding imaagess
@app.route("/image")
def giphy():
    return '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExczY3dzBvbTNkeWJ6Z2xqbGdmeGdrZTRua2Jya3M1MTY1MmE2Z2FzaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/d5ktzgbVFftMkLaZ33/giphy.gif"/>'
app.run(debug=True)