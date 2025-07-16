from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def eat(self):
        pass

class Dog(Animal):
    def eat(self):
        print("Dog Food")


d = Dog()
d.eat()