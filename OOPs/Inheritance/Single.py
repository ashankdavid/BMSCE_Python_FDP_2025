class Animal:
    def eat(self):
        print("Eating...")


class Dog(Animal):
    def bark(self):
        print("Barking....")


a = Animal()  # Object for Animal
d = Dog()     # Object for Dog

a.eat()

d.bark()
d.eat()
