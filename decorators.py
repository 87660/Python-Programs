# decorators is a function that takes another function as an argument and returns a new function 
# that modifies the behaviour of the original function . And a new function is reffered to as a "decorated" function
def greet(fx):     # decorator
    def mfx():
        print("Good morning")
        fx()
        print("Thanks for using function")
    return mfx

@greet
def hello():
    print("Hello World")

hello()

def add(a,b):
    print(a+b)
