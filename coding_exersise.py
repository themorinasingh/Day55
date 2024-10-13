def logging_decorator(func):
    def wrapper(*args):
        output = func(*args)

        print(f"You called {func.__name__}{args} \nand it returned {output}")


    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)


#this coding exersise was already done