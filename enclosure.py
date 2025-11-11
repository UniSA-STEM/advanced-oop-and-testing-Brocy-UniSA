"""
File: enclosure.py
Description: <Temporary Description>.
Author: Corey Brooke
ID: 110480857
Username: Brocy076
This is my own work as defined by the
University's Academic Misconduct Policy.
"""


class Enclosure:
    def __init__(self, size, environmental_type, cleanliness_level):
        self.__size = size
        self.__environmental_type = environmental_type
        self.__cleanliness_level = cleanliness_level
        self.__species_housed = None
        self.__animals_in_enclosure = []
        if self.__size == "Small":
            self.__max_animals_in_enclosure = 2
        elif self.__size == "Medium":
            self.__max_animals_in_enclosure = 5
        elif self.__size == "Large":
            self.__max_animals_in_enclosure = 10
        self.__food_storage = 0
        if self.__size == "Small":
            self.__max_food_storage = 50
        elif self.__size == "Medium":
            self.__max_food_storage = 100
        elif self.__size == "Large":
            self.__max_food_storage = 200

    @property
    def food_amount(self):
        return self.__food_storage

    @food_amount.setter
    def food_amount(self, value):
        self.__food_storage = max(0, min(value, self.__max_food_storage))

    @property
    def species_housed(self):
        return self.__species_housed

    def refill_food(self):
        self.__food_storage = self.__max_food_storage

    def check_availability(self):
        if len(self.__animals_in_enclosure) >= self.__max_animals_in_enclosure:
            return False
        return True

    def add_animal(self, animal):
        if self.__species_housed is None:
            self.__species_housed = animal.species
        self.__animals_in_enclosure.append(animal)

    def __str__(self):
        return (f"ENCLOSURE: {self.__size} - {self.__environmental_type}"
                f"\nFOOD AMOUNT: ({self.__food_storage} / "
                f"{self.__max_food_storage})"
                f"\nCLEANLINESS: ({self.__cleanliness_level} / 100)")
