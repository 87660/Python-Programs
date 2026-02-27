#static methods in Python are methods that belongs to a class rather then n instance of the class. They are defined using the @staticmethod decorator 
# and do not have access to the class.

class Math:
    def __init__(self , num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num +n


    @staticmethod
    def add(a, b):
        return a + b
    
# result = Math.add(1, 2)
# print(result)     # output: 3

a= Math(5)
print(a.num)

a.addtonum(6)
print(a.num)

print(a.add(7 , 2))