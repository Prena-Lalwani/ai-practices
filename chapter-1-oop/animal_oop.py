from abc import ABC, abstractmethod


# Abstract Base Class (Abstraction)
class Animal(ABC):
    def __init__(self, name, age):
        self.__name = name  # private attribute (Encapsulation)
        self._age = age  # protected attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @staticmethod
    def general_info():
        return "All animals need food and make some kind of sound."

    @classmethod
    def species_info(cls):
        return f"This is the Animal base class: {cls.__name__}"


# Inheritance + Polymorphism
class Carnivore(Animal):
    def sound(self):
        return "Roar!"

    def eat(self):
        return "Eats meat"


class Herbivore(Animal):
    def sound(self):
        return "Moo!"

    def eat(self):
        return "Eats plants"


# Main Program with User Input
if __name__ == "__main__":
    print("Welcome to Animal OOP Program 🐾")

    name = input("Enter animal name: ")
    age = int(input("Enter animal age: "))

    print("\nChoose Animal Type:")
    print("1. Carnivore")
    print("2. Herbivore")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        animal = Carnivore(name, age)
    elif choice == "2":
        animal = Herbivore(name, age)
    else:
        print("Invalid choice, defaulting to Herbivore...")
        animal = Herbivore(name, age)

    print("\n--- Animal Details ---")
    print("Name:", animal.get_name())
    print("Age:", animal._age)  # Normally you'd use a getter
    print("Sound:", animal.sound())
    print("Eating Style:", animal.eat())

    print("\n--- Extra Info ---")
    print(Animal.general_info())
    print(Animal.species_info())
