"""
File: animal.py
Description: <Temporary Description>.
Author: Corey Brooke
ID: 110480857
Username: Brocy076
This is my own work as defined by the
University's Academic Misconduct Policy.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, species, age, dietary_needs):
        self.name = name
        self.species = species
        self.age = age
        self.dietary_needs = dietary_needs

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Bird(Animal):
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs)

    def eat(self):
        pass

    def make_sound(self):
        pass

    def sleep(self):
        pass


class Mammal(Animal):
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs)

    def eat(self):
        pass

    def make_sound(self):
        pass

    def sleep(self):
        pass


class Reptile(Animal):
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs)

    def eat(self):
        pass

    def make_sound(self):
        pass

    def sleep(self):
        pass
