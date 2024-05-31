from typing import List
from calendar import Calendar
import event
import csv


def save_calendar(calendar: Calendar, filename: str):
    with open(filename, 'w') as f:
        w = csv.writer(f)
        for e in calendar:
            w.writerow(list(e))


def load_calendar(filename: str) -> Calendar:
    with open(filename, 'r') as f:
        events = []
        reader = csv.reader(f)
        for row in reader:
            events.append(event.Event(row[0], row[1], row[2]))
        calendar = Calendar(events)
        return calendar





def print_list(lines: List):
    for i in lines:
        print(i)
