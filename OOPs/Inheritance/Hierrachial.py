class Animal:
    def eat(self):
        print("Eating...")


class Dog(Animal):
    def bark(self):
        print("Barking....")


class Cat(Animal):
    def meow(self):
        print("Meowing...")


a = Animal()  # Object for Animal
d = Dog()     # Object for Dog
c = Cat()     # Object for Cat