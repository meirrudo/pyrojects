
class Employee():

    firstName = ""
    lastName = ""

    def __init__(self,firstName = "",lastName = ""):
        self.firstName = firstName
        self.lastName = lastName

    def getEmployeeName(self):
        return  self.firstName + " " + self.lastName




a = Employee("John","Doe")

print(a.getEmployeeName())