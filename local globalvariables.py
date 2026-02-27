# local variable is defined within the function and only accessible within that same function.
# global variable is the variable which declared outside the function and can be accessible within the program and in any function.
x=4
print(x)


def hello():
    x=5
    print(x)

    print(f"the local value of x is {x}.")

print(f"the global value of x is {x}.")
hello()