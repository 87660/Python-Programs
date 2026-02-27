#factorial(9)=9*8*7*6*5*4*3*2*1
# factorial(n)=n * factorial(n-1)
def factorial(n):
    if(n==0 or n==1):
      return 1
    else:
       return n * factorial(n-1)
    
print(factorial(3))
print(factorial(8))
print(factorial(7))

#print(factorial(5))
#5 * factorial(4)
#5 * 4 * factorial(3)
#5 * 4 * 3 * factorial(2)
#5 * 4 * 3 * 1 * factorial(1)
#5 * 4 * 3 * 2 * 1

# write a program to print fibonacci series
# f0=0
# f1=1
# f2=f1 + f0
# fn=f(n-1) + f(n-2)

def fibonacci(n):
   if(n==0 or n==1):
      return n
   else:
     return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(8))
print(fibonacci(2))
print(fibonacci(7))