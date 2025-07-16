class Animal:
    def eat(self):
        print("Eating...")


class Dog(Animal):
    def bark(self):
        print("Barking....")

class Puppy(Dog):
    def cry(self):
        print("Crying...")


a = Animal()  # Object for Animal
d = Dog()  # Object for Dog
p = Puppy() # Object of Puppy

a.eat()

d.bark()
d.eat()

p.eat()
p.bark()
p.cry()
