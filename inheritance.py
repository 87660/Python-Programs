class Employee:
    def __init__(self, name , id):
      self.name= name
      self.id = id
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


class Programmer(Employee):    # employee is inherited to programmer
  def showLanguage(self):
      print("The default language is Python. ")

e = Employee("Rohit Sharma",45)
e.showDetails()

e = Programmer("Rohit Sharma",45)
e.showLanguage()
