from duplicate_error import DuplicateEventException
from event import Event
from typing import List


class Calendar:
    def __init__(self, events: List[Event]):
        self.events = events
        self.events.sort(key=lambda x: x.date_from)
        self.date_format = "%d-%m-%Y"

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.events):
            result = self.events[self.i]
            self.i += 1
            return result

        raise StopIteration

    def add_event(self, event: Event):
        if event not in self.events:
            self.events.append(event)
            self.events.sort(key=lambda x: x.date_from)
        else:
            raise DuplicateEventException()

    def remove_event(self, event: Event):
        self.events.remove(event)
