class Parent:
    def __init__(self):
        print("This is Parent Constructor")


class Child(Parent):
    def __init__(self):
        print("This is Child Constructor")

c = Child()