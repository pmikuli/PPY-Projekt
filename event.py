from datetime import datetime


class Event:
    def __init__(self, date_from: datetime, date_to: datetime, description: str):
        self.date_from = date_from
        self.date_to = date_to
        self.description = description

    def __iter__(self):
        return iter([self.date_from, self.date_to, self.description])

    def __eq__(self, other):
        if type(other) is Event:
            return self.date_from == other.date_from and self.date_to == other.date_to and self.description == other.description

        return False
