class Person:  # class
 name = "Shreya"
 occupation = "Software Developer"
 networth = 100000


 # self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class
 def info(self):  #method
   print(f"{self.name} is a {self.occupation}.")

a = Person()   # object
# a.name = "Rohit"
# a.occupation = "Developer"
# print(a.name , a.occupation , a.networth)

a.info()