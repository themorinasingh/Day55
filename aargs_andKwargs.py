from flask import Flask
############################################################
app = Flask(__name__)
############################################################
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

    def login(self):
        self.is_logged_in = True

def authenticator(function):
    def wrapper_function(*args):
        is_authenticated = args[0].is_logged_in
        if is_authenticated:
            return function(args[0])
        else:
            print("User is not logged in")

    return wrapper_function



@authenticator
def create_blog(user):
    print(f"Here is {user.name}'s new blog")

morina = User("morina")

create_blog(morina)
morina.login()
create_blog(morina)













