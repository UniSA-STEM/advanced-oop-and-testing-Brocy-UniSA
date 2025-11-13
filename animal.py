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
                 dietary_needs: list[str]):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_needs = dietary_needs
        self.__hunger = 0
        self.__max_hunger = 100
        self.__enclosure = None

    def __str__(self):
        return (
            f"{self.name_display} - Age: {self.__age} "
            f"\n{self.hunger_display}.")

    # Properties

    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species

    @property
    def hunger(self):
        return self.__hunger

    @hunger.setter
    def hunger(self, value):
        self.__hunger = max(0, min(value, self.__max_hunger))

    @property
    def max_hunger(self):
        return self.__max_hunger

    @property
    def enclosure(self):
        return self.__enclosure

    @property
    def name_display(self):
        return f"{self.__name} ({self.__species.upper()})"

    @property
    def hunger_display(self):
        return f"Hunger: ({self.__hunger} / {self.__max_hunger})"

    # Eating

    def eat_snack(self):
        self.__hunger = min(self.__hunger + self.__max_hunger // 2, 100)
        self.__enclosure.cleanliness_level -= random.randint(1, 5)
        return (f"{self.name_display} ate a snack."
                f"\n{self.hunger_display}.")

    def eat_food(self):
        if self.__enclosure is None:
            return (f"{self.name_display} needs to be put in an "
                    f"enclosure.")

        if self.__enclosure.food_amount == 0:
            return f"there is no food in the enclosure."

        hunger_ratio = self.__hunger / self.__max_hunger

        options = [
            (0.10, (75, 100), "was very hungry and ate a lot!", (2, 5)),
            (0.25, (50, 75), "was hungry and ate heartily.", (1, 4)),
            (0.50, (25, 50), "ate a moderate amount.", (0, 3)),
            (0.75, (10, 25), "had a light snack.", (0, 2))
        ]

        for threshold, amount_range, message, mess in options:
            if hunger_ratio <= threshold:
                food_eaten = random.randint(*amount_range)
                food_eaten = min(food_eaten, self.__enclosure.food_amount)

                self.__enclosure.cleanliness_level -= random.randint(*mess)
                self.__enclosure.food_amount -= food_eaten
                self.__hunger = min(self.__hunger + food_eaten, 100)

                return (f"{self.name_display} {message}\n"
                        f"{self.hunger_display}\n"
                        f"Food remaining: "
                        f"{self.__enclosure.food_amount}")

        return f"{self.name_display} is not hungry right now."

    # Enclosure Management

    def assign_enclosure(self, enclosure: Enclosure):
        if (self.species == enclosure.species_housed or
                enclosure.species_housed is None):

            if enclosure.check_availability():
                enclosure.add_animal(self)
                self.__enclosure = enclosure
                return (f"{self.name_display} has been added to this "
                        f"enclosure.")

            return (f"There is not enough space in this enclosure for "
                    f"{self.name_display}.")

        return (f"This is a {enclosure.species_housed} enclosure. "
                f"{self.name_display} is not a "
                f"{enclosure.species_housed}.")

    def remove_enclosure(self):
        if self.__enclosure is None:
            return f"{self.name_display} isn't in an enclosure."

        self.__enclosure.remove_animal(self)
        self.__enclosure = None
        return (f"{self.name_display} has been removed from this "
                f"enclosure.")

    # Abstract methods

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def interact_with_environment(self):
        pass

    @abstractmethod
    def enrichment_activity(self):
        pass


# SubClasses

class Bird(Animal):
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs)

    def make_sound(self):
        self.hunger -= random.randint(1, 3)
        return f"{super().name_display} Squawks"

    def sleep(self):
        self.hunger -= random.randint(35, 50)
        self.enclosure.cleanliness_level -= random.randint(1, 3)
        return (f"shhh... *blub-blub* {super().name_display}, "
                f"has fallen asleep.")

    def move(self):
        self.hunger -= random.randint(1, 5)
        self.enclosure.cleanliness_level -= random.randint(1, 3)
        return (f"{self.name_display} flutters and hops around the "
                f"enclosure.")

    def interact_with_environment(self):
        self.hunger -= random.randint(5, 10)
        self.enclosure.cleanliness_level -= random.randint(1, 3)
        return (f"{self.name_display} pecks at branches and explores "
                f"perches.")

    def enrichment_activity(self):
        self.hunger -= random.randint(3, 7)
        self.enclosure.cleanliness_level -= random.randint(1, 3)
        return f"{self.name_display} plays with a hanging bell toy."


class Mammal(Animal):
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs)

    def make_sound(self):
        self.hunger -= random.randint(1, 3)
        return f"{super().name_display} Growls"

    def sleep(self):
        self.hunger -= random.randint(35, 50)
        self.enclosure.cleanliness_level -= random.randint(1, 3)
        return (f"shhh... *zzZzZZz* {super().name_display}, "
                f"has fallen asleep.")

    def move(self):
        self.hunger -= random.randint(1, 5)
        self.enclosure.cleanliness_level -= random.randint(1, 3)
        return f"{self.name_display} stomps around the enclosure."

    def interact_with_environment(self):
        self.hunger -= random.randint(5, 10)
        self.enclosure.cleanliness_level -= random.randint(1, 3)
        return (f"{self.name_display} digs, sniffs, and explores the "
                f"area.")

    def enrichment_activity(self):
        self.hunger -= random.randint(3, 7)
        self.enclosure.cleanliness_level -= random.randint(1, 3)
        return (f"{self.name_display} enjoys a puzzle feeder filled "
                f"with treats.")


class Reptile(Animal):
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs)

    def make_sound(self):
        self.hunger -= random.randint(1, 3)
        return f"{super().name_display} Hisses"

    def sleep(self):
        self.hunger -= random.randint(35, 50)
        self.enclosure.cleanliness_level -= random.randint(1, 3)
        return (f"shhh... *ssSSs* {super().name_display}, "
                f"has fallen asleep.")

    def move(self):
        self.hunger -= random.randint(1, 5)
        self.enclosure.cleanliness_level -= random.randint(1, 3)
        return f"{self.name_display} slowly moves to a new warm spot."

    def interact_with_environment(self):
        self.hunger -= random.randint(5, 10)
        self.enclosure.cleanliness_level -= random.randint(1, 3)
        return (f"{self.name_display} basks in hotspots and hides "
                f"under rocks.")

    def enrichment_activity(self):
        self.hunger -= random.randint(3, 7)
        self.enclosure.cleanliness_level -= random.randint(1, 3)
        return f"{self.name_display} explores new hiding spots."
