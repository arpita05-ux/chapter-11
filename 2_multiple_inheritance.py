class Employee:        # base class
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")


class coder():
    language = "Python"
    def printlanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")


class Programmer(Employee, coder):        # Derived or child class    
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printlanguage()
b.showLanguage()

 