class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True

random_user = User("mike", "tyson")

def authenticator(function):
    def wrapper(*args, **kwargs):
        is_authenticated = args[0].authenticated
        if is_authenticated:
            return function(args[0])
        else :
            return f"{args[0].username} is not authenticated"

    return wrapper

@authenticator
def make_a_post(user):
    return (f"{user.username} \n"
            "Everything you've ever wanted is sitting on the other side of fear.")

print(make_a_post(random_user))

random_user.authenticate("mike", "tyson")

print(make_a_post(random_user))