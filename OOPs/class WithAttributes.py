# Classes With Attributes or Constructor
class Student:
    def __init__(self, name, usn):
        self.name = name
        self.usn = usn

    def printDetails(self):
        print(f"Name is {self.name}")
        print(f"USN is {self.usn}")


s1 = Student("Ashank", 123)
s2 = Student("Abhishek", 234)

s1.printDetails()
s2.printDetails()