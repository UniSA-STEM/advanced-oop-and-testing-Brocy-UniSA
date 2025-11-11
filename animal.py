"""
File: animal.py
Description: <Temporary Description>.
Author: Corey Brooke
ID: 110480857
Username: Brocy076
This is my own work as defined by the
University's Academic Misconduct Policy.
"""

import random
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
    def name(self):
        return self.__name

    @property
    def hunger(self):
        return self.__hunger

    @property
    def _name_display(self):
        return f"{self.__name} ({self.__species.upper()})"

    @property
    def _hunger_display(self):
        return f"Hunger: ({self.__hunger} / {self.__max_hunger})"

    def eat_snack(self):
        self.__hunger = min(self.__hunger + self.__max_hunger // 2, 100)
        return (
            f"{self._name_display} ate a snack."
            f"\n{self._hunger_display}.")

    def eat_food(self):
        if self.__enclosure.food_amount == 0:
            return (
                f"{self._name_display} is getting sad, because "
                f"there is no food in the enclosure.")

        options = [
            (0.10, (75, 100), "was very hungry and ate a lot!"),
            (0.25, (50, 75), "was hungry and ate heartily."),
            (0.50, (25, 50), "ate a moderate amount."),
            (0.75, (10, 25), "had a light snack.")
        ]

        hunger_ratio = self.__hunger / self.__max_hunger

        for threshold, amount_range, message in options:
            if hunger_ratio <= threshold and self.__enclosure.food_amount > 0:
                food_eaten = random.randint(*amount_range)
                food_eaten = min(food_eaten, self.__enclosure.food_amount)

                self.__enclosure.food_amount -= food_eaten
                self.__hunger = min(self.__hunger + food_eaten,
                                    self.__max_hunger)

                return (
                    f"{self._name_display} {message}\n"
                    f"{self._hunger_display}\n"
                    f"Food remaining in enclosure: "
                    f"{self.__enclosure.food_amount}"
                )

        return f"{self._name_display} is not hungry right now."

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    def __str__(self):
        return (
            f"{self._name_display} - Age: {self.__age} "
            f"\n{self._hunger_display}.")


class Bird(Animal):
    def __init__(self, name, species, age, dietary_needs,
                 enclosure: Enclosure | None = None):
        super().__init__(name, species, age, dietary_needs, enclosure)

    def make_sound(self):
        print("*Skwwackk*")

    def sleep(self):
        print(
            f"shhh... *zzZzZZz* {super()._name_display}, has fallen asleep.")


class Mammal(Animal):
    def __init__(self, name, species, age, dietary_needs,
                 enclosure: Enclosure | None = None):
        super().__init__(name, species, age, dietary_needs, enclosure)

    def make_sound(self):
        print("*Growls*")

    def sleep(self):
        print(
            f"shhh... *zzZzZZz* {super()._name_display}, has fallen asleep.")


class Reptile(Animal):
    def __init__(self, name, species, age, dietary_needs,
                 enclosure: Enclosure | None = None):
        super().__init__(name, species, age, dietary_needs, enclosure)

    def make_sound(self):
        print("*SSssSssSs*")

    def sleep(self):
        print(
            f"shhh... *zzZzZZz* {super()._name_display}, has fallen asleep.")
