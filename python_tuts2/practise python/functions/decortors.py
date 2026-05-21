"""   
burger-function
extra cheesre -extra feature

main function ek aur function add
without changing main function 


"""

"""  
creation of decorator

def decorator_function(any_function):
    def wrapper_function():
        print("this is extra feature")
        any_function()
        print
    return wrapper_function

@decorator_function
def function_to_be_decorated():
def say_hello():
    print("hello world")
say_hello()

"""

def decorator(func):
    def wrapper():  # it helps to add extra features
        print("this is extra feature added")
        func()  # it helps to call the main function
        print("this is another extra feature added after the main function")
    return wrapper

@decorator
def main_function():
    print("this is the main function")

main_function()
