"""
File: health_issue.py
Description: <Temporary Description>.
Author: Corey Brooke
ID: 110480857
Username: Brocy076
This is my own work as defined by the
University's Academic Misconduct Policy.
"""
from datetime import date

class HealthIssue:
    def __init__(self, description: str, severity: str,
                 date_reported = None,
                 treatment_plan: str = ""):
        self.__description = description.capitalize()
        self.__severity = severity
        self.__date_reported = date_reported or date.today()
        self.__treatment_plan = treatment_plan
        self.__resolved = False
        self.__notes: list[str] = []

    def __str__(self) -> str:
        status = "RESOLVED" if self.__resolved else "ACTIVE"
        return (
            f"STATUS: {status} ({self.__severity.upper()})\n"
            f"REPORTED: {self.__date_reported}\n"
            f"DESCRIPTION: {self.__description}\n"
            f"TREATMENT: {self.__treatment_plan}")

    def add_note(self, note: str):
        self.__notes.append(note)

    def mark_resolved(self, note: str = ""):
        self.__resolved = True
        if note:
            self.__notes.append(f"[RESOLUTION NOTE: {note}]")
        else:
            self.__notes.append("[RESOLVED]")

