# class variables are defined at class level and shared among all instances of class
# they are defined outside of any method and are usually used to store information that is common to all instance of the class.


class Employee:
    companyname = "Apple"       #class variables
    def __init__(self, name):
        self.name=name            # instance variables
        self.raise_amount = 0.02

    def showDetails(self):
        print(f"The name of employee is {self.name} and the raise_amount in the {self.companyname} is {self.raise_amount}.")


emp1 = Employee("Shreya")
emp1.raise_amount = 0.3
emp1.showDetails()


emp2 = Employee("Sakshi")
emp2.showDetails()