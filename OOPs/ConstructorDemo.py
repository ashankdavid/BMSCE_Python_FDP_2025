# Program to understand that constructors will get called even if u don't create it
class Demo:
    def __init__(self):
        print("I'm a Constructor")


obj1 = Demo()