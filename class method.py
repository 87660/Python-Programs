class Employee:
    companyname = "Microsoft"
    def show(self):
        print(f"The name is {self.name} and the company name is {self.companyname}. ")

    def changeCompany(cls , newCompany):
       cls.companyname= newCompany

e1 = Employee()
e1.name = "Shreya"
e1.show()
e1.changeCompany("Tesla")
e1.show()

print(Employee.companyname)