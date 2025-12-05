# OOP Concepts
# Encapsulation, Inheritance, Polymorphism, Extraction
# Written for Infosys Springboard internship assessment.
# Each concept has very simple beginner-friendly examples.

# --------------------------------------------------------
# Encapsulation Examples
# --------------------------------------------------------
# Encapsulation means hiding data inside a class and giving
# access only through methods.

# Example 1
class Student:
    def __init__(self):
        self.__marks = 90   # hidden variable

    def get_marks(self):
        return self.__marks


# Example 2
class Account:
    def __init__(self):
        self.__balance = 0  # private data

    def deposit(self, amt):
        self.__balance += amt


# Example 3
class Person:
    def __init__(self):
        self.__age = 20

    def set_age(self, age):
        if age > 0:
            self.__age = age


# --------------------------------------------------------
# Inheritance Examples
# --------------------------------------------------------
# Inheritance means one class taking features from another.

# Example 1
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    pass


# Example 2
class Vehicle:
    def move(self):
        return "Vehicle moving"

class Car(Vehicle):
    pass


# Example 3
class PersonBase:
    def say(self):
        return "Hello"

class StudentPerson(PersonBase):
    pass


# --------------------------------------------------------
# Polymorphism Examples
# --------------------------------------------------------
# Polymorphism means same method name but different behavior.

# Example 1
class DogPoly:
    def sound(self):
        return "Woof"

class CatPoly:
    def sound(self):
        return "Meow"


# Example 2
class English:
    def greet(self):
        return "Hello"

class Telugu:
    def greet(self):
        return "Namaskaram"


# Example 3
class Bike:
    def wheels(self):
        return 2

class CarPoly:
    def wheels(self):
        return 4


# --------------------------------------------------------
# Extraction Examples
# --------------------------------------------------------
# Extraction means taking common code out into a separate
# helper class to avoid repeating logic.

# Example 1
class MathHelper:
    def add(self, a, b):
        return a + b

class Marks:
    def total(self, m1, m2):
        return MathHelper().add(m1, m2)


# Example 2
class TextHelper:
    def upper(self, text):
        return text.upper()

class Message:
    def show(self, msg):
        return TextHelper().upper(msg)


# Example 3
class NameHelper:
    def full(self, first, last):
        return first + " " + last

class User:
    def display(self):
        return NameHelper().full("Teja", "Sri")
