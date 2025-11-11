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
        enclosure_space = (f"({len(self.__animals_in_enclosure)} / "
                           f"{self.__max_animals_in_enclosure})")
        enclosure_food_space = (f"({self.__food_storage} / "
                                f"{self.__max_food_storage})")
        header_text = (f"ENCLOSURE: {self.__size} {enclosure_space}"
                       f" - {self.__environmental_type}"
                       f"\nFOOD AMOUNT: {enclosure_food_space}"
                       f"\nCLEANLINESS: "
                       f"({self.__cleanliness_level} / 100)")

        animal_blocks = (
            [str(a).split("\n") for a in self.__animals_in_enclosure]
            if self.__animals_in_enclosure
            else [["No animals currently in this enclosure."]])

        all_lines = header_text.split("\n") + [line for block in animal_blocks
                                               for line in block]
        max_width = max(len(line) for line in all_lines)

        header_border = "+" + "=" * (max_width + 2) + "+"
        animal_border = "+" + "-" * (max_width + 2) + "+"

        header_section = (
                f"{header_border}\n"
                + "\n".join(f"| {line.ljust(max_width)} |" for line in
                            header_text.split("\n"))
                + f"\n{header_border}"
        )

        animal_sections = []
        for block in animal_blocks:
            animal_text = "\n".join(
                f"| {line.ljust(max_width)} |" for line in block)
            animal_sections.append(f"{animal_text}\n{animal_border}")
        animals_section = "\n".join(animal_sections)

        return f"{header_section}\n{animals_section}"
