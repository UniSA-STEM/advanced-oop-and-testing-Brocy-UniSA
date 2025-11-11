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

from enclosure import Enclosure


class Animal(ABC):
    def __init__(self, name: str, species: str, age: int,
                 dietary_needs: list[str],
                 enclosure: Enclosure | None = None):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_needs = dietary_needs
        self.__hunger = 0
        self.__max_hunger = 100
        self.__enclosure = enclosure

    @property
    def __name_display(self):
        return f"{self.__name} ({self.__species.upper()})"

    @property
    def __hunger_display(self):
        return f"Hunger: ({self.__hunger} / {self.__max_hunger})"

    def eat_snack(self):
        self.__hunger = min(self.__hunger + self.__max_hunger // 2, 100)
        return (
            f"{self.__name_display} ate a snack."
            f"\n{self.__hunger_display}.")

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
