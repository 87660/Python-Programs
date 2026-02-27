# lambda function is a small anonymous function without a name. It is defined  using the lambda keyword and has the following syntax: lambda arguments: expression
# def double(x):
#     return x*2

double = lambda x:x*2
cube = lambda x: x*x*x
avg= lambda x,y: (x+y)/2
percentage = lambda x,y:((x+y)/2) *100
print(double(5))
print(cube(2))
print(avg(5, 5))
print(percentage(50, 50))