class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self,name, age, usn):
        super().__init__(name, age)
        self.usn = usn

    def printDetails(self):
        print(f"The Student name is {self.name}")
        print(f"The Student Age is {self.age}")
        print(f"The Student USN is {self.usn}")

s = Student("Ashank", 30, 123)
s.printDetails()