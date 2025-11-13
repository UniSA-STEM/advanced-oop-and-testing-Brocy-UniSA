"""
File: staff.py
Description: <Temporary Description>.
Author: Corey Brooke
ID: 110480857
Username: Brocy076
This is my own work as defined by the
University's Academic Misconduct Policy.
"""
import random
from abc import ABC, abstractmethod

from animal import Bird, Mammal, Reptile


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

    def clean_enclosure(self, enclosure):
        if enclosure.cleanliness_level == 100:
            return f"This enclosure doesn't need to be cleaned"
        enclosure.clean_enclosure()
        return f"{self.__name} cleaned up the enclosure"

    def conduct_animal_health_check(self, animal):
        if random.random() < 0.25:
            problem_map = {
                Bird: [
                    "broken wing",
                    "feather loss",
                    "overgrown beak",
                    "parasites",
                    "eye irritation",
                    "skin irritation",
                    "foot sores",
                    "overgrown claws",
                    "feather mites",
                    "wound infection",
                    "avian pox symptoms"
                ],
                Reptile: [
                    "incomplete shed",
                    "retained eye caps",
                    "parasites",
                    "scale damage",
                    "fungal infection",
                    "skin irritation",
                    "overgrown nails",
                    "digestive blockage",
                    "thermal burns",
                    "swollen joints",
                    "stomatitis"
                ],
                Mammal: [
                    "fleas",
                    "ticks",
                    "skin irritation",
                    "dental issues",
                    "ear infection",
                    "parasites",
                    "joint pain",
                    "digestive upset",
                    "overgrown nails",
                    "wound infection",
                    "eye irritation",
                    "allergic reaction",
                    "muscle strain"
                ]
            }

            for species, problems in problem_map.items():
                if isinstance(animal, species):
                    problem = random.choice(problems)
                    return (
                        f"{self.__name} has helped {animal.name_display}"
                        f" with their {problem}.")
                return None
            return None

        else:
            return (f"{self.__name} did not find anything wro"
                    f"ng with {animal.name_display}.")


class Zookeeper(Staff):
    def daily_tasks(self):
        pass


class Veterinarian(Staff):
    def daily_tasks(self):
        pass
