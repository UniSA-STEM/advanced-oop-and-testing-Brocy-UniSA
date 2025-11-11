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

    def refill_food(self):
        self.__food_storage = self.__max_food_storage

    def __str__(self):
        return (f"ENCLOSURE: {self.__size} - {self.__environmental_type}"
                f"\nFOOD AMOUNT: ({self.__food_storage} / "
                f"{self.__max_food_storage})"
                f"\nCLEANLINESS: ({self.__cleanliness_level} / 100)")
