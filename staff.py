"""
File: staff.py
Description: <Temporary Description>.
Author: Corey Brooke
ID: 110480857
Username: Brocy076
This is my own work as defined by the
University's Academic Misconduct Policy.
"""

from abc import ABC, abstractmethod


class Staff(ABC):
    def __init__(self, name):
        self.__name = name
        self.__assigned_animal = []
        self.__assigned_enclosure = []

    @abstractmethod
    def daily_tasks(self):
        pass

    def feed_animal(self, animal):
        if animal.hunger == animal.max_hunger:
            return (f"{animal.name_display} was not hungry and went to"
                    f" play.")
        animal.eat_snack()
        return f"{self.__name} fed {animal.name_display}."

    def refill_enclose_food(self, enclosure):
        if enclosure.max_food == enclosure.max_food_amount:
            return f"This enclosure doesn't need more food"
        enclosure.refill_food()
        return f"{self.__name} has filled up the enclosure with food."

    def clean_enclosures(self):
        pass

    def conduct_animal_health_check(self):
        pass


class Zookeeper(Staff):
    def daily_tasks(self):
        pass


class Veterinarian(Staff):
    def daily_tasks(self):
        pass
