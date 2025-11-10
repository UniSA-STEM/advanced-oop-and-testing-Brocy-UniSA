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
    def __init__(self):
        pass

    @abstractmethod
    def do_stuff(self):  # temp function name
        pass

    def feed_animal(self):
        pass

    def clean_enclosures(self):
        pass

    def conduct_animal_health_check(self):
        pass


class Zookeeper(Staff):
    def do_stuff(self):
        pass


class Veterinarian(Staff):
    def do_stuff(self):
        pass
