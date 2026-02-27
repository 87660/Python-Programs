# Access specifiers are used to limit the access of class variables and methods outside the class while implementing the concept of inheritance
# TYPES: 1- Public    2- Protected     3 - private

class Emp:
    # def __init__(self):
    #     self.name = "Shreya"

    def __init__(self):
        self.__name = "Shreya"   # private access modifier _ _

a= Emp()
# print(a.__name)   #cannot be accessed directly
print(a._Emp__name)   # Can be accessed indirectly
 
# a = Emp()
# print(a.name)